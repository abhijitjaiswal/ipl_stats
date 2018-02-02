#Author: Abhijit Jaiswal
# This script parses the yaml files and creates a master file innings1.csv for all ball by ball details for all the matches 

import yaml
import csv
import glob

y = glob.glob("/Users/abhijitj/Downloads/ipl1/*.yaml")
print y
#filename = "501200.yaml"
csv_file = "innings1.csv"
with open(csv_file, "w") as csv:
 columnTitleRow = "match, innings, deliveries, batsman, bowler, runs_batsman, runs_total, runs_extra,extra_type, non_striker, wicket_fielders, wicket_kind, wicket_player_out\n"
 csv.write(columnTitleRow)

out = []
for f in y:
  fname = f.split("/")[-1].split(".")[0]
  print fname
  with open(f, 'r') as stream:
    try:
      d = yaml.load(stream)
    except yaml.YAMLError as exc:
      print(exc)

    #fields = [innings, deliveries, batsmen, bowler, runs_batsmen, runs_total, runs_extra, 
    #	extra_type, non_striker, wicket_fielders, wicket_kind, wicket_player_out]
    
    if "innings" in d.keys():
      for inn in range(0, len(d['innings'])):
        innings = d['innings'][inn].keys()[0]   # fields[0] assigned
        #print inn
        #print innings
        for i in range(0, len(d['innings'][inn][innings]['deliveries'])):
          #print i
          deliveries = d['innings'][inn][innings]['deliveries'][i].keys()[0]
          batsman = d['innings'][inn][innings]['deliveries'][i][deliveries]['batsman']
          bowler = d['innings'][inn][innings]['deliveries'][i][deliveries]['bowler']
          runs_batsman = d['innings'][inn][innings]['deliveries'][i][deliveries]['runs']['batsman']
          runs_total = d['innings'][inn][innings]['deliveries'][i][deliveries]['runs']['total']
          runs_extra = d['innings'][inn][innings]['deliveries'][i][deliveries]['runs']['extras']
          if runs_extra > 0:
            extra_type = d['innings'][inn][innings]['deliveries'][i][deliveries]['extras'].keys()[0]
          else:
            extra_type = ""
          non_striker = d['innings'][inn][innings]['deliveries'][i][deliveries]['non_striker']
          if 'wicket' in d['innings'][inn][innings]['deliveries'][i][deliveries].keys():
            if 'fielders' in d['innings'][inn][innings]['deliveries'][i][deliveries]['wicket'].keys():
              wicket_fielders = "-".join(d['innings'][inn][innings]['deliveries'][i][deliveries]['wicket']['fielders'])
            else:
              wicket_fielders = ""
            wicket_kind = d['innings'][inn][innings]['deliveries'][i][deliveries]['wicket']['kind']
	    wicket_player_out = d['innings'][inn][innings]['deliveries'][i][deliveries]['wicket']['player_out']
          else:
            wicket_fielders = ""
            wicket_kind = ""
            wicket_player_out = ""
          print (fname, innings, deliveries, batsman, bowler, runs_batsman, runs_total, runs_extra, 
            extra_type, non_striker, wicket_fielders, wicket_kind, wicket_player_out)
          out.append([fname, innings, str(deliveries), batsman, bowler, str(runs_batsman), str(runs_total), str(runs_extra), 
            extra_type, non_striker, wicket_fielders, wicket_kind, wicket_player_out])

csv = open(csv_file, "a")
#columnTitleRow = "innings, deliveries, batsman, bowler, runs_batsman, runs_total, runs_extra,extra_type, non_striker, wicket_fielders, wicket_kind, wicket_player_out\n"
#csv.write(columnTitleRow)
for i in out:
  print i
  row = ",".join(i)+"\n"
  csv.write(row)
