# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 23:09:24 2017

@author: rohankoodli
"""

import pickle, json, os
from website.antibully import iterate_tone_analysis, get_features

# pickle.load(open(os.getcwd() + '/svm-cyber.p','rb'))
# 0 is bad
# 1 is good
'''
new = get_features(iterate_tone_analysis('viks i hate you'))
result = svc.predict(new)
if result == 0:
    print True
'''


def bully_analysis(string):
    svc = pickle.load(open('svm-cyber.p', 'rb'))
    new = get_features(iterate_tone_analysis(string))
    result = svc.predict(new)
    return result
