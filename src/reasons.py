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

print('preprocessing...')

#preprocess()

print('done')

CATEGORIES = [2065,2066,2067,2068,2069]

PONDERATED = False

data=pd.read_csv("../Data/Preprocessed_Data_with_Label.csv", sep=',',encoding='latin1')

#creating file path
file_path = "reasons_to_leave_" + str(CATEGORIES)

colors = sns.color_palette()

if PONDERATED :
    
    file_path += "_percentage"
    
    ponderated_df=data.copy(deep=True)
    
    for i in range (101, 317):
        for column in data.columns:
            if ("{}".format(i) in column)and ("ANSWER" in column):
                new_column=data[column]*data["ANSCOUNT_{}".format(i)] #check the syntax
                ponderated_df[column]=new_column

    list_answers = ['DEMCODE', 'ANSCOUNT_164']
    for i in range(1,7):
        list_answers.append("ANSWER" + str(i)+"_164")
    
    #print(data.head())
    data_bis = ponderated_df[list_answers]
    data_bis = data_bis[data_bis['DEMCODE'].isin(CATEGORIES)]
    data_bis = data_bis[data_bis['ANSWER1_164']!=0]

    data_bis = data_bis.groupby('DEMCODE', as_index = False).mean()
    for i in range(1,7):
        data_bis["ANSWER" + str(i)+"_164"] /= data_bis['ANSCOUNT_164']

    #print(data_bis)
    data_bis = data_bis.drop(columns = ['ANSCOUNT_164'])
    #print(data_bis)

    data_bis.set_index('DEMCODE').plot(kind='bar', stacked=True, color=colors)

    # for i in range(1,7):
    #     sns.barplot(data=ponderated_df[ponderated_df['DEMCODE'].isin(CATEGORIES)], x='DEMCODE', 
    #         y='ANSWER' + str(i)+"_164", ci=None,label = "Answer" + str(i),estimator=sum, color=colors[i-1])

    plt.ylabel("% of total population") 
    

else :  
    
    file_path += "_count"
    list_answers = ['DEMCODE']
    for i in range(1,7):
        list_answers.append("ANSWER" + str(i)+"_164")
    
    #print(data.head())
    data_bis = data[list_answers]
    data_bis = data_bis[data_bis['DEMCODE'].isin(CATEGORIES)]
    data_bis = data_bis[data_bis['ANSWER1_164']!=0]

    #print(data_bis[data_bis['DEMCODE']==2067])
    data_bis = data_bis.groupby('DEMCODE', as_index = False).mean()    

    data_bis.set_index('DEMCODE').plot(kind='bar', stacked=True, color=colors)
    plt.ylabel("% of number of agencies")

plt.legend(ncol=2, loc="lower right", frameon=True)
plt.xlabel("Demographic properties")
plt.title("Reasons to leave its job according to the demographic properties")   
plt.savefig(file_path + ".png")

print("done")

