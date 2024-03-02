#this file tests reading files in a directory
import os
import cv2
from sklearn.model_selection import train_test_split
import tensorflow as tf


print("")
print("********************New Run*******************")
print("")


cur_path = os.path.dirname(__file__)

new_path = os.path.join(cur_path,"\\Users\\kahin\\Documents\\cs502\\gtsrb\\7")  #Not the best but gets you to correct directory
print("New Path", new_path)
 
images=[] # a blank list
#This section lists all the images in the directory.  Start with only one image.
img_files_list=os.listdir(new_path)
for img_file in img_files_list[:10]:
    temp_path=os.path.join(new_path,img_file)
    image_content=cv2.imread(temp_path) #Returns the image as an numpy array
    image_content=cv2.resize(image_content,(56, 56)) #Resize the image.  Not sure if they are all around 56
    cv2.imshow("Image", image_content)  #This shows the image, press any key to close the image
    #cv2.waitKey(0) 
    temp_tupple=(image_content,"7")
    images.append(temp_tupple) #This is the final tupple


#Turn the list of tupples into evidence and row lists
evidence=[]
labels=[]
for image in images:
    evidence.append(image[0])
    labels.append(image[1])


print(labels)

#Seperate data into training and testing groups
#evidence=[row["evidence"] for row in images]
#labels=[row["label"] for row in images]
<<<<<<< HEAD
X_training, X_testing, Y_training, Y_testing=train_test_split(
=======
X_training, X_testing, y_training, y_testing=train_test_split(
>>>>>>> e154eb8a3237b731d6e21831157e0500e0920ae1
    evidence, labels, test_size=0.4
)

#Define
model=Sequential()



#Compile

#Train

#Evaluate








