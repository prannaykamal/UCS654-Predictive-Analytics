# UCS654

# Sampling
Taking number of samples, n= (z^2*p*(1-p))/e^2=384 
where z=1.96, p=0.5, e=0.05

5 sampling techniques used are Simple Random Sampling, Systematic Sampling, Stratified Sampling, Cluster Sampling, Bootstrap Sampling;  
5 models used are Logistic Regression, Decision Tree, Random Forest, SVM Classifier, KNN

For each sampling method, each model is selected, StandardScaler() is used to normalize the data before calculating and storing accuracy.
For each sampling method, mean accuracy is calculated by taking average of all 5 model accuracies.
The sampling method getting the highest mean accuracy is considered best. Best technique results may change when different samples are choosen.

# Probability Density Functions
For r=102317125, ar=0.05 and br=0.3
Transformation is done using z=x+ar*sin(br*x), where x is NO2 column of India Air Quality dataset.

On comparing given probability function with Gaussian probability density function:
1. The area under the curve over all values of z must be one. Therefore, c=root(lambda/pi)
2. mean is calculated as summation of all z divided by number of samples.
3. Using MLE for: p(z)=root(lambda/pi)*e^(-lambda*(z-mean)^2), the MLE solution is lambda=n/(2*sum((z-mean)^2))
   
lambda=0.0014603894854064846, mean=25.80791010190818, c=0.021560529002873346

TRAINING:
The code runs for epochs=5000 with batch size=64.
Discriminator: Distinguishes between real and fake samples using Binary Cross Entropy loss.
Generator: Tries to create better fake data to fool the Discriminator. As training progresses, the Generator becomes highly skilled at mimicking the statistical properties of the original NO2 data.

VISUALIZATION:
Sampling generates 10,000 samples from the trained Generator.
Plots a histogram for both the real and fake data.

# Mashup

Program 1: Mashup Tool
This program is designed as a command-line utility that automates the creation of an audio mashup based on specific user arguments. When the script runs, it first reads inputs provided directly in the terminal, including the name of a singer, number of videos, the duration for each clip, and the name for the output file. The program validates these inputs to ensure the user has requested a minimum number of videos (10) and a sufficient duration (20 seconds). If the criteria are not met, the error message is displayed to the user.
Once the inputs are verified, the program searches a video platform for content matching the singer's name and downloads audio tracks from the specified number of videos. It then processes each downloaded file by trimming it down to the exact duration requested by the user. Finally, these individual short clips are stitched together into one continuous audio track which is saved locally as a new file, and the temporary downloaded files are automatically deleted to keep the computer's storage clean.

Program 2: Web-Based Mashup Service
This program functions as a web application, providing a interface for users to generate mashups without using the command line. It launches a local web server that displays an HTML form, prompting the user to enter the artist's name, number of videos, clip duration, and email address. When the user submits the form, the application receives the data and triggers the background processing logic to handle the media generation task.
In the backend, the logic identifies and downloads the relevant audio tracks, trims them to the specified length and merges them into a single file. The program compresses the final audio into a zip archive and connects to an email server. It then sends the zipped mashup directly to the email address provided by the user as an attachment, ensuring that all temporary files are removed from the server once the delivery is complete. This email is sent via "prannaykamal9@gmail.com". The password mentioned in the code is revoked.
