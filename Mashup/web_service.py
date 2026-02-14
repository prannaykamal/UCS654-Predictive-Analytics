import os
import smtplib
import zipfile
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from flask import Flask, request, render_template_string
import yt_dlp
from pydub import AudioSegment

app = Flask(__name__)

sender_mail = "prannaykamal9@gmail.com" 
sender_pswd = "cnxnefnnhffkbcmt" 

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Mashup Service</title>
    <style>
        body { font-family: sans-serif; margin: 50px; display: flex; justify-content: center; }
        table { border: 1px solid #ccc; padding: 20px; border-radius: 5px; background: #fdfdfd; }
        .btn { background: orange; color: white; border: 1px solid #333; padding: 8px 25px; cursor: pointer; font-weight: bold; }
    </style>
</head>
<body>
    <form method="POST" action="/mashup">
        <table>
            <tr><th colspan="2"><h2>Mashup Generator</h2></th></tr>
            <tr><td>Singer Name:</td><td><input type="text" name="singer" required></td></tr>
            <tr><td># of Videos:</td><td><input type="number" name="count" min="11" required></td></tr>
            <tr><td>Duration (sec):</td><td><input type="number" name="duration" min="21" required></td></tr>
            <tr><td>Email Id:</td><td><input type="email" name="email" required></td></tr>
            <tr><td colspan="2" align="center"><br><button type="submit" class="btn">Submit</button></td></tr>
        </table>
    </form>
</body>
</html>
"""

def generate_mashup(singer, count, duration):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': 'temp_%(autonumber)s.%(ext)s',
        'postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3','preferredquality': '192'}],
        'quiet': True
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([f"ytsearch{count}:{singer}"])

    merged = AudioSegment.empty()
    remove_files = []
    
    for file in os.listdir("."):
        if file.startswith("temp_") and file.endswith(".mp3"):
            audio = AudioSegment.from_mp3(file)
            merged += audio[:duration * 1000]
            remove_files.append(file)
            
    output_filename = "mashup_output.mp3"
    merged.export(output_filename, format="mp3")
    
    for f in remove_files:
        os.remove(f)
        
    return output_filename

def zip_file(filename):
    name = "mashup_output.zip"
    with zipfile.ZipFile(name, 'w') as f:
        f.write(filename)
    return name

def send_email(recipient_email, zip_filename):
    mssg = MIMEMultipart()
    mssg['From'] = sender_mail
    mssg['To'] = recipient_email
    mssg['Subject'] = "Mashup"

    with open(zip_filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
    
    encoders.encode_base64(part)
    part.add_header("Content-Disposition", f"attachment; filename= {zip_filename}")
    mssg.attach(part)

    print(f"Connecting to Gmail and sending to {recipient_email}...")
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(sender_mail, sender_pswd)
    server.send_message(mssg)
    server.quit()

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/mashup', methods=['POST'])
def mashup():
    try:
        singer = request.form['singer']
        count = int(request.form['count'])
        duration = int(request.form['duration'])
        email = request.form['email']

        mp3 = generate_mashup(singer, count, duration)
        
        zip_filename = zip_file(mp3)
        
        send_email(email, zip_filename)

        os.remove(mp3)
        os.remove(zip_filename)

        return f"<h3>Mashup sent to {email}</h3><a href='/'>Go Back</a>"
    except Exception as e:
        return f"<h3>Error: {str(e)}</h3><p>Ensure your App Password is correct and FFmpeg is installed.</p><a href='/'>Go Back</a>"

if __name__ == '__main__':
    app.run(debug=True)