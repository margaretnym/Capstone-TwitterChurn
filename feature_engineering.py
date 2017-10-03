import pandas as pd
import numpy as np

from numpy import sort

import cPickle as pickle

import sklearn
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.feature_selection import SelectFromModel
from sklearn.grid_search import GridSearchCV
from sklearn.model_selection import cross_val_score
from sklearn.metrics import roc_curve, auc, accuracy_score, recall_score, f1_score, precision_score


from imblearn.combine import SMOTEENN 
from collections import Counter

import matplotlib.pyplot as plt
# %matplotlib inline 
import matplotlib
matplotlib.style.use('ggplot')

def feature_engineering():
    
    df_features = pd.read_csv('/Users/margaretnym/Desktop/Galvanize Data Science/Capstone/feature_engineering/data/combo_features.csv')
    df_delta_churn = pd.read_csv('/Users/margaretnym/Desktop/Galvanize Data Science/Capstone/df_delta.csv')
    df = pd.merge(left=df_features,right=df_delta_churn, left_on='screen_name', right_on='screen_name')

    df.fillna(0, inplace=True)
    df= pd.get_dummies(df, columns=['source'])
    df['verified'] = df.verified.apply(lambda x: 0 if x =="False" else 1)
    df['profile'] = df.profile.apply(lambda x: 0 if x =="False" else 1)
    df['churn_mean'] = df.churn_mean.apply(lambda x: 0 if x =="no" else 1)


    X_col = df[[u'created_date_til_today', u'status_lifespan',
       u'fav_lifespan', u'friends_count', u'ollowers_count',
       u'ratio', u'avg_len', u'retweet_ratio', u'org_fav',
       u'org_retweet', u'org_hastages', u'org_mentions', u'org_url',
       u'org_media_type']]
    y_col = df['churn_mean']

    X = np.array(X_col)
    y = np.array(y_col)

    return X,y


def parameter_tuning(X_train,y_train):   
    param_grid = {'n_estimators':[10, 100, 1000],
                  'max_depth': [4, 6], 
                  'max_features': ['auto', 'sqrt', 'log2']}

    
    gb_model = GradientBoostingClassifier()
    gb_cv = GridSearchCV(gb_model, param_grid, n_jobs=-1,verbose=True, cv=2).fit(X_train,y_train)  
    
    rf_model = RandomForestClassifier()
    rf_cv = GridSearchCV(rf_model, param_grid, n_jobs=-1,verbose=True, cv=2).fit(X_train,y_train)  
    
    Cs = np.logspace(-4, 4, 3)
    param_grid2 = {'penalty':['l1', 'l2'], 'C':Cs}
    
    log_model = LogisticRegression()
    log_cv = GridSearchCV(log_model, param_grid2, n_jobs=-1,verbose=True, cv=2).fit(X_train,y_train)  
               
               
    if (gb_cv.best_score_ > rf_cv.best_score_) and (gb_cv.best_score_ > log_cv.best_score_) :
        best_model = gb_cv.best_estimator_
    elif (rf_cv.best_estimator_ > gb_cv.best_score_) and (rf_cv.best_estimator_ > log_cv.best_score_):
        best_model = rf_cv.best_estimator_
    else:
        best_model = log_cv.best_estimator_
        
    print str(gb_cv.best_estimator_), str(gb_cv.best_score_)
    print str(rf_cv.best_estimator_), str(rf_cv.best_score_)
    print str(log_cv.best_estimator_), str(log_cv.best_score_)
    
    score = np.mean(cross_val_score(best_model, X_train, y_train ,cv=2))
    print 'training score: {}' .format(score)
    recall = np.mean(cross_val_score(best_model, X_train, y_train,cv=2, scoring='recall'))
    print 'training recall: {}' .format(recall)
    precision = np.mean(cross_val_score(best_model, X_train, y_train,cv=2, scoring='precision'))
    print 'training precision: {}' .format(recall)
    f1_score = np.mean(cross_val_score(best_model, X_train, y_train,cv=2, verbose=True, scoring="f1"))
    print 'training F1-score: {}' .format(f1_score)
    
    
    return best_model


def balance_class(X,y):
    sm = SMOTEENN()
    X_resampled, y_resampled = sm.fit_sample(X, y)
    print('Original dataset shape {}'.format(Counter(y)))
    print('Resampled dataset shape {}'.format(Counter(y_resampled)))
    return X_resampled, y_resampled

def plot_ROC_curve(fpr, tpr) :
    # Compute ROC curve and ROC area for each class
    roc_auc = auc(fpr, tpr)

    plt.figure(figsize=(5,5))
    lw = 2
    plt.plot(fpr, tpr, color='darkorange',
         lw=lw, label='ROC curve (area = %0.2f)' % roc_auc)
    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('Receiver operating characteristic example')
    plt.legend(loc="lower right")
    plt.savefig('ROC.svg', format='svg', dpi=400)
    plt.show()

def check_feature_importance(model, X_train, X_test, y_train, y_test):
    y_pred = model.predict(X_test)
    predictions = [round(value) for value in y_pred]
    accuracy = accuracy_score(y_test, predictions)
    print("Accuracy: %.2f%%" % (accuracy * 100.0))
    # Fit model using each importance as a threshold
    
    feature_names = [u'created_date_til_today', u'status_lifespan', \
                 u'fav_lifespan',  u'friends_count', u'ollowers_count',\
                 u'ratio', u'avg_len', u'retweet_ratio', u'org_fav',\
                 u'org_retweet', u'org_hastages', u'org_mentions', u'org_url',\
                 u'org_media_type']

    dict_feature = {x:y for x,y in zip(feature_names, best_model.feature_importances_)}
    
    thresholds = sort(best_model.feature_importances_)


    for thresh in thresholds:
        # select features using threshold
        selection = SelectFromModel(best_model, threshold=thresh, prefit=True)
        select_X_train = selection.transform(X_train)
        # train model
        selection_model = GradientBoostingClassifier()
        selection_model.fit(select_X_train, y_train)
        # eval model
        select_X_test = selection.transform(X_test)
        y_pred = selection_model.predict(select_X_test)
        predictions = [round(value) for value in y_pred]
        accuracy = accuracy_score(y_test, predictions)

        for f_name, f_val in dict_feature.iteritems():
            if f_val == thresh:
                name = f_name     
                print "Thresh=%.3f, n=%d, name = %s, Accuracy: %.2f%%" % (thresh, select_X_train.shape[1], name, accuracy*100.0)
                print "******"

def score_best_models(X,y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.3)
    best_model = parameter_tuning(X_train,y_train)    
    
    #Evaluate the model
    #print 'Best score:', best_model.score(X_test, y_test)  #accuracy
    print 'Test-set Accuracy:', accuracy_score(y_test,best_model.predict(X_test))
    print 'Test-set Recall:', recall_score(y_test,best_model.predict(X_test))
    print 'Test-set Precision:', precision_score(y_test,best_model.predict(X_test))
    print 'Test-set F-1 Score:', f1_score(y_test,best_model.predict(X_test))

    y_score = best_model.predict_proba(X_test)

    fpr,tpr, threshold = roc_curve(y_test,y_score[:,1])
    plot_ROC_curve(fpr, tpr)

    return best_model, X_train, X_test, y_train, y_test

def plot_feature_importance(model):
    feature_importance = best_model.feature_importances_
    # make importances relative to max importance
    feature_importance = 100.0 * (feature_importance / feature_importance.max())
    sorted_idx = np.argsort(feature_importance)
    pos = np.arange(sorted_idx.shape[0]) + .5
    plt.subplot(1, 2, 2)
    plt.barh(pos, feature_importance[sorted_idx], align='center')
    plt.yticks(pos, np.array(feature_names)[sorted_idx])
    plt.xlabel('Relative Importance')
    plt.title('Variable Importance')

    plt.savefig('featureimportance.svg', format='svg', dpi=400)
    plt.show()

if __main__ == "__name__":
    X,y = feature_engineering()
    resampled_X, resampled_y = balance_class(X,y)
    best_model, X_train, X_test, y_train, y_test = score_best_models(resampled_X,resampled_y)
    check_feature_importance(best_model, X_train, X_test, y_train, y_test)
    plot_feature_importance(best_model)
    with open('model.pkl', 'wb') as f:
        pickle.dump(best_model, f)