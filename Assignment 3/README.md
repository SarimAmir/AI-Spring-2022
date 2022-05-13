# GROUP MEMBERS
### 1. SARIM AMIR - 63686 
working on KNN and SVM.
Problem faced while working on KNN  was that KNN is best suited and usually used on small dataset. Was taking hours to execute. I solved the problem by just only using train.csv file and splitting it into 80-20 train test ratio. Even after this it took 1 hour to give output but It did help me achieved 71% accuracy but i was unable to make csv file of submission to submit on kaggle since I dropped 'id' column from train.csv file. \
In SVM problem I was facing was liblinear was failing to converge. I tried to solve it by using standard scalar. I tried to scale data to 0 mean, unit standard deviation using Scikit-Learn's StandardScaler. What it did was it increased accuracy from 0.51 to 0.60 but still gives failing to converge warning and unable to print k fold accuracy scores.
#### KNN OUTPUT ON DATASPELL IDE:

![knn output-dtaspell](https://user-images.githubusercontent.com/73839879/168310337-d3578c60-1202-4e3b-bf2a-5475423ffb68.PNG)

#### SVM OUTPUT ON KAGGLE:
##### BEFORE USING STANDARD SCALAR:
![WhatsApp Image 2022-05-13 at 7 32 01 AM](https://user-images.githubusercontent.com/73839879/168313252-9aa10341-73c3-480c-8060-eb5d9a1024ba.jpeg)

##### AFTER USING STANDARD SCALAR:
![image](https://user-images.githubusercontent.com/73839879/168312746-b1a5b15e-c26f-47a0-83b2-8dcc1c8bd254.png)
