#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/check_images.py
                                                                            
# PROGRAMMER: Saulita Smith
# DATE CREATED:  06 of November 2023                                

# PURPOSE: Classifies pet images using a pretrained CNN model, compares these
#          classifications to the true identity of the pets in the images, and
#          summarizes how well the CNN performed on the image classification task. 
          

# Imports python modules
from time import time, sleep
import os

# Imports print functions that check the lab
from print_functions_for_lab_checks import *

# Imports functions created for this program
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results

# Main program function defined below
def main():
    start_time = time()
    #sleep(75)
    
    
    # Define get_input_args function within the file get_input_args.py
    # This function retrieves 3 Command Line Arugments from user as input from
    # the user running the program from a terminal window. This function returns
    # the collection of these command line arguments from the function call as
    # the variable in_arg
    in_arg=get_input_args()

    # Function that checks command line arguments using in_arg  
    #check_command_line_arguments(in_args)
    
    results=get_pet_labels(in_arg.dir)

    classify_images(in_arg.dir, results, in_arg.arch)


    # Defines adjust_results4_isadog function within the file adjust_results4_isadog.py
    
    adjust_results4_isadog(results, in_arg.dogfile)

    # Defines calculates_results_stats function within the file calculates_results_stats.py
    # This function creates the results statistics dictionary that contains a
    # summary of the results statistics (this includes counts & percentages).
    
    results_stats = calculates_results_stats(results)
    
    
    print_results(results, results_stats, in_arg.arch, True, True)
    
    
    # Measures total program runtime by collecting end time
    end_time = time()
    # Computes overall runtime in seconds & prints it in hh:mm:ss format
    tot_time = end_time - start_time
    print("\n** Total Elapsed Runtime:",
        str(int((tot_time/3600)))+":"+str(int((tot_time%3600)/60))+":"
        +str(int((tot_time%3600)%60)) )
    
    print("\nTotal Elapsed Runtime:", tot_time, "in seconds.")


# Call to main function to run the program
if __name__ == "__main__":
    main()
