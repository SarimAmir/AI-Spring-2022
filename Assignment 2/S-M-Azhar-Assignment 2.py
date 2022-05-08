#Name: Shah Muhammad Azhar-62822
#
#Libraries

import pandas as pd
import numpy as np
#Code

testDf = pd.read_csv('C:\\Users\\Azhar Khan\\Downloads\\test.csv')
idDf = testDf[['id']]
idDf.insert(1,"target",0)
idDf['target'] = np.random.rand(700000,1)
print(idDf)
idDf.to_csv('out.csv',index=False)

Output:
![Capture](https://user-images.githubusercontent.com/73800301/167296914-110e51d8-6f95-413c-b5a2-481755de8991.PNG)
