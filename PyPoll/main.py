# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
#"/Users/ana/Desktop/python-challenge/PyPoll
#/Users/ana/Desktop/python-challenge/PyPoll/Resources/
file_to_load = os.path.join("/Users/ana/Desktop/python-challenge/PyPoll/Resources/", "election_data.csv") # Input file path  # Input file path
file_to_output = os.path.join("/Users/ana/Desktop/python-challenge/PyPoll/analysis/", "election_analysis.txt")  # Output file path


# Initialize variables to track the election data
total_votes = 0  # Track the total number of votes cast

# Define lists and dictionaries to track candidate names and vote counts
candLst ={}
print(candLst)


# Winning Candidate and Winning Count Tracker 
canName =""
winner = ""
winnerVoteCount = 0


# Open the CSV file and process it
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Skip the header row
    header = next(reader)

    # Loop through each row of the dataset and process it
    for row in reader:

        # Print a loading indicator (for large datasets)
        print(". ", end="")

        # Increment the total vote count for each row
        total_votes += 1 

        # Get the candidate's name from the row
        canName = row[2]

        # If the candidate is not already in the candidate list, add them
        if canName not in candLst:

            candLst.update({canName:[1,0.0]})

        # Add a vote to the candidate's count
        else:
            candLst[canName][0] += 1

print("\nElection Results\n------------------------------------------------")


# Open a text file to save the output
with open(file_to_output, "w") as txt_file:

    # Print the total vote count (to terminal)
    print(f'Total Votes: {total_votes}\n------------------------------------------------')

    # Write the total vote count to the text file
    txt_file.write(f'Election Results\n------------------------------------------------'
                   f'\nTotal Votes: {total_votes}\n------------------------------------------------\n')

    # Loop through the candidates to determine vote percentages and identify the winner
    for name in candLst:

        # Get the vote count and calculate the percentage
        percent = (candLst[name][0]/total_votes) * 100
        percent = round(percent,3)
        candLst[name][1] = percent

        # Update the winning candidate if this one has more votes
        # First Condition: Save first canidate and voter count

        if  winner == "":
            winner = name
            winnerVoteCount = candLst[name][0]

        # Compare if another canidate has a higher voter count than the current leader. If so, reassign the winner variable
        elif candLst[name][0] > winnerVoteCount:
            winner = name
            winnerVoteCount = candLst[name][0]

        # Print and save each candidate's vote count and percentage
        print(f'{name}: {percent}% ({candLst[name][0]})')
        txt_file.write(f'{name}: {percent}% ({candLst[name][0]})\n')


    # Generate and print the winning candidate summary
    print(f'------------------------------------------------\nWinner: {winner}\n------------------------------------------------')


    # Save the winning candidate summary to the text file
    txt_file.write(f"------------------------------------------------\nWinner: {winner}\n------------------------------------------------")
