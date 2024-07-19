import os
import csv
# Path to collect data from the Resources folder
election_csv = os.path.join("Resources", "election_data.csv")
election_txt = os.path.join("analysis", "election_analysis.txt")
candidate_list = []
candidate_votes = {}
total_votes = 0
winning_candidate = ""
winning_count = 0


with open(election_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    header = next(csv_reader)

    for row in csv_reader:
        candidate_name = row[2]
        total_votes += 1
        if candidate_name not in candidate_list:
            candidate_list.append(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
with open(election_txt,"w") as txt_file:
    election_results =(
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n")
    print(election_results)
    txt_file.write(election_results)

    for candidate in candidate_votes:
        votes = candidate_votes.get(candidate)
        vote_percentage = float(votes)/float(total_votes)*100
        if (votes > winning_count):
            winning_count = votes
            winning_candidate = candidate
        voter_output =(f"{candidate}: {vote_percentage:.3f}% ({votes})\n")
        print(voter_output)
        txt_file.write(voter_output)

    winning_candidate_summary = (f"-------------------------\n"
                f"Winner: {winning_candidate}\n"
                f"-------------------------")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)