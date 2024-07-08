#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Saulita Smith
# DATE CREATED:      06 November 2023                            
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
import os

#       Defined bellow is get_pet_labels function 
def get_pet_labels(image_dir):
    results_dic = dict()
    filename_list = os.listdir(image_dir)
    
    for filename in filename_list:
        if not filename.startswith('.'):
            #pet_label = filename.lower().split('.')[0]
            pet_label = ' '.join(filename.lower().split(".")[0].split("_")[:-1])
            
            #if check_if_dog(os.path.join(image_dir, filename)):
            results_dic[filename] = [pet_label]
    
    return results_dic

