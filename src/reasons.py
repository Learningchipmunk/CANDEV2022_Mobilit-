import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_style()

from helpers.data_preproc import preprocess
from helpers.trad_demcode import DEMCODE_TO_ENG

print('preprocessing...')

# preprocess()

print('done')

CATEGORIES = list(range(2063, 2064+1))
XLABEL = "Other visible minority group"
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

    plt.ylabel("Average population for the agencies") 
    

else :  
    
    file_path += "_count"
    list_answers = ['DEMCODE']
    for i in range(1,7):
        list_answers.append("ANSWER%d_164"%i)
    
    data_bis = data[list_answers].copy()

    data_bis.rename(columns={'ANSWER%d_164'%(i+1):j for i, j in enumerate([
        'To retire',
        'To pursue another position within my department or agency',
        'To pursue a position in another department or agency',
        'To pursue a position outside the federal public service',
        'End of my term, casual or student employment',
        'Other'])}, inplace=True)
    data_bis = data_bis[data_bis['DEMCODE'].isin(CATEGORIES)]
    data_bis = data_bis[data_bis['To retire']!=0]

    data_bis = data_bis.groupby('DEMCODE', as_index = False).mean()    

    ax = data_bis.set_index('DEMCODE').plot(kind='bar', stacked=True, color=colors)
    ax.set_xticklabels([DEMCODE_TO_ENG[i] for i in CATEGORIES], rotation='horizontal')
    plt.ylabel("Average percentage for the agencies")

plt.xticks(rotation = 45, ha='right')
plt.legend(ncol=1, bbox_to_anchor=(1, -0.1))
plt.xlabel(XLABEL)
plt.title("Reasons to consider leaving their job according to the demographic properties")
plt.savefig(file_path + ".png", bbox_inches="tight")

print("done")

