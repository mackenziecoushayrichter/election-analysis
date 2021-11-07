# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates that received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on the popular vote

import csv
import os

#Assign a variable for the file to load and the path
file_to_load = os.path.join('resources', 'election_results.csv')

#Assign a variable to save the file to a path
file_to_save = os.path.join('analysis', 'election_analysis.txt')

#1. Initialize a total votes counter
total_votes = 0

#candidate options
candidate_options= []

#Declare empty dictionary
candidate_votes = {}

#Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #Read the header row
    headers = next(file_reader)

    #print each row in the csv file
    for row in file_reader:
        #2. add to the total vote count
        total_votes+=1
    
        #print candidate name from each row
        candidate_name = row[2]

        #If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            #add to list of candidates
            candidate_options.append(candidate_name)

            #begin tracking that candidates vote count
            candidate_votes[candidate_name] = 0


#print candidate list
print(candidate_votes)




    




    
  


    

  






