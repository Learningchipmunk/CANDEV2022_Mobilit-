#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import copy

import seaborn as sns
sns.set_style()

DATA_PATH = '../Data/'

def preprocess():
 
    data_origin = pd.read_csv(DATA_PATH+"subset-3-sous-ensemble-3.csv", encoding='latin1')
    
    data = data_origin.copy()
    
    try: data.drop(columns=['LEVEL2ID', 'LEVEL3ID', 'LEVEL4ID', 'LEVEL5ID'], inplace=True)
    except: pass
    
    useless = ['BYCOND', 'DESCRIP_E', 'DESCRIP_F', 'TITLE_E', 'TITLE_F', 'SUBINDICATORENG', 'SUBINDICATORFRA', 'DEPT_E', 'DEPT_F', 'INDICATORENG', 'INDICATORFRA', 'SCORE100']
    try: data.drop(columns=useless, inplace=True)
    except: pass
    
    # drop empty lines
    data.drop(data[data['ANSWER1'] == ' '].index, inplace=True)
    
    # change strings to numbers
    traduction_question = {ques: i+101 for i, ques in enumerate(data['QUESTION'].unique())}
    data['QUESTION'] = data['QUESTION'].map(lambda x: traduction_question[x])
    
    data = data.astype({'SCORE5': 'float'}, copy=False)
    data = data.astype({col: 'int' for col in ['ANSWER1', 'ANSWER2', 'ANSWER3', 'ANSWER4', 'ANSWER5', 'ANSWER6', 'ANSWER7',
        'MOST_POSITIVE_OR_LEAST_NEGATIVE', 'NEUTRAL_OR_MIDDLE_CATEGORY', 'MOST_NEGATIVE_OR_LEAST_POSITIVE', 'AGREE',
        'ANSCOUNT']}, copy=False)
    
    # add unique ids to each participant
    data['ID'] = data['LEVEL1ID']*1000 + (data['SURVEYR']-2018)*100 + data['DEMCODE']-2011
    
    #for col in data.columns:
        #print(col, '\t', len(data[col].unique()), '\t', type(data[col][0]), '\t', data[col][0])
    
    data_questions = data.drop(columns = ['SURVEYR', 'DEMCODE', 'LEVEL1ID'])
    list_id = data_questions['ID'].unique()
    set_id = set(list_id)
    data_agg = pd.DataFrame({'ID' : list_id})
    
    for i in range(101, 317):
        new_question = data_questions[data_questions['QUESTION']==i].drop(columns = ['QUESTION'])
        missing_id = list(set_id-set(new_question['ID']))
            
        new_df = pd.DataFrame({name: ([0]*len(missing_id) if index<len(new_question.columns)-1 else missing_id) for index, name in enumerate(new_question.columns)})
        new_question = new_question.append(new_df, ignore_index = True)
                
        new_question.rename(columns=lambda x: x + "_" + str(i) if x!='ID' else x, inplace=True)
        data_agg = pd.merge(data_agg, new_question, on = 'ID')
    
    data_agg['LEVEL1ID'] = data_agg['ID'] // 1000
    data_agg['SURVEYR'] = (data_agg['ID'] // 100) % 10 + 2018
    data_agg['DEMCODE'] = data_agg['ID'] % 100 + 2011
    
    data_agg.to_csv(DATA_PATH+'Preprocessed_Data.csv', index=False)
    
    
    data_with_label = data_agg[(data_agg['ANSWER1_163'] != 9999) & ((data_agg['ANSWER1_163'] != 0) & (data_agg['ANSWER2_163'] != 0))]
    
    supp_columns = []
    for i in range(101, 317):
        supp_columns.extend(['MOST_POSITIVE_OR_LEAST_NEGATIVE_'+str(i),'NEUTRAL_OR_MIDDLE_CATEGORY_'+str(i),'MOST_NEGATIVE_OR_LEAST_POSITIVE_'+str(i), 'AGREE_'+str(i),'SCORE5_'+str(i)])
        
    data_with_label = data_with_label.drop(columns = supp_columns)
    
    supp_columns = []
    
    for col in data_with_label.columns:
        uni = data_with_label[col].unique()
        if len(uni) == 2 and 9999 in uni and 0 in uni:
            supp_columns.append(col)
    
    data_with_label = data_with_label.drop(columns = supp_columns)
    
    data_with_label.to_csv(DATA_PATH+'Preprocessed_Data_with_Label.csv', index=False)
    
