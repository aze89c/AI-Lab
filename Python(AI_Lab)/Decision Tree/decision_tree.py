'''                                  4a. Decision tree 
A Decision Tree is an algorithm that is used to visually represent decision-making. A Decision Tree 
can be made by asking a yes/no question and splitting the answer to lead to another decision. The 
question is at the node and it places the resulting decisions below at the leaves. The tree depicted below 
is used to decide if we can play tennis. 
REFER THE "TENNIS" IMAGE. 

Important Terms Used in Decision Trees 
1. 
Root Node: The root node is always the top node of a decision tree. It represents the entire 
population or data sample, and it can be further divided into different sets. 
Entropy: Entropy is the measure of uncertainty or randomness in a data set. Entropy handles 
how a decision tree splits the data. 
It is calculated using the following formula: 
2. Information Gain: The information gain measures the decrease in entropy after the data set is split. 
It is calculated as follows: 
IG( Y, X) = Entropy (Y) - Entropy ( Y | X) 
3. 
Gini Index: The Gini Index is used to determine the correct variable for splitting nodes. It 
measures how often a randomly chosen variable would be incorrectly identified. 
4. 
REFER THE FORMULA IMAGE.
 
 
5. Decision Node: Decision nodes are subnodes that can be split into different subnodes; they 
contain at least two branches. 
 
6. Leaf Node: A leaf node in a decision tree carries the final results. These nodes, which are also 
known as terminal nodes, cannot be split any further. 
 
 
LOAD THE DATA 
TRAIN THE DATA 
TEST THE DATA 
DISPLAY THE DATA

'''

# 4a. Write a program to train and validate the following classifiers 
# for given data (Scikit-learn) :   Decision tree 
 
from sklearn.datasets import make_classification 
from sklearn import tree 
from sklearn.model_selection import train_test_split 

# Generate a synthetic dataset
X, t = make_classification(100, 5, n_classes=2, shuffle=True, random_state=10)  

# Split the dataset into training and test sets
X_train, X_test, t_train, t_test = train_test_split(X, t, test_size=0.3, shuffle=True, random_state=1) 

# Train a Decision Tree classifier
model = tree.DecisionTreeClassifier() 
model = model.fit(X_train, t_train) 

# Predict on the test set
predicted_value = model.predict(X_test) 
print("Predicted values:", predicted_value) 

# Visualize the decision tree (requires matplotlib)
tree.plot_tree(model) 

# Count number of zeroes and ones in the training labels
zeroes = 0 
ones = 0 

for i in range(len(t_train)):  
    if t_train[i] == 0:
        zeroes += 1 
    else: 
        ones += 1 

print("Zeroes:", zeroes) 
print("Ones:", ones) 

# Calculate Gini index for the training set
val = 1 - ((zeroes/70)**2 + (ones/70)**2) 
print("Gini:", val) 

# Calculate accuracy on the test set
match = 0 
unmatch = 0 

for i in range(len(t_test)): 
    if predicted_value[i] == t_test[i]:  
        match += 1 
    else: 
        unmatch += 1 

accuracy = match / len(t_test)
print("Accuracy is:", accuracy)
 
 
'''

Output: 
 
[0 1 0 1 0 0 0 0 0 0 1 0 0 1 0 0 0 0 1 1 0 1 0 0 0 1 1 1 0 0] 
 
31 
 
 
39 
 
Gini : 0.4934693877551021 
 
Accuracy is: 0.8333333333333334 

'''