#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND/intropylab-classifying-images/test_classifier.py
#                                                                             
# PROGRAMMER: Saulita Smith                                                    
# DATE CREATED: 06 Noveber 2023                                  
                    
# PURPOSE: To demonstrate the proper usage of the classifier() function that 
#          is defined in classifier.py This function uses CNN model 
#          architecture that has been pretrained on the ImageNet data to 
#          classify images. The only model architectures that this function 
#          will accept are: 'resnet', 'alexnet', and 'vgg'. 

def classify_images(in_arg_dir, results, in_arg_arch):
    for image_name, classification in results.items():
        print(f"Image: {image_name}, Classification: {classification}")
    process_images(in_arg_dir, results, in_arg_arch)
    
    
    # Function that checks Results Dictionary using results    
     
def check_classifying_images(results):
    check_classifying_images(results)
    
    
def process_images(in_arg_dir, results, in_arg_arch):
    in_arg_dir = 'path/to/workspace'
    results = {}
    in_arg_arch = 'resnet40'





# Imports classifier function for using pretrained CNN to classify images 
from classifier import classifier 

# Defines a dog test image from pet_images folder
test_image="pet_images/Collie_03797.jpg"

# Defines a model architecture to be used for classification  
model = "vgg"

# Demonstrates classifier() functions usage
image_classification = classifier(test_image, model)

# prints result from running classifier() function
print("\nResults from test_classifier.py\nImage:", test_image, "using model:",
      model, "was classified as a:", image_classification)
