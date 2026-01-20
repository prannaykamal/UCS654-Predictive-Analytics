# UCS654

# Sampling
Taking number of samples, n= (z^2*p*(1-p))/e^2=384 
where z=1.96, p=0.5, e=0.05

5 sampling techniques used are Simple Random Sampling, Systematic Sampling, Stratified Sampling, Cluster Sampling, Bootstrap Sampling; 
5 models used are Logistic Regression, Decision Tree, Random Forest, SVM Classifier, KNN

For each sampling method, each model is selected, StandardScaler() is used to normalize the data before calculating and storing accuracy.
For each sampling method, mean accuracy is calculated by taking average of all 5 model accuracies.
The sampling method getting the highest mean accuracy is considered best. Best technique results may change when different samples are choosen.

