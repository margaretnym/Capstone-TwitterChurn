
import pandas as pd
import numpy as np

def get_userid(): 
    df = pd.read_csv('final_list_bio.csv')
    userid_list = list(df['userid'])
    
    return userid_list

if __name__ == "__main__":
    get_userid()
    