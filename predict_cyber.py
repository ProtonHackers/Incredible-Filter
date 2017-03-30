# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 23:09:24 2017

@author: rohankoodli
"""

import pickle, json, os
from antibully import iterate_tone_analysis, get_features


pickle.load(open(os.getcwd() + '/svm-cyber','rb'))
# 0 is bad
# 1 is good
'''
new = get_features(iterate_tone_analysis(''))
result = svc.predict(new)
if result == 0:
    print True
'''
def bully_analysis(string):
    svc = pickle.load(open(os.getcwd() + '/svm-cyber','rb'))
    new = get_features(iterate_tone_analysis(string))
    result = svc.predict(new)
    return result

print bully_analysis('viks screw you')        