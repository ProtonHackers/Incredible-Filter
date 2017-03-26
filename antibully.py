# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 21:34:15 2017

@author: rohankoodli
"""

from sklearn.svm import SVC
from watson_developer_cloud import ToneAnalyzerV3, NaturalLanguageClassifierV1
import json, os, pickle

tone_analyzer = ToneAnalyzerV3(
   username='26db2c5b-2eda-46d0-9c66-438d943713d8',
   password='O3UAXtApBXOQ',
   version='2016-05-19')

words = ['suck','hate','terribe','worst',
         'bad','ugly',
         'nice','thanks','kind','safe','appreciate','yay','beautiful']

#print json.dumps(tone_analyzer.tone(text='yayyyy'),indent=2)

def iterate_tone_analysis(jsonfile):
    return tone_analyzer.tone(text=jsonfile)
    
def get_features(json_text):
    main_json = []
    for val in json_text['document_tone']['tone_categories']:
        for i in val['tones']:
            main_json.append(i['score'])
    return main_json

word_analysis = []
for i in words:
    tone = iterate_tone_analysis(i)
    features = get_features(tone)
    word_analysis.append(features)


good_labels = [1]*7
bad_labels = [0]*6

labels = bad_labels + good_labels

svc = SVC()
svc.fit(word_analysis,labels)
pickle.dump(svc,open(os.getcwd()+'/svm-cyber.p','wb'))


