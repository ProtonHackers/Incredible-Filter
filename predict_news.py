# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 04:25:41 2017

@author: rohankoodli
"""

import pickle, os, json
from antibully import iterate_tone_analysis, get_features


pickle.load(open(os.getcwd() + '/svm-news.p','rb'))

f = open(os.getcwd()+'/data/realnews/la-1.txt','rw')
cnn = f.read()
print type(cnn)
new = cnn.replace("'","\'")
new2 = new.replace('"','\"')

feat = get_features(iterate_tone_analysis(new2))
print svc.predict(feat)