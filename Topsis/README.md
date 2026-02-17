# Part-1
The Technique for Order of Preference by Similarity to Ideal Solution (TOPSIS), a multi-criteria decision-making approach, is the main component of this project.
The algorithm applies user-defined weights after first normalizing the input data to a comparable scale in accordance with a strict mathematical procedure.
The "Best" and "Worst" optimal solutions are then determined by whether a criterion is for minimization (-) or maximization (+).
In order to determine the final ranking, it computes a performance score Pi = Sworst / (Sbest + Sworst), by calculating the Euclidean distance of each alternative from these ideals.

# Part-2
This step involves using Twine to upload the TOPSIS logic to PyPI after it has been transformed into a distributable Python package.
With just one command - topsis <InputDataFile> <Weights> <Impacts> <OutputResultFileName>
users can perform the analysis by user-friendly Command Line Interface (CLI).
To ensure that the input file exists, has at least three columns, and that the number of weights and impacts equals the number of criteria columns, the script incorporates strong error handling.

# Part-3
In order to make the TOPSIS tool browser-accessible, the last section creates a Web Service using the Flask framework.
Users can upload their CSV data and enter the required parameters (weights, impacts, and email ID) in a form on the web interface.
The backend processes the data, creates a result.csv file with scores and ranks, and automatically sends this file as an email attachment to the user via SMTP rather than showing the results directly on the screen.
