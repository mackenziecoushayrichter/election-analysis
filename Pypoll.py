# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates that received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on the popular vote

#Add our dependencies
import csv
import os

#Assign a variable for the file to load and the path
file_to_load = os.path.join('resources', 'election_results.csv')

#Assign a variable to save the file to a path
file_to_save = os.path.join('analysis', 'election_analysis.txt')

#1. Initialize a total votes counter
total_votes = 0

#candidate options list
candidate_options= []

#Declare empty dictionary for candidate votes
candidate_votes = {}

#winning candidate and winning candidate tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    #Read the header row
    headers = next(file_reader)

    #print each row in the csv file
    for row in file_reader:
        #add to the total vote count
        total_votes+=1
    
        #get candidate name from each row
        candidate_name = row[2]

        #If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            #add to list of candidates
            candidate_options.append(candidate_name)

            #begin tracking that candidates vote count
            candidate_votes[candidate_name] = 0

        #add a vote to that candidates count
        candidate_votes[candidate_name]+=1
    
#Save the results to our text file
with open(file_to_save, "w") as txt_file:
    #print the final vote count to the terminal
    election_results= (
        f'\n Election Results\n'
        f'-------------------------\n'
        f'Total Votes: {total_votes:,}\n'
        f'-------------------------\n')
    print(election_results, end="")
    #Save the final vote count to the text file
    txt_file.write(election_results)


    #determine the percentage of votes for each candidate by looping through the counts
    #1. Iterate through the candidate list
    for candidate_name in candidate_votes:
        #2. Retrieve vote count of a candidate
        votes= candidate_votes[candidate_name]
        #3. Calculate the percentage of votes
        vote_percentage = round(float(votes)/float(total_votes) *100,1)
        
        #Print out each candidates name, vote count, and percentage of votes to the terminal
        candidate_results=(f'{candidate_name} : {vote_percentage}% ({votes:,})\n')
        print(candidate_results)
        #save the candidate results to the text file
        txt_file.write(candidate_results)

        #determing winning vote count and candidate
        #1. determing if the votes are greater than the winning count
        if (votes> winning_count) and (vote_percentage> winning_percentage):
            #2. If true then set winning_count = votes and winning_percentage = vote_percentage
            winning_count= votes
            winning_percentage = vote_percentage
            #3. Set the winning_candidate equal to the candidates name
            winning_candidate = candidate_name

    #Pring winning candidates results to the terminal
    winning_candidate_summary = (
        f"-------------------------\n"
        f'Winner: {winning_candidate}\n'
        f'Winning Vote Count: {winning_count:,}\n'
        f'Winning Percentage: {winning_percentage}%\n')

    print(winning_candidate_summary)

    #save winning candidates name to the text file
    txt_file.write(winning_candidate_summary)









        




        
    


        

    






