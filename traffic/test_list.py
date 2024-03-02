import os  #Needed to read files 
import tensorflow as tf
import random
from sklearn.model_selection import train_test_split
import numpy as np

#Try tensorflow on trivial data.
#Input is random numbers.  Output is letters.
#1 maps to a, 2 maps to b...

#print(random.random())

x_list=[]
y_list=[]
letter_list=["a","b","c","d"]
#Loop through a first and then create 3 
for letter in letter_list:
    for i in range(6):
        print(i)
        x_list.append(round(random.random()+letter_list.index(letter),3))
        y_list.append(letter)

x_array=np.asarray(x_list)
print(x_array)
y_array=np.asarray(y_list)

#Now split into training and testing data
X_training, X_testing, Y_training, Y_testing=train_test_split(x_array,y_array,test_size=0.4)


#print(Y_training)
#print(Y_testing)
print("Starting the model")
model=tf.keras.models.Sequential()

model.add(tf.keras.layers.Dense(8,input_shape=(1,),activation="relu"))
model.add(tf.keras.layers.Dense(4, activation="sigmoid"))

model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)
model.fit(X_training, Y_training, epochs=20)
model.evaluate(X_testing,Y_testing,verbose=2)

