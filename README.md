# Capstone-TwitterChurn


## Propose

### Main Infrastructure
- MongoDB
- Flask
- AWS - EC2

### Library Used
- Numpy
- Pandas
- Sklearn
- Jinja
- cPickle
- pymongo
- flask
- SMOTE The raw dataset is imbalanced. Hence, the SMOTE algorithm is used to balance the datasets.
http://contrib.scikit-learn.org/imbalanced-learn 


### Diagram of work flow 
![App Architecture](https://github.com/margaretnym/event-fraud-detection/blob/master/images/fraud_detection.png)

## Data Collection
## Data Size
## Sample Accounts Category
## Power Curves
## Way to define churn
## Feature engineering

#### Feature Picked up & its importance
Category | Feature |Description | Feature Importance
------------ | ------------- | -------------| -------------
body_length|                  |0.38
have_previous_payouts||0.21
payout_type_|NAN for payout_type|0.08
maindomain_email|If the email domain from 'hotmail.com', 'gmail.com', or 'yahoo.com'|0.06
Facebook_presence|            |0.05
show_map|                     |0.05
US/N|If the country is US or not|0.04
Twitter_presence|             |0.04
sensible_age|User age is within the range 15-80                 |0.03
payout_type_CHECK|Check for payout_type             |0.02
cap_name|If name is all in captial case                     |0.02
payout_type_ACH|ACH for payout_type              |0.02

## Model picked
Models experiemented: Logistic Regression, Decision Trees, Gradient Boosting. 
All models are trained using 10-foldcross validation.

The final supervised classification model used is the Gradient Boosting Classifier.
```python
GradientBoostingClassifier(criterion='friedman_mse', init=None,
               learning_rate=0.1, loss='deviance', max_depth=4,
               max_features='log2', max_leaf_nodes=None,
               min_impurity_split=1e-07, min_samples_leaf=1,
               min_samples_split=2, min_weight_fraction_leaf=0.0,
               n_estimators=100, presort='auto', random_state=None,
               subsample=1.0, verbose=0, warm_start=False)
```
## Topic Modeling - Visualizations¶
