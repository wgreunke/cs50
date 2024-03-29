import cv2 #https://www.askpython.com/python/examples/convert-images-to-numpy-arrays
import numpy as np
import os
import sys
import tensorflow as tf

from sklearn.model_selection import train_test_split

EPOCHS = 10
IMG_WIDTH = 30
IMG_HEIGHT = 30
NUM_CATEGORIES = 43
TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) not in [2, 3]:
        sys.exit("Usage: python traffic.py data_directory [model.h5]")

    # Get image arrays and labels for all image files
    #images, labels = load_data(sys.argv[1])
    images, labels = load_data("C:/Users/kahin/Documents/CS50/gtsrb/7") #Testing on single directory
    #"C://Users//Vanshi//Desktop//gfg"
    #"C:\Users\kahin\Documents\AI"

    # Split data into training and testing sets
    labels = tf.keras.utils.to_categorical(labels)
    x_train, x_test, y_train, y_test = train_test_split(
        np.array(images), np.array(labels), test_size=TEST_SIZE
    )

    # Get a compiled neural network
    model = get_model()

    # Fit model on training data
    #model.fit(x_train, y_train, epochs=EPOCHS)

    # Evaluate neural network performance
    #model.evaluate(x_test,  y_test, verbose=2)

    # Save model to file
    if len(sys.argv) == 3:
        filename = sys.argv[2]
        model.save(filename)
        print(f"Model saved to {filename}.")


def load_data(data_dir):
    """
    Load image data from directory `data_dir`.

    Assume `data_dir` has one directory named after each category, numbered
    0 through NUM_CATEGORIES - 1. Inside each category directory will be some
    number of image files.

    Return tuple `(images, labels)`. `images` should be a list of all
    of the images in the data directory, where each image is formatted as a
    numpy ndarray with dimensions IMG_WIDTH x IMG_HEIGHT x 3. `labels` should
    be a list of integer labels, representing the categories for each of the
    corresponding `images`.
    """

    #Get a list of files in the directory
    dir_list = os.listdir(data_dir)
    print(data_dir)
    print("Files and directories in '", data_dir, "' :")
    # prints all files
    print(dir_list)

    #Read each file, set to a tupple then return the set of tupples.
    
    #


    raise NotImplementedError


def get_model():
#https://www.youtube.com/watch?v=J1QD9hLDEDY&t=3072s  Minute 50:

    """
    Returns a compiled convolutional neural network model. Assume that the
    `input_shape` of the first layer is `(IMG_WIDTH, IMG_HEIGHT, 3)`.
    The output layer should have `NUM_CATEGORIES` units, one for each category.
    """
    raise NotImplementedError


if __name__ == "__main__":
    main()
