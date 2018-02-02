#Author: Abhijit Jaiswal
#This file parses the information in deliveries.csv and forms batsman.csv and bowlers.csv

import csv

csv_file = "batsman.csv"
with open(csv_file, "w") as c:
  columnTitleRow = "player, opponent, total_runs, striek_rate, ground, win"
  c.write(columnTitleRow)

runs = {}
r=0

bowlers = {}

with open("deliveries.csv", 'rb') as d:
  for line in d.readlines()[1:]:
    if line.split(",")[8] not in runs.keys():
      bowlers[str(line.split(",")[8])] = {}

#f1 = file("matches.csv", "r")
#mat = csv.reader(f1)

with open("deliveries.csv", 'rb') as d:
  #for m in mat.readlines()[1:]:
    #run = int(line.split(",")[15])
    for line in d.readlines()[1:]:
      run = int(line.split(",")[15])
      player = line.split(",")[6]
      b = line.split(",")[8]
      if player not in bowlers[b].keys():
        bowlers[b][player] = {}
        bowlers[b][player]['runs'] = int(run)
        bowlers[b][player]['deliveries'] = 1
        bowlers[b][player]['sr'] = round(float((int(run) / 1))*100.0, 2)
        if line.split(",")[18] == player:
          bowlers[b][player]['wickets'] = 1
      else:
        bowlers[b][player]['runs'] = bowlers[b][player]['runs'] + run
        bowlers[b][player]['deliveries'] = bowlers[b][player]['deliveries'] + 1
        bowlers[b][player]['sr'] = round(float(bowlers[b][player]['runs']) / float(bowlers[b][player]['deliveries'])*100.0, 2)
        if line.split(",")[18] == player:
          if "wickets" in bowlers[b][player].keys():
            bowlers[b][player]['wickets'] = bowlers[b][player]['wickets'] + 1
          else:
            bowlers[b][player]['wickets'] = 1

fields = "bowler,batsman,runs,deliveries,sr,wickets\n"
with open("test_output1.csv", "wb") as w:
  #w = csv.writer(f)
  w.write(fields)
  for k in bowlers.keys():
    print bowlers[k]
    for player in bowlers[k].keys():
        if "wickets" in bowlers[k][player].keys():
          w.write(k+","+ player+","+str(bowlers[k][player]['runs'])+","+str(bowlers[k][player]['deliveries'])+","+str(bowlers[k][player]['sr'])+","+str(bowlers[k][player]['wickets'])+"\n")  
        else:
          w.write(k+","+ player+","+str(bowlers[k][player]['runs'])+","+str(bowlers[k][player]['deliveries'])+","+str(bowlers[k][player]['sr'])+",0\n")

for bw in bowlers.keys():
  if bw == "B Kumar":
    print "###################################################"
    print bw
    print "###################################################"
    print bowlers[bw]


with open("deliveries.csv", 'rb') as d:
  for line in d.readlines()[1:]:
    if line.split(",")[3] not in runs.keys():
      runs[str(line.split(",")[3])] = {}

#f1 = file("matches.csv", "r")
#mat = csv.reader(f1)

with open("deliveries.csv", 'rb') as d:
  #for m in mat.readlines()[1:]:
    #run = int(line.split(",")[15])
    for line in d.readlines()[1:]:
      run = int(line.split(",")[15])
      player = line.split(",")[6]
      team = line.split(",")[3]
      if player not in runs[team].keys():
        runs[team][player] = {}
        runs[team][player]['runs'] = int(run)
        runs[team][player]['deliveries'] = 1
        runs[team][player]['sr'] = round(float((int(run) / 1))*100.0, 2)
      else:
        runs[team][player]['runs'] = runs[team][player]['runs'] + run
        runs[team][player]['deliveries'] = runs[team][player]['deliveries'] + 1
        runs[team][player]['sr'] = round(float(runs[team][player]['runs']) / float(runs[team][player]['deliveries'])*100.0, 2)
        #print "Runs   " + str(runs[team][player]['runs'])
        #print "Deliveries    " + str(runs[team][player]['deliveries'])
        #print "SR   "+  str(float(runs[team][player]['runs']) / float(runs[team][player]['deliveries']))
        """
        r=r+1
        if r> 10:
          break
        """
"""
import operator 
sorted_runs = {}
for i in runs.keys():
  sorted_runs[i] = sorted(runs[i].items(), key=operator.itemgetter(1))


for i in sorted_runs.keys():
  print "##################################################"
  print "##################################################"
  print i
  print "##################################################"
  print "##################################################"
  print sorted_runs[i]
"""
#print runs
#vk=0
#for i in runs.keys():
#  print runs[i]
#  if 'V Kohli' in runs[i]:
#    vk = vk+runs[i]['V Kohli']  
#print vk
