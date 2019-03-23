# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 07:54:23 2019

@author: DELL
"""

import pandas as pd
daily={'day':['mon','tue','web'],'sleping':[12,5,3],'exercise':[65,45,47],'working':[6,8,13]}
print(daily)
ds=pd.DataFrame(daily)
print(ds)