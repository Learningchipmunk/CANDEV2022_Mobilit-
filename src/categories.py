import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_style()

#import os 
#dir_path = os.path.dirname(os.path.realpath(__file__))
#print(dir_path)
#print(os.dir())

from helpers.data_preproc import *

preprocess()

PERCENTAGE = 40
CATEGORIES = [2065,2066,2067,2068,2069]
PONDERATED = True

data=pd.read_csv("..\Data\Preprocessed_Data_with_Label.csv", sep=',',encoding='utf8')
         
want_leave = data[data['ANSWER1_163']>PERCENTAGE]

#creating file path
file_path = "desire_to_leave_" + str(CATEGORIES) + "_" + PERCENTAGE

if PONDERATED :
    
    file_path += "_percentage"
    
    ponderated_df=data.copy(deep=True)
    
    for i in range (101, 317):
        for column in data.columns:
            if ("{}".format(i) in column)and ("ANSWER" in column):
                new_column=data[column]*data["ANSCOUNT_{}".format(i)] #check the syntax
                ponderated_df[column]=new_column
                
    sns.catplot(data=ponderated_df[ponderated_df['DEMCODE'] in CATEGORIES], x='DEMCODE', kind='count')
    plt.savefig('graph.png')
    plt.savefig(file_path + ".png")

else :  
    
    file_path += "_count"
      
    sns.catplot(data=data[data['DEMCODE'] in CATEGORIES], x='DEMCODE', kind='count') 
    plt.savefig(file_path + ".png")

print("done")