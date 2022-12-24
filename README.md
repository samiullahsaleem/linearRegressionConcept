# LinearRegressionConcept

![image](https://user-images.githubusercontent.com/54318487/209437381-6c1aff3a-0d1e-491f-82b0-b81584fa9482.png)

<p>
This code uses the linear regression model from the scikit-learn library to predict a continuous value.

First, it imports the LinearRegression class from scikit-learn and creates an instance of the model called "model". Then, it loads the data that will be used to train the model. In this case, the data consists of two lists: X and y. X contains a list of integers from 1 to 10, and y contains the corresponding values of 8, 16, 24, 32, 40, 48, 56, 64, 72, and 80.

Next, the code trains the model on the data by calling the "fit" method and passing in the X and y arrays as arguments. This method fits the model to the data and allows it to learn the relationship between X and y.

Finally, the code makes a prediction using the model by calling the "predict" method and passing in a new test value, [[30000]], as an argument. The result of this prediction is stored in the variable "z" and printed to the console as an integer.
</p>
