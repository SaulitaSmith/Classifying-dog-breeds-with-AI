#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
#                                                                             
# PROGRAMMER:    Saulita Smith
# DATE CREATED:   06 of November 2023                               
# REVISED DATE: 
# PURPOSE: Create a function calculates_results_stats that calculates the 
#          statistics of the results of the programrun using the classifier's model 
#          architecture to classify the images. This function uses the 
#          results in the results dictionary to calculate these statistics. 
#          This function will then put the results statistics in a dictionary
#          (results_stats_dic) that's created and returned by this function.
#          This will allow the program to determine the 'best' 
#          model for classifying the images. The statistics that are calculated
#          are counts and percentages.   
#         This function inputs:
#            -The results dictionary as results_dic within calculates_results_stats 
#             function and results for the function call within main.
#         This function creates and returns the Results Statistics Dictionary -
#          results_stats_dic. This dictionary contains the results statistics 
#          (either a percentage or a count) where the key is the statistic's 
#           name (starting with 'pct' for percentage or 'n' for count) and value 
#          is the statistic's value.  


def calculates_results_stats(results_dic):
    n_images = len(results_dic) # number of images
    n_dogs_img = 0 # number of dog images
    n_notdogs_img = 0 # number of NON-dog images
    n_match = 0 #number of matches between pet & classifier labels
    n_correct_dogs = 0 #number of correctly classified dog images
    n_correct_notdogs = 0 #number of correctly classified NON-dog images
    n_correct_breed = 0 #number of correctly classified dog breeds

    for key in results_dic:
        is_match = results_dic[key][2]
        is_label_dog = results_dic[key][3]
        is_classify_dog = results_dic[key][4]

        #Value 3 tells us if it's a dog (i.e. was the name derived from the label, included in the dogs.txt file)
        n_dogs_img+=is_label_dog
        n_notdogs_img+=1-is_label_dog
        n_match+=is_match
        if (is_label_dog+is_classify_dog) == 2:
            n_correct_dogs+=1
        if (is_label_dog+is_classify_dog) == 0:
            n_correct_notdogs+=1
        if is_match and is_label_dog:
            n_correct_breed+=1
            
#            pct_match - percentage of correct matches
#            pct_correct_dogs - percentage of correctly classified dogs
#            pct_correct_breed - percentage of correctly classified dog breeds
#            pct_correct_notdogs - percentage of correctly classified NON-dogs
    #Numbers compiled, now calculate percentages
    pct_match= (n_match / n_images) * 100
    pct_correct_dogs = (n_correct_dogs / n_dogs_img) * 100
    pct_correct_breed = (n_correct_breed / n_dogs_img) * 100
    pct_correct_notdogs = (n_correct_notdogs / n_notdogs_img) * 100

 #   if n_dogs != 0:
 #      pct_correct_breed = (n_correct_breed / n_dogs) * 100
 #   else:
 #       pct_correct_breed = 0

    results_stats = {
        'n_images': n_images,
        'n_dogs_img': n_dogs_img,
        'n_notdogs_img': n_notdogs_img,
        'n_match': n_match,
        'n_correct_dogs': n_correct_dogs,
        'n_correct_notdogs': n_correct_notdogs,
        'n_correct_breed': n_correct_breed,
        'pct_match': pct_match,
        'pct_correct_dogs': pct_correct_dogs,
        'pct_correct_breed': pct_correct_breed,
        'pct_correct_notdogs': pct_correct_notdogs
    }

    return results_stats