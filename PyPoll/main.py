import os
import csv

csvpath = os.path.join("Documents", "python-challenge", "PyPoll", "Resources1", "election_data.csv")

count = 0

with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    counter_Khan = 0
    c_correy = 0
    li = 0
    tooley = 0

    for row in csv_reader:
        # print(row[0], row[1], row[2])
        if row[2] == str("Khan"):
            counter_Khan = counter_Khan + 1
        if row[2] == str("Correy"):
            c_correy = c_correy + 1
        if row[2] == str("Li"):
            li = li + 1
        if row[2] == str("O'Tooley"):
            tooley = tooley + 1
            
        max_winner = max(counter_Khan, c_correy, li, tooley)
        count = count + 1

    khan_percent = round(int((counter_Khan)/(count - 1)*100), 0)
    tooley_percent = round(((tooley/(count - 1))*100), 0)
    li_percent = round(((li/(count - 1))*100), 0)
    correy_percent = round(c_correy/(count - 1)*100, 0)


    print("Election Results")
    print("-------------------------")  
    print("Total Votes: " + str(count))
    print("-------------------------")
    print("Khan: " + str(khan_percent) + "% " + str(counter_Khan))
    print("Correy: " + str(correy_percent) + "% " + str(c_correy))
    print("Li: " + str(li_percent) + "% " + str(li))
    print("O'Tooley: " + str(tooley_percent) + "% " + str(tooley))
    print("-------------------------")

if counter_Khan > c_correy and counter_Khan > li and counter_Khan > tooley:
    print("Winner: Khan")
if c_correy > counter_Khan and c_correy > li and c_correy > tooley:
    print("Winner: Correy")
if li > c_correy and li > counter_Khan and li > tooley:
    print("Winner: Li")
if tooley > c_correy and tooley > li and tooley > counter_Khan:
    print("Winner: O'Tooley")


output = os.path.join("Documents", "python-challenge", "PyPoll", "analysis", "PyPoll.txt")
with open(output, "w") as analysis:
        analysis.write("Election Results" + "\n")
        analysis.write("---------------------------------" + "\n")
        analysis.write("Total Votes: " + str(count) + "\n")
        analysis.write("-------------------------" + "\n")
        analysis.write("Khan: " + str(khan_percent) + "% " + str(counter_Khan) + "\n")
        analysis.write("Li: " + str(li_percent) + "% " + str(li) + "\n")
        analysis.write("Correy: " + str(correy_percent) + "% " + str(c_correy) + "\n")
        analysis.write("O'Tooley: " + str(tooley_percent) + "% " + str(tooley))