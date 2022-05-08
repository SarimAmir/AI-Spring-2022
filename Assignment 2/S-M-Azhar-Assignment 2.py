Name: Shah Muhammad Azhar-62822

import pandas as pd
import numpy as np

testDf = pd.read_csv('C:\\Users\\Azhar Khan\\Downloads\\test.csv')
idDf = testDf[['id']]
idDf.insert(1,"target",0)
idDf['target'] = np.random.rand(700000,1)
print(idDf)
idDf.to_csv('out.csv',index=False)
