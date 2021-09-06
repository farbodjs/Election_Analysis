# Add our dependencies
import os
import csv

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize total_votes variable
total_votes = 0
# declaring candidate_votes dictionary and candidate_options list
candidate_votes ={}
candidate_options =[]  
# Open the election results and read the file.
with open(file_to_load) as election_data:
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # read the header row.
    headers = next(file_reader)

    # looping through rows in CSV file
    for row in file_reader:
        # add to toal_votes count
        total_votes = total_votes + 1
        # Print the candidate name from each row
        candidate_name = row[2]
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates. 
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
            # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
    # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        # 3. Calculate the percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100
        # 4. Print the candidate name and percentage of votes.
        print(f"{candidate_name}: received {vote_percentage:.2f}% of the vote.")



        
        

# Print the candidate list. q
print(candidate_options)
print(candidate_votes)
        








    

#1. The total number of votes cast.
#2. A complete list of candidates who recieved votes.
#3. The percentage of votes each candidate won.
#4. The total number of votes each candidate won.
#5. The winner of the election based on popular votes.

