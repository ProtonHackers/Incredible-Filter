# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 19:07:32 2017

@author: rohankoodli
"""

from watson_developer_cloud import NaturalLanguageClassifierV1
import json

natural_language_classifier = NaturalLanguageClassifierV1(
  username='26db2c5b-2eda-46d0-9c66-438d943713d8',
  password='O3UAXtApBXOQ')

classes = natural_language_classifier.classify('90e7acx197-nlc-4557', 'How hot will it be today?')
print(json.dumps(classes, indent=2))