# -*- coding: utf-8 -*-
"""AppliedMathematics exercise1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jdX1EL1zCaaszmfn2Pg9hc7ssijpgiAT
"""

#creating Series from Array
import pandas as pd
import numpy as np
new_array=np.array(['P','U','J','A'])
call=pd.Series(new_array)
print(call)

#create a Dataframe using list
import pandas as pd
list=['Python','Panther']
df= pd.DataFrame(list)
print(df)

#pandas Series.map
import pandas as pd
import numpy as np
array= pd.Series(['Java','Python','C++','C'])
array.map({'Python':'Puja','Java':'Fortan'})

#another example on mapping
a= pd.Series(['Java','Python','C++',np.nan])
a.map({'Java':'Pika'})
a.map('I like {}'.format, na_action='ignore')

#converting Series into DataFrame
s=pd.Series(['a','b','c'])
name="vals"
s.to_frame()

#Another example on converting Series to DataFrame
import matplotlib.pyplot as plt
Employer= ['Rajkaran','Pratik','Rahul','Vijay']
ID = [100,101,102,103]
Employer_series = pd.Series(Employer)
id_series = pd.Series(ID)
frame = {'Employer':Employer_series, 'ID':id_series}
Result = pd.DataFrame(frame)
print(Result)