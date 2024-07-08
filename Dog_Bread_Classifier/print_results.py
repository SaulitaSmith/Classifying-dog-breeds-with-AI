#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#                                                                             
# PROGRAMMER: Saulita Smith
# DATE CREATED: 06 November 2023

# PURPOSE: Create a function print_results that prints the results statistics
#          from the results statistics dictionary (results_stats_dic). 
#         This function inputs:
#            -The results dictionary as results_dic within print_results 
#             function and results for the function call within main.
#            -The results statistics dictionary as results_stats_dic within 
#             print_results function and results_stats for the function call within main.
#            -The CNN model architecture as model wihtin print_results function
#             and in_arg.arch for the function call within main. 
#            -Prints Incorrectly Classified Dogs as print_incorrect_dogs within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#            -Prints Incorrectly Classified Breeds as print_incorrect_breed within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)

def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs=False, print_incorrect_breed=False):
 
    # Print the results
    print("Results for model: {}".format(model))
    print("Number of images: {}".format(len(results_dic)))
    print("Number of dog images: {}".format(results_stats_dic['n_dogs_img']))
    print("Number of not-dog images: {}".format(results_stats_dic['n_notdogs_img']))
    print("Percentage of correct not-dog predictions: {}".format(results_stats_dic['pct_correct_notdogs']))
    print("Percentage of correct dog predictions: {}".format(results_stats_dic['pct_correct_dogs']))
    print("Percentage of correct dog breed predictions: {}".format(results_stats_dic['pct_correct_breed']))
    print("Percentage of match labels: {}".format(results_stats_dic['pct_match']))
    
    if print_incorrect_dogs:
        print("Incorrectly classified dogs:")
        for key in results_dic:
            if results_dic[key][3] == 0 and results_dic[key][4] == 1:
                print("Real: {}   Classifier: {}".format(results_dic[key][0], results_dic[key][1]))
    
    if print_incorrect_breed:
        print("Incorrectly classified breed:")
        for key in results_dic:
            if results_dic[key][3] == 1 and results_dic[key][2] == 0:
                print("Real: {}   Classifier: {}".format(results_dic[key][0], results_dic[key][1]))
  
 
  
                
