#this file tests reading files in a directory
import os
import cv2
from sklearn.model_selection import train_test_split
print("")
print("")

cur_path = os.path.dirname(__file__)
data_dir="C:\\Users\\kahin\\Documents\\CS50\\gtsrb\\7"
#dir_list = os.listdir(data_dir)
new_path = os.path.join(cur_path,"gtsrb\\7")

#print("The current path is", cur_path)

#print("The new path is")
#print(new_path)
# prints all files
 
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


#Seperate data into training and testing groups
evidence=[row["evidence"] for row in images]
labels=[row["label"] for row in images]
X_training, X_testing, y_training, ytesting=train_test_split(
    evidence, labels, test_size=0.4
)

print(y_training) 










#image_path=os.path.join(cur_path,"gtsrb\\7\\00027_00026.ppm")
#print("image path is",image_path)

#Now convert the image
#print(image_content.shape)

#image_tupple=(image_content,"7")
#print(image_tupple)


#Create a tupple with the image and the label





