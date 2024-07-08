#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_input_args.py
#                                                                             
# PROGRAMMER: Saulita Smith
# DATE CREATED:    06 of November 2023                               

# PURPOSE: Create a function that retrieves the following 3 command line inputs 
#          from the user using the Argparse Python module.
#     1. Image Folder as --dir with default value 'pet_images'
#     2. CNN Model Architecture as --arch with default value 'vgg'
#     3. Text File with Dog Names as --dogfile with default value 'dognames.txt'

# Imports python modules
import argparse

def get_input_args():
      # Create Parse using ArgumentParser
    parser = argparse.ArgumentParser()
    # Creating 3 command line arguments using add_argument() from ArguementParser method
    parser.add_argument("--dir", 
                        type=str, 
                        default = 'pet_images/', 
                        help='Path to folder of pet_images')
    parser.add_argument("--arch", 
                        type=str, 
                        default = 'vgg', 
                        choices = ('vgg','resnet','alexnet'), 
                        help='The neural network architecture to choose')
    parser.add_argument("--dogfile",
                        type=str,
                        default = 'dognames.txt',
                        help='Dog breed names to reffer to')
    
    args = parser.parse_args()
    
    return args

    
