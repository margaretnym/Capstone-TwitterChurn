import numpy as np
import pandas as pd


import matplotlib.pyplot as plt
# %matplotlib inline 
import matplotlib
matplotlib.style.use('ggplot')

import seaborn

def conditional_cols():

	df_allpeople = pd.read_csv('/Users/margaretnym/Desktop/Galvanize Data Science/Capstone/Data/combine_users/ulta_combine_users/all_user_list.csv')

	conditions = [
	    (df_allpeople['statuses_count'] == 0),
	    (df_allpeople['statuses_count'] < 5),
	    (df_allpeople['statuses_count'] >= 5) & (df_allpeople['statuses_count'] < 50),
	    (df_allpeople['statuses_count'] >= 50) & (df_allpeople['statuses_count'] < 500)]
	choices = ["Never Tweet", "n < 5", "5 <= n < 50", "50 <= n < 500"]
	df_allpeople['group']  = np.select(conditions, choices, default="n => 500")

def boxplot_friends():
	# Boxplot for friends
	df_allpeople['log_friends'] = np.log(df_allpeople['friends']+1)
	df_allpeople.sort_values(["group"], inplace=True)
	seaborn.boxplot(x="group", y='log_friends', data=df_allpeople, order=["Never Tweet", "n < 5", "5 <= n < 50", "50 <= n < 500", "n => 500"], \
	               palette="Set2").set_title("Boxplot for friends in different tweet activity groups")
	plt.savefig('boxplot_friends.svg', format='svg', dpi=400)
	plt.show()

def boxplot_friends():
	# Boxplot for followers
	df_allpeople['log_followers'] = np.log(df_allpeople['followers']+1)
	df_allpeople.sort_values(["group"], inplace=True)
	seaborn.boxplot(x="group", y='log_followers', data=df_allpeople, order=["Never Tweet", "n < 5", "5 <= n < 50", "50 <= n < 500", "n => 500"], palette="Set2").set_title("Boxplot for followers in different tweet activity groups")
	plt.savefig('boxplot_followers.svg', format='svg', dpi=400)
	plt.show()

if __name__ == "__main__":
	conditional_cols()
	boxplot_friends()
	boxplot_friends()
