import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_style()

from helpers.data_preproc import preprocess
from helpers.trad_demcode import DEMCODE_TO_ENG

print('preprocessing...')

#preprocess()

print('done')

PERCENTAGE = 40
CATEGORIES = list(range(2063, 2064+1))
XLABEL = "Other visible minority group"
PONDERATED = False

data=pd.read_csv("../Data/Preprocessed_Data_with_Label.csv", sep=',',encoding='latin1')
         
want_leave = data[data['ANSWER1_163']>PERCENTAGE]
want_leave = want_leave[want_leave['DEMCODE'].isin(CATEGORIES)]

data = data[data['DEMCODE'].isin(CATEGORIES)]

#want_leave = pd.concat([want_leave, data[data['DEMCODE'].isin(CATEGORIES)]])

#creating file path
file_path = "desire_to_leave_" + str(CATEGORIES) + "_" + str(PERCENTAGE)

if PONDERATED :
    
    file_path += "_percentage"
                
    sns.catplot(data=want_leave[want_leave['DEMCODE'].isin(CATEGORIES)], x='DEMCODE', y='ANSCOUNT_163', hue = 'LEAVE', kind='bar', ci=None)
    
    plt.ylabel("total population") 

else :  
    
    file_path += "_count"

    a = [want_leave[want_leave['DEMCODE']==i].shape[0] for i in CATEGORIES]
    b = [data[data['DEMCODE']==i].shape[0] for i in CATEGORIES]

    a = np.array(a)/want_leave.shape[0]
    b = np.array(b)/data.shape[0]

    plt.bar(np.array(CATEGORIES)-0.2, a, width=0.4, color='b', align='center', label='Agencies with high mobility')
    plt.bar(np.array(CATEGORIES)+0.2, b, width=0.4, color='g', align='center', label='All agencies') 
    plt.xticks(CATEGORIES, labels=[DEMCODE_TO_ENG[i] for i in CATEGORIES], rotation='45', ha='right')
    plt.ylabel("Proportion of agencies with this population")

plt.xlabel(XLABEL)
plt.title("Will to leave their job according to the demographic properties")
plt.legend()
plt.savefig(file_path + ".png", bbox_inches="tight")

print("done")