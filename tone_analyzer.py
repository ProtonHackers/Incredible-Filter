# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 17:31:41 2017

@author: rohankoodli
"""

import json
import os
from watson_developer_cloud import ToneAnalyzerV3, NaturalLanguageClassifierV1
from sklearn.svm import SVC
import pickle

tone_analyzer = ToneAnalyzerV3(
   username='26db2c5b-2eda-46d0-9c66-438d943713d8',
   password='O3UAXtApBXOQ',
   version='2016-05-19')

def iterate_tone_analysis(jsonfile):
    return tone_analyzer.tone(text=jsonfile)
    
def get_features(json_text):
    main_json = []
    for val in json_text['document_tone']['tone_categories']:
        for i in val['tones']:
            main_json.append(i['score'])
    return main_json    

realnews = []
fakenews = []

for i in realnews:
    tone = iterate_tone_analysis(i)
    features = get_features(tone)
    realnews.append(features)
    realnews_labels = [0] * len(realnews)

for i in fakenews:
    tone = iterate_tone_analysis(i)
    features = get_features(tone)
    fakenews.append(features)
    fakenews_labels = [1] * len(fakenews)

allnews = realnews + fakenews
labels = realnews_labels + fakenews_labels

svc = SVC()
svc.fit(allnews,labels)
pickle.dump(svc,os.getcwd()+'/svm')



'''
natural_language_classifier = NaturalLanguageClassifierV1(
  username='568b8beb-6d6d-4dcf-8580-77f1d13d5a0e',
  password='wksunbZBrAyF')

with open(os.getcwd() + '/train.csv', 'rb') as training_data:
  classifier = natural_language_classifier.create(
    training_data=training_data,
    name='My Classfier',
    language='en'
  )
print(json.dumps(classifier, indent=2))

classes = natural_language_classifier.classify('90e7acx197-nlc-4545', 'very sincere')
print(json.dumps(classes, indent=2))
'''