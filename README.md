![App Architecture](https://github.com/margaretnym/Capstone-TwitterChurn/blob/master/ppt/1Margaret%20-%20Capstone2nd.png)
## Propose
Understanding what keeps social media users engaged is a foundation to develop retention strategies to keep users from walking out the door. This capstone project defines Twitter users who have churned, their important features, and what they said in their last tweets.

### Diagram of work flow 

### Main Infrastructure
- MongoDB
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

### Data Collection and Data Charactistics
![App Architecture](https://github.com/margaretnym/Capstone-TwitterChurn/blob/master/ppt/2Margaret%20-%20Capstone2nd.png)

### Define Churn
![App Architecture](https://github.com/margaretnym/Capstone-TwitterChurn/blob/master/ppt/3Margaret%20-%20Capstone.png)

### Feature Engineering
![App Architecture](https://github.com/margaretnym/Capstone-TwitterChurn/blob/master/ppt/Screen%20Shot%202017-10-04%20at%204.12.10%20PM.png)

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

![App Architecture](https://github.com/margaretnym/Capstone-TwitterChurn/blob/master/ppt/5Margaret%20-%20Capstone.png)

#### Links to the data vis
https://s3-us-west-2.amazonaws.com/margaretgalvanize/self_firstfirstfirstfirst_tfidf.html
https://s3-us-west-2.amazonaws.com/margaretgalvanize/self_lastlastlast_count.html


## Visualizing topic models with pyLDAvis
![App Architecture](https://github.com/margaretnym/Capstone-TwitterChurn/blob/master/ppt/6Margaret%20-%20Capstone.png)

![App Architecture](https://github.com/margaretnym/Capstone-TwitterChurn/blob/master/ppt/6.5Margaret%20-%20Capstone.png)

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



Analyzing our LDA model

The interactive visualization pyLDAvis produces is helpful for both:

    Better understanding and interpreting individual topics, and
    Better understanding the relationships between the topics.

For (1), you can manually select each topic to view its top most freqeuent and/or "relevant" terms, using different values of the $\lambda$ parameter. This can help when you're trying to assign a human interpretable name or "meaning" to each topic.

For (2), exploring the Intertopic Distance Plot can help you learn about how topics relate to each other, including potential higher-level structure between groups of topics.

In our plot, there is a stark divide along the x-axis, with two topics far to the left and most of the remaining 48 far to the right. Inspecting the two outlier topics provides a plausible explanation: both topics contain many non-English words, while most of the rest of the topics are in English. So, one of the main attributes that distinguish the reviews in the dataset from one another is their language.

This finding isn't entirely a surprise. In addition to English-speaking cities, the Yelp dataset includes reviews of businesses in Montreal and Karlsruhe, Germany, often written in French and German, respectively. Multiple languages isn't a problem for our demo, but for a real NLP application, you might need to ensure that the text you're processing is written in English (or is at least tagged for language) before passing it along to some downstream processing. If that were the case, the divide along the x-axis in the topic plot would immediately alert you to a potential data quality issue.

The y-axis separates two large groups of topics — let's call them "super-topics" — one in the upper-right quadrant and the other in the lower-right quadrant. These super-topics correlate reasonably well with the pattern we'd noticed while naming the topics:

    The super-topic in the lower-right tends to be about food. It groups together the burger & fries, breakfast, sushi, barbecue, and greek topics, among others.
    The super-topic in the upper-right tends to be about other elements of the restaurant experience. It groups together the ambience & seating, location & time, family, and customer service topics, among others.

So, in addition to the 50 direct topics the model has learned, our analysis suggests a higher-level pattern in the data. Restaurant reviewers in the Yelp dataset talk about two main things in their reviews, in general: (1) the food, and (2) their overall restaurant experience. For this dataset, this is a very intuitive result, and we probably didn't need a sophisticated modeling technique to tell it to us. When working with datasets from other domains, though, such high-level patterns may be much less obvious from the outset — and that's where topic modeling can help.



![App Architecture](https://github.com/margaretnym/Capstone-TwitterChurn/blob/master/ppt/8Margaret%20-%20Capstone.png)


