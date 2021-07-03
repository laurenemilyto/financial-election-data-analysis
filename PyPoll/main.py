#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import dependencies
import os
import csv

#Import pypoll.csv file
pypoll_csv = os.path.join("Documents","python_challenge","python_challenge","PyPoll", "Resources", "election_data1.csv")


# In[2]:


# Initialize null lists
voter_ids = []
countys = []
candidates = []


# In[3]:


# Read in the CSV file
with open(pypoll_csv) as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    #Read the header row
    csv_header = next(csvreader)

    # Loop through columns, adding data from csv to lists after header
    for row in csvreader:
        
        voter_ids.append(int(row[0]))
        countys.append(str(row[1]))
        candidates.append(str(row[2])) 


# In[4]:


# Total votes can be found by using len to find length of voter_id list
total_votes = len(voter_ids)


# In[5]:


# List created to specify unique candidates for dictionary
unique_candidates = ["Khan", "Correy", "Li", "O'Tooley"]


# In[6]:


# Votes per candidate can be found using count to tally up total votes for each candidate
votes_khan = candidates.count("Khan")
votes_correy = candidates.count("Correy")
votes_li = candidates.count("Li")
votes_otooley = candidates.count("O'Tooley")

votes_list = [votes_khan, votes_correy, votes_li, votes_otooley]


# In[7]:


# Percentage of votes can be found by dividing votes_per_candidate by total_votes, multiplied by 100
khan_percent = round((votes_khan / total_votes) * 100)
correy_percent = round((votes_correy / total_votes) * 100)
li_percent = round((votes_li / total_votes) * 100)
otooley_percent = round((votes_otooley / total_votes) * 100)


# In[8]:


# Create percents list in order to find winner
percents = [khan_percent,correy_percent,li_percent,otooley_percent]


# In[9]:


# Zip candidate_list and votes_per_candidate list together for final output
a_zip = zip(unique_candidates,votes_list)
zipped_dict = dict(a_zip)


# In[10]:


# Add values in correct order to zipped_dict for final output
zipped_dict['Khan'] = khan_percent, votes_khan
zipped_dict['Correy'] = correy_percent,votes_correy
zipped_dict['Li'] = li_percent,votes_li
zipped_dict["O'Tooley"] = otooley_percent,votes_otooley


# In[11]:


# Create function to print dictionary for final output
def print_txt ():
    for key, value in zipped_dict.items():
        print(key, ':', value)
        continue


# In[12]:


# Find max percent within percents list to determine winner
max_percent = max(percents)


# In[13]:


# Use index to determine candidate with max percent of votes
winner_index = percents.index(max_percent)
winner = candidates[winner_index]


# In[35]:


# open & write txt to pypoll_results.txt
with open ("pypoll_results.txt", "w") as file:
    file.write("Election Results" + "\n") 
    file.write("------------------------------------"+ "\n")
    file.write(f"Total Votes: {total_votes} \n")
    file.write("------------------------------------"+ "\n")
    file.write(f"Khan: {khan_percent}% ({votes_khan}) \n")
    file.write(f"Correy: {correy_percent}% ({votes_correy}) \n")
    file.write(f"Li: {li_percent}% ({votes_li}) \n")
    file.write(f"O'Tooley: {otooley_percent}% ({votes_otooley}) \n")
    file.write("------------------------------------"+ "\n")
    file.write(f"Winner: {winner} \n")
    file.write("------------------------------------"+ "\n")


# In[36]:


file = open("pypoll_results.txt", "r")
print(file.read())

# close txt file

