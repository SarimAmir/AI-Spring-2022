#Sarim Amir's code 63686

import pandas as pd
import numpy as np
train_df=pd.read_csv('tabular-playground-series-may-2022/test.csv')
id_df=train_df[['id']]
id_df.insert(1,"target",0)
id_df['target']=np.random.rand(700000,1)
print(id_df)
id_df.to_csv ('output.csv',index=False)

#Sarim Amir's code 63686