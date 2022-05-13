# GROUP MEMBERS
### 1. SARIM AMIR - 63686 
working on KNN and SVM.
Problem faced while working on KNN because KNN is best suited and usually used on small dataset. I solved the problem by just only using train.csv file and splitting it into 80-20 train test ratio. It did help me achieved 71% accuracy but i was unable to make csv file of submission to submit on kaggle since I dropped 'id' column from train.csv file.
In SVM problem I was facing was liblinear was failing to converge. I tried to solve it by using standard scalar. I tried to scale data to 0 mean, unit standard deviation using Scikit-Learn's StandardScaler
