# Open up the file nbasalaries.csv
salaries_file = open("nbasalaries.csv",'r')
#{}=dictionary
teams={}
for line in salaries_file:
    player_data = line.split(',')
    player_name = player_data[0]
    player_team=player_data[1]
    salary=int(player_data[2])
    if player_team in teams.keys():
        teams[player_team] += salary
    else:
        teams[player_team] = salary

print teams.keys()
for w in sorted(teams,key=teams.get,reverse=True):
    print w, teams[w]
