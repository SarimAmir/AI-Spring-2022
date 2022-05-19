# GROUP MEMBERS
### 1. SARIM AMIR - 63686 
In SVM problem I was facing was liblinear was failing to converge and unable to print k fold accuracy scores when i was puttingh cv=10. I changed the value for cv from 10 to 4 and this solved it but was still getting 50% accuracy. To increase the accuracy I used StandardScalar(). What standard scalar does is it removes the mean value and scales each feature/variable to unit variance. It transform our data such that its distribution will have a mean value 0 and standard deviation of 1. Given the distribution of the data, each value in the dataset will have the mean value subtracted, and then divided by the standard deviation of the whole dataset. It increases the accuracy from 50% to 60%. ![output](https://user-images.githubusercontent.com/73839879/168486071-c52df4e6-e393-4eb1-9a28-860a2f011d93.PNG)
### 2. ZAIN AHMED SIDDIQUI - 64131
If your test data set has a categorical variable of a category that wasn't present in the training data set, the Naive Bayes model will assign it zero probability and won't be able to make any predictions in this regard.After using grid search we found that the best accuracy is at [paramater =10.0] and after trying several times with diffrent parameters we got no change.
![kaggle score](https://user-images.githubusercontent.com/85029018/169362565-7f3181dc-2fde-486a-84a3-31c3059443bc.JPG)
### 3. ZEESHAN BIN SAEED - 64126
One of the disadvantages of grid search is that when it comes to dimensionality, it endures when assessing the number of hyperparameters develops exponentially. In any case, there's no ensure that the look will create the perfect arrangement, because it usually finds one by aliasing around the proper set and the the best accuracy i got 0.548 at 0.5 because there were no change found after trying other values like 0.8, 0.3 , 0.6.
![kaggle snip](https://user-images.githubusercontent.com/57366208/169365530-4c5891e9-4f41-461e-b8d8-6c2dfe390fe1.JPG)


