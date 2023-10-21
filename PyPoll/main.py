#import the csv and os modules
import csv
import os

#read in csv file
csv_file = os.path.join('Resources', 'election_data.csv')

#create reader from csv_file
with open(csv_file, 'r') as election_data:
    reader = csv.reader(election_data, delimiter = ",")

#store and skip header
    header = next(reader)

#initialize variables and lists
    total_vote_count = 0
    candidate_count = 0
    iteration = 0
    candidate_list = []
    vote_tally = []
    votes_list = []
    vote_percentage = []
    
    #use a list comprehension to loop through reader and add votes to the votes list
    votes_list = [row[2] for row in reader]

#count the total votes
total_vote_count = len(votes_list)

#separate out the unique candidate names from the votes list into a candidate list
for vote in votes_list:
    if vote not in candidate_list:
        candidate_list.append(vote)

#loop through each unique candidate
for candidate in candidate_list: 
    
    #count the presence of each candidate's name in the votes list and assign the total to the votes tally
    candidate_count = [vote for vote in votes_list if vote == candidate]
    vote_tally.append(len(candidate_count))
 
#calculate vote percentage
for vote in vote_tally:
    vote_percentage.append(round(int(vote) / int(total_vote_count) * 100, 3))

#establish popular vote winner
popular_vote = max(vote_tally) 
winner = candidate_list[vote_tally.index(popular_vote)]

#zip candidates, vote percentages and vote tallies into list 
results = list(zip(candidate_list, vote_percentage, vote_tally))

#print results to terminal
print('Election Results')
print('-------------------------')
print(f'Total Votes: {total_vote_count}')
print('-------------------------')
#iterate throuh results list for each entry
for result in results:
    print(f'{result[0]}: {result[1]}% ({result[2]})')
print('-------------------------')
print(f'Winner: {winner}')
print('-------------------------')
            
#create new text file in the analysis directory
write_path = os.path.join('analysis', "analysis.txt")

#open new file in write mode
with open(write_path, 'w') as txt_file:

    #write results to txt file  
    txt_file.write('Election Results \n')
    txt_file.write('------------------------- \n')
    txt_file.write(f'Total Votes: {total_vote_count} \n')
    txt_file.write('------------------------- \n')
    #iterate throuh results list for each entry
    for result in results:
        txt_file.write(f'{result[0]}: {result[1]}% ({result[2]}) \n')
    txt_file.write('------------------------- \n')
    txt_file.write(f'Winner: {winner} \n')
    txt_file.write('------------------------- \n')