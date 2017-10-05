# -*- coding: utf-8 -*-
import pandas as pd
import os
import pyLDAvis
import pyLDAvis.sklearn

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def fast_tweet(file):
	#df_Fristtweet = pd.read_csv('/Users/margaretnym/Desktop/Galvanize Data Science/Capstone/LastOne.csv')
	df_Fristtweet = pd.read_csv(file)
	text_frist1 = df_Fristtweet[(df_Fristtweet['screen_name'].isin(people_churned_lst.tolist())) & (df_Fristtweet['lang']=='en')]['text']


	tf_vectorizer_first1 = CountVectorizer(strip_accents = 'unicode',
	                                stop_words = 'english',
	                                lowercase = True,
	                                token_pattern = r'\b[a-zA-Z]{3,}\b',
	                                max_df = 0.5,
	                                min_df = 10)

	dtm_tf_first1 = tf_vectorizer_first1.fit_transform(text_frist1.str.decode("utf-8", "replace"))

	lda_tf_first1 = LatentDirichletAllocation(n_topics=8, random_state=0)
	lda_tf_first1.fit(dtm_tf_first1 )

	pyLDAvis.sklearn.prepare(lda_tf_first1, dtm_tf_first1, tf_vectorizer_first1)
	PreparedData = pyLDAvis.sklearn.prepare(lda_tf_first1, dtm_tf_first1, tf_vectorizer_first1)
	pyLDAvis.save_html(PreparedData, 'firstfirstfirstfirst_counter.html')


def last_tweet(file):

	#df_alltweets  = pd.read_csv('/Users/margaretnym/Desktop/Galvanize Data Science/Capstone/Data/combine_tweets/ulta_combine_tweets/
	df_alltweets = pd.read_csv(file)

	UltraUltraTweets/New Folder With Items/New Folder With Items/combo.csv', error_bad_lines=False )
	lasttweet = df_alltweets[df_alltweets['count_for_each_user'] == 1]
	lasttweet_dropped = lasttweet.drop_duplicates()


	text_last1 = lasttweet_dropped[(lasttweet_dropped['screen_name'].isin(people_churned_lst.tolist())) & (lasttweet_dropped['lang']=='en')]['text']

	tfidf_vectorizer_last = TfidfVectorizer(strip_accents = 'unicode',
	                                stop_words = step_stop_words_last,
	                                lowercase = True,
	                                token_pattern = r'\b[a-zA-Z]{3,}\b',
	                                max_df = 0.5,
	                                min_df = 10)


	dtm_tfidf_last = tfidf_vectorizer_last.fit_transform(text_last1.str.decode("utf-8", "replace"))

	lda_tfidf_last = LatentDirichletAllocation(n_topics=8, random_state=0)
	lda_tfidf_last.fit(dtm_tfidf_last)

	pyLDAvis.sklearn.prepare(lda_tfidf_last, dtm_tfidf_last, tfidf_vectorizer_last)
	PreparedData = pyLDAvis.sklearn.prepare(lda_tfidf_last, dtm_tfidf_last, tfidf_vectorizer_last)
	pyLDAvis.save_html(PreparedData, 'self_lastlastlast_count.html')

if __name__ == "__main__":
	df_delta_churn = pd.read_csv('/Users/margaretnym/Desktop/Galvanize Data Science/Capstone/df_delta.csv')
	people_churned = df_delta_churn[df_delta_churn['churn_mean'] == 'yes']['screen_name']
	people_churned_lst = people_churned.unique()
	fast_tweet(file)
	last_tweet(file)
