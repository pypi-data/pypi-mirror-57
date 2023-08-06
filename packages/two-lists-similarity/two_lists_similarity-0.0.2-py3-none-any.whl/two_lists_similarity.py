# -*- coding: utf-8 -*-
"""
Created on Fri Dec  12 14:50:00 2019

@author: Praneeth Ponnekanti (+91-9710331264) (praneeth.ponnekanti@gmail.com)

"""


import pandas as pd
from fuzzywuzzy import fuzz,process
import time
import sys
import os
import logging
import time




class Calculate_Similarity():

    def __init__(self, input_list, ref_list):   
        
        #Create global variables for storing the input and reference lists so that these can be used across various functions in the class
        self.input_list = input_list
        self.ref_list = ref_list
        
        #Create the columns for the output dataframe/csv file that contains the similarity calculations for each input list item.
        # Create an index column in the dataframe which containts an incremental counter to ensure smooth copying of data into the data frame during fuzzy matching.
        self.similarity_df = pd.DataFrame(columns = ['index','input_list_item', 'similar_ref_list_item', 'similarity_score'])
        
    
    
    
    def fuzzy_match_output(self, output_csv_name = None, output_csv_path = os.getcwd()) :
        '''
        Inputs : Input list, Reference list
        
        Functionality : 1. Compares every item in the input list against all the items in the reference list 
                        2. Calculates similarity scores for each of the above mentioned comparisons
                        3. Matches the list item in the input list with its counterpart in the reference list that has the highest similarity score.
        
        Output : A dataframe with (Input_List_Item, Matched Reference List Item, Similarity Score)  
                 A csv file with the above mentioned records if you wish to use it for further comparisons. Default Directory is the current working directory.
        '''
        
        # Create an index in the dataframe to ensure smooth copying of data into the data frame.
        ctr = 0 #Index Iterator Variable
        start_time = time.time()
    #Fuzzy Matching starts now.
        logging.info("Initiating fuzzy matching.......")
        print ("Initiating fuzzy matching.......")
        print ("------------------------------------------------")
        for i in self.input_list :    
            print("Input column name : " + i)
            Ratios = process.extract(i,self.ref_list)
            print ("Similarity Ratios when compared with the similar reference list items are as below : ", Ratios)
            highest  = process.extractOne(i,self.ref_list)
            #print ("Input, Ref, Score.")
            #print(i,highest[0],highest[1])
            self.similarity_df.at[ctr,'input_list_item'] = i
            self.similarity_df.at[ctr,'similar_ref_list_item'] = highest[0]
            self.similarity_df.at[ctr,'similarity_score'] = (highest[1]/100)
            ctr = ctr+1
            print ("Associated Reference list item with highest similarity : ")
            print(highest)
       
            print("------------------------------------------------")
    #End of fuzzy matching operation displays individual (input string, matched reference column name, similarity score)   
        logging.info("Fuzzy matching complete.")
        self.similarity_df = self.similarity_df.drop(['index'],axis = 1)

        #Convert tuple to string to further perfrom string operations
        self.similarity_df['similar_ref_list_item'] = self.similarity_df['similar_ref_list_item'].apply(lambda x : ''.join(x))
        
        #Convert Similarity score into a flot from tuple
        self.similarity_df['similarity_score'] = self.similarity_df['similarity_score'].apply(lambda y : float(y))
        self.similarity_df['similar_ref_list_item'] = self.similarity_df['similar_ref_list_item'].replace("(","").replace(",)" , "")
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("Datatypes Check : ")
        print(self.similarity_df.dtypes)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        
        if (output_csv_name is not None) : 
            print ("Generating similarity calculation output file... ")
            logging.info("Generating similarity calculation output file...")
            final_output_path = os.path.join(output_csv_path, output_csv_name)
            self.similarity_df.to_csv(final_output_path, index = False)
            print("Output file generated at : " , final_output_path)
        else : 
            print("File Generation error : -----No output filename mentioned.------")

        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("Output Data Frame looks like : ")
        print (self.similarity_df.head(5))
        print("***********************************************")
        print ("Fuzzy Matching Output generated in : ")
        print("--- %s seconds ---" % (time.time() - start_time))

        logging.info("***********************************************")
        logging.info(" Fuzzy Matching Output generated in :  ")
        logging.info("--- %s seconds ---" % (time.time() - start_time))
        print("***********************************************")

        return self.similarity_df
       
    
    
    
    
    def dissimilar_input_items(self, similarity_threshold = 0.65):
        
        '''
        Input : Threshold to filter the items from the input_list that are way too similar. Recommended value : 65%
        
        Functionality : Applies the threshold to filter out the records that have similarity_score <= Treshold
        
        Output : List of items from the input list that have similarity scores <= threshold when compared against all the reference list items        
        '''
        
        uc_inp_list = []
        uc_inp_list.extend(list(self.similarity_df['input_list_item'].loc[self.similarity_df['similarity_score'] <= similarity_threshold]))
        if len (uc_inp_list) == 0:
            print ("All input list items matched. No different input list items found.")
            logging.info("All input list items matched. No different input list items found.")
        else : 
            print ("ALERT : Input list items that are way too different from the reference list items are : ", uc_inp_list)
            logging.info(" Input list items that are way too different from the reference list items are :: " + str(uc_inp_list))
       
        return uc_inp_list