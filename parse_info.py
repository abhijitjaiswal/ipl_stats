import yaml
import csv
import glob

y = glob.glob("/Users/abhijitj/Downloads/ipl1/*.yaml")
#filename = "501200.yaml"
csv_file = "info2.csv"
with open(csv_file, "w") as csv:
 columnTitleRow = "match, city, season, dates, match_type, venue, team1, team2, umpire1, umpire2, toss_winner, toss_decision, player_of_match, outcome_winner, result, win_by_runs, win_by_wickets, overs\n"
 csv.write(columnTitleRow)

out = [] 
for f in y:
  print f
  fname = f.split("/")[-1].split(".")[0]  
  with open(f, 'r') as stream:
    try:
      d = yaml.load(stream)
    except Exception as e:
      print(e)
  if "city" in d['info'].keys():
    city = d['info']['city']
  else:
    city = ""
  if "dates" in d['info'].keys():
    dates = d['info']['dates'][0]
    dates = dates.strftime('%d/%m/%Y')
    season = str(dates).split("/")[2]
  else:
    dates = ""
  if "match_type" in d['info'].keys():
    match_type = d['info']['match_type']
  else:
    match_type = ""
  if "venue" in d['info'].keys():
    venue = d['info']['venue'].replace(",", "")
  else:
    venue = ""
  if "teams" in d['info'].keys():
    team1 = d['info']['teams'][0]
    team2 = d['info']['teams'][1]
  else:
    team1 = ""
    team2 = ""
  if "umpires" in d['info'].keys():
    umpire1 = d['info']['umpires'][0]
    umpire2 = d['info']['umpires'][1]
  else:
    umpire1= ""
    umpire2 = ""
  if "toss" in d['info'].keys():
    toss_winner = d['info']['toss']['winner']
    toss_decision = d['info']['toss']['decision']
  else:
    toss_winner = ""
    toss_decision = ""
  if "player_of_match" in d['info'].keys():
    player_of_match = d['info']['player_of_match'][0]
  else:
    player_of_match = ""
  if "winner" in d['info']['outcome'].keys():
    outcome_winner = d['info']['outcome']['winner']
    result = d['info']['outcome']['winner']
    if "runs" in d['info']['outcome']['by'].keys():
      win_by_runs = d['info']['outcome']['by']['runs']
    else:
      win_by_runs = ""
    if "wickets" in d['info']['outcome']['by'].keys():
      win_by_wickets = d['info']['outcome']['by']['wickets']
    else:
      win_by_wickets = ""
  else:
    outcome_winner = ""
    result = d['info']['outcome']['result']
    win_by_runs = ""
    win_by_wickets = ""
  if "overs" in d['info'].keys():
    overs = d['info']['overs']
  else:
    overs = ""
  #print [fname, city, dates, match_type, venue, team1, team2, umpire1, umpire2, toss_winner, toss_decision, player_of_match, outcome_winner, win_by_runs, win_by_wickets, overs]
  out.append([fname, city, season, dates, match_type, venue, team1, team2, umpire1, umpire2, toss_winner, toss_decision, player_of_match, outcome_winner, result, str(win_by_runs), str(win_by_wickets), str(overs)])

with open(csv_file, "a") as csv:
  for i in out:
    print i
    row = ",".join(i)+"\n"
    csv.write(row)
"""

with open("/Users/abhijitj/Downloads/ipl1/"+filename, 'r') as stream:
  try:
    d = yaml.load(stream)
  except yaml.YAMLError as exc:
    print(exc)

#fields = [innings, deliveries, batsmen, bowler, runs_batsmen, runs_total, runs_extra, 
#	extra_type, non_striker, wicket_fielders, wicket_kind, wicket_player_out]

out = []
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
          wicket_fielders = ",".join(d['innings'][inn][innings]['deliveries'][i][deliveries]['wicket']['fielders'])
        else:
          wicket_fielders = ""
        wicket_kind = d['innings'][inn][innings]['deliveries'][i][deliveries]['wicket']['kind']
	wicket_player_out = d['innings'][inn][innings]['deliveries'][i][deliveries]['wicket']['player_out']
      else:
        wicket_fielders = ""
        wicket_kind = ""
        wicket_player_out = ""
      print (innings, deliveries, batsman, bowler, runs_batsman, runs_total, runs_extra, 
            extra_type, non_striker, wicket_fielders, wicket_kind, wicket_player_out)
      out.append([innings, str(deliveries), batsman, bowler, str(runs_batsman), str(runs_total), str(runs_extra), 
            extra_type, non_striker, wicket_fielders, wicket_kind, wicket_player_out])

csv_file = filename.split(".")[0]+"_output.csv"
csv = open(csv_file, "w")
columnTitleRow = "innings, deliveries, batsman, bowler, runs_batsman, runs_total, runs_extra,extra_type, non_striker, wicket_fielders, wicket_kind, wicket_player_out\n"
csv.write(columnTitleRow)
for i in out:
  print i
  row = ",".join(i)+"\n"
  csv.write(row)
"""
