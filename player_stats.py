import csv
import pandas as pd

df = pd.read_csv("innings1.csv" )
matches = df.match.unique()
players = {}
bowlers = {}
for i in matches:
  ndf = pd.DataFrame(df[df['match'] == i])
  ndf = ndf.rename(columns=lambda x:x.strip())
  for x in ndf.batsman.unique():
    if x not in players.keys():
      players[x] = ndf[ndf['batsman'] == x]['runs_batsman'].sum()
    else:
      players[x] = players[x] + ndf[ndf['batsman'] == x]['runs_batsman'].sum()
  for y in ndf[ndf.wicket_kind.notnull() & (ndf['wicket_kind'] != 'run out')].bowler.unique():
    if y not in bowlers.keys():
      bowlers[y] = 1
    else:
      bowlers[y] = bowlers[y] + len(ndf[ndf.wicket_kind.notnull() & (ndf['wicket_kind'] != 'run out') & (ndf['bowler'] == y)])
    if y == "V Sehwag":
      print ndf[ndf.wicket_kind.notnull() & (ndf['wicket_kind'] != 'run out') & (ndf['bowler'] == y)]
      #print bowlers[y]
#print players
print bowlers
