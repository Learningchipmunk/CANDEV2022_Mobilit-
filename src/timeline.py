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
CATEGORIES = list(range(2011, 2013+1))
PONDERATED = False

data=pd.read_csv("../Data/Preprocessed_Data_with_Label.csv", sep=',',encoding='latin1')

#want_leave = pd.concat([want_leave, data[data['DEMCODE'].isin(CATEGORIES)]])

#creating file path
file_path = "timeline_" + str(CATEGORIES) + "_" + str(PERCENTAGE)

if PONDERATED :
    pass

else :  
    #data['ANSWER1_163'] = data['ANSWER1_163']*data['ANSCOUNT_163']//100
    
    data_2018 = data[data['SURVEYR']==2018]
    data_2019 = data[data['SURVEYR']==2019]
    data_2020 = data[data['SURVEYR']==2020]

    file_path += "_count"

    for id in data['LEVEL1ID'].unique():
        count18 = data_2018[data_2018['LEVEL1ID']==id][data_2018['DEMCODE'].isin(CATEGORIES)]
        count19 = data_2019[data_2019['LEVEL1ID']==id][data_2019['DEMCODE'].isin(CATEGORIES)]
        count20 = data_2020[data_2020['LEVEL1ID']==id][data_2020['DEMCODE'].isin(CATEGORIES)]


        count18 = count18['ANSWER1_163'].sum() / (count18['ANSCOUNT_163'].sum())
        count19 = count19['ANSWER1_163'].sum() / (count19['ANSCOUNT_163'].sum())
        count20 = count20['ANSWER1_163'].sum() / (count20['ANSCOUNT_163'].sum())

        plt.plot([2018,2019,2020], [count18, count19, count20], label=id)
    
    #plt.bar(np.array(CATEGORIES)+0.2, b, width=0.4, color='g', align='center', label='All agencies') 
    plt.xticks([2018,2019,2020])#, labels=['Heterosexual', 'Gay/lesbian', 'Bisexual', 'Other', 'No answer'], rotation='horizontal')
    plt.ylabel("Proportion of people considering a move")

plt.xlabel("Survey year")
plt.title("Ratio of people considering leaving their position for each department")
plt.savefig(file_path + ".png", bbox_inches="tight")

print("done")