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

TRAINING
The code runs for epochs=5000 with batch size=64.
Discriminator: Distinguishes between real and fake samples using Binary Cross Entropy loss.
Generator: Tries to create better fake data to fool the Discriminator. As training progresses, the Generator becomes highly skilled at mimicking the statistical properties of the original NO2 data.

VISUALIZATION
Sampling generates 10,000 samples from the trained Generator.
Plots a histogram for both the real and fake data.
