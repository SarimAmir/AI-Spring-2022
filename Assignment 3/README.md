# GROUP MEMBERS
### 1. SARIM AMIR - 63686 
working on KNN and SVM.
Problem faced while working on KNN because KNN is best suited and usually used on small dataset. I solved the problem by just only using train.csv file and splitting it into 80-20 train test ratio. It did help me achieved 71% accuracy but i was unable to make csv file of submission to submit on kaggle since I dropped 'id' column from train.csv file. \
In SVM problem I was facing was liblinear was failing to converge. I tried to solve it by using standard scalar. I tried to scale data to 0 mean, unit standard deviation using Scikit-Learn's StandardScaler. What it did was it increased accuracy from 0.51 to 0.60 but still gives failing to converge warning.
#### KNN OUTPUT ON DATASPELL IDE:

![knn output-dtaspell](https://user-images.githubusercontent.com/73839879/168310337-d3578c60-1202-4e3b-bf2a-5475423ffb68.PNG)

#### SVM OUTPUT ON KAGGLE:
![image](https://user-images.githubusercontent.com/73839879/168312746-b1a5b15e-c26f-47a0-83b2-8dcc1c8bd254.png)
