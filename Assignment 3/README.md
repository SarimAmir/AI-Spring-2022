# GROUP MEMBERS
### 1. SARIM AMIR - 63686 
working on KNN and SVM.
Problem faced while working on KNN  was that KNN is best suited and usually used on small dataset. Was taking hours to execute. I solved the problem by just only using train.csv file and splitting it into 80-20 train test ratio. Even after this it took 1 hour to give output but It did help me achieved 72% accuracy but i was unable to make csv file of submission to submit on kaggle since I dropped 'id' column from train.csv file. \
In SVM problem I was facing was liblinear was failing to converge and unable to print k fold accuracy scores when i was puttingh cv=10. I changed the value for cv from 10 to 4 and this solved it but was still getting 50% accuracy.
#### KNN OUTPUT ON DATASPELL IDE:

![image](https://user-images.githubusercontent.com/73839879/168484589-074b66b2-3c64-4e9a-8e28-96fd43ea30f6.png)

#### SVM OUTPUT ON KAGGLE:

![WhatsApp Image 2022-05-13 at 7 32 01 AM](https://user-images.githubusercontent.com/73839879/168313252-9aa10341-73c3-480c-8060-eb5d9a1024ba.jpeg)


### 2. OWAIS ZAHID - 64139
Problem: The problem was that the dataset was huge and system couldn't bear so have done working on Kaggle like preparing notebook. Also I have checked and applied some data cleaning techniques like removing outliers but it didn't affect the accuracy.

Working: The Algorithm I used is KNN (K-Nearest Neighbour) in which I checked accuracy on different neighbors  but got good one / better one on k = 15, so firstly I checked some null values and info and description on the data. 
Then I applied Cross Validation also. 
Then I get the test data separated the id column and then predicted the testing data, then make a new dataframe and made submission on Kaggle.

Note: I have made training and perform testing on 6 most related columns with the target using Feature Importance.

![KAGGLE](https://user-images.githubusercontent.com/62961644/168481303-91a43ffb-8e58-4815-815f-98b23d771140.jpeg)

### 3. MUHAMMAD ZEESHAN BIN SAEED - 64126
Working on Naive Bayes - Lidstone Smoothing
Problems I Faced: Tackling the Dataset and performing different operations to handle my scenerios.
My Working: The  Naive Bayes algorithm Lidstone Smoothing is a Bayesian learning approach which I used but firstly I applied Min Max Scaling because Multinomial NB doesn't take negative values.



### KAGGLE OUTPUT
![kaggle score](https://user-images.githubusercontent.com/57366208/168481482-12766750-d182-4a15-bfe3-591f9f48b081.JPG)


### 4.ZAIN AHMED SIDDIQUI - 64131
Problems I Faced: Handling the data was a main problem because the data was huge so I come to grips with the data by checking for incorrect data, checking for null values and checking some data info.

Solutions: I solved things of data handling using Pandas and applied Bernoulli & gaussian Naive Bayes  (Laplace Smoothing) and get accuracy then get predictions on testing data and created a new csv file containing id and predicted target values (x2 Columns) then saved as a CSV file and uploaded to kaggle and get the score which is attached in the file.
![zain](https://user-images.githubusercontent.com/85029018/168482073-5be6cba2-977f-42b7-9821-d61357a82f22.jpeg)


### 5. SHAH MUHAMMAD AZHAR - 62822
Problem I Faced: Problem is the data was a main problem because the data was huge so it is time consuming. and at first run accuracy was not that good.
Solution: I do cross validation, due to this the accuracy is better than the previous one
![Azharcsv](https://user-images.githubusercontent.com/73800301/168966053-98a4cfda-1ff5-4b28-ad75-925fc655bafd.PNG)

