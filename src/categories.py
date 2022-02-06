import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

#Not finished..

sns.set_style()

#import os 
#dir_path = os.path.dirname(os.path.realpath(__file__))
#print(dir_path)
#print(os.dir())

from helpers.data_preproc import *

print('preprocessing...')

#preprocess()

print('done')

PERCENTAGE = 40
CATEGORIES = [2065,2066,2067,2068,2069]
PONDERATED = True

data=pd.read_csv("../Data/Preprocessed_Data_with_Label.csv", sep=',',encoding='latin1')
         
want_leave = data[data['ANSWER1_163']>PERCENTAGE]
want_leave = want_leave[want_leave['DEMCODE'].isin(CATEGORIES)]
want_leave['LEAVE'] = 'yes'
data['LEAVE'] = 'no'

want_leave = pd.concat([want_leave, data[data['DEMCODE'].isin(CATEGORIES)]])

#creating file path
file_path = "desire_to_leave_" + str(CATEGORIES) + "_" + str(PERCENTAGE)



if PONDERATED :
    
    file_path += "_percentage"
                
    sns.catplot(data=want_leave[want_leave['DEMCODE'].isin(CATEGORIES)], x='DEMCODE', y='ANSCOUNT_163', hue = 'LEAVE', kind='bar', ci=None)
    
    plt.ylabel("total population") 

else :  
    
    file_path += "_count"
      
    sns.catplot(data=want_leave[want_leave['DEMCODE'].isin(CATEGORIES)], x='DEMCODE', hue = 'LEAVE', kind='count') 
    plt.ylabel("number of agencies")

plt.xlabel("Demographic properties")
plt.title("Desire to leave its job according to the demographic properties")   
plt.legend(title = 'More than ' + str(PERCENTAGE )+ '% want to leave')
plt.savefig(file_path + ".png")

print("done")