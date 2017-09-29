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
All models are trained using 10-fold cross validation.

The final supervised classification model used is the Gradient Boosting Classifier.
```python
GradientBoostingClassifier(criterion='friedman_mse', init=None,
              learning_rate=0.1, loss='deviance', max_depth=6,
              max_features='auto', max_leaf_nodes=None,
              min_impurity_decrease=0.0, min_impurity_split=None,
              min_samples_leaf=1, min_samples_split=2,
              min_weight_fraction_leaf=0.0, n_estimators=1000,
              presort='auto', random_state=None, subsample=1.0, verbose=0,
              warm_start=False)

```
## Visualizing topic models with pyLDAvis


Wait, what am I looking at again?

There are a lot of moving parts in the visualization. Here's a brief summary:

On the left, there is a plot of the "distance" between all of the topics (labeled as the Intertopic Distance Map)
- The plot is rendered in two dimensions according a multidimensional scaling (MDS) algorithm. Topics that are generally similar should be appear close together on the plot, while dissimilar topics should appear far apart.
- The relative size of a topic's circle in the plot corresponds to the relative frequency of the topic in the corpus.
- An individual topic may be selected for closer scrutiny by clicking on its circle, or entering its number in the "selected topic" box in the upper-left.

On the right, there is a bar chart showing top terms.
- When no topic is selected in the plot on the left, the bar chart shows the top-30 most "salient" terms in the corpus. A term's saliency is a measure of both how frequent the term is in the corpus and how "distinctive" it is in distinguishing between different topics.
- When a particular topic is selected, the bar chart changes to show the top-30 most "relevant" terms for the selected topic. The relevance metric is controlled by the parameter $\lambda$, which can be adjusted with a slider above the bar chart.
- Setting the $\lambda$ parameter close to 1.0 (the default) will rank the terms solely according to their probability within the topic.
- Setting $\lambda$ close to 0.0 will rank the terms solely according to their "distinctiveness" or "exclusivity" within the topic — i.e., terms that occur only in this topic, and do not occur in other topics.
- Setting $\lambda$ to values between 0.0 and 1.0 will result in an intermediate ranking, weighting term probability and exclusivity accordingly.
- Rolling the mouse over a term in the bar chart on the right will cause the topic circles to resize in the plot on the left, to show the strength of the relationship between the topics and the selected term.
