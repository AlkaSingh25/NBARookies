# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 18:35:04 2024

@author: Admin
"""

import requests

url = 'https://localhost:5000/predict_api'
r = requests.post(url,json={'experience':2,
                            'test_Score':9,
                            'interview_score':6
                            })

print(r.json())