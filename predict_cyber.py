# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 23:09:24 2017

@author: rohankoodli
"""

import pickle, json, os
from antibully import iterate_tone_analysis, get_features


pickle.load(open(os.getcwd() + '/svm-cyber.p','rb'))

new = get_features(iterate_tone_analysis('you are the greatest'))
print svc.predict(new)

