li = ["sachin cricket", "Federer tennis", "Nadal tennis", "virat cricket", "Messi football"]


'''out = {"cricket": ["sachin", "virat"], "tennis": ["federer", 'nadal'], 
"football": ['Messi']}'''

players_dict = {}

for i in li:
    import pdb; pdb.set_trace()
    sport = i.split() # ['sachin', 'cricket']
    if sport[1] not in players_dict:
        players_dict[sport[1]] = []  #{'cricket': []}
    players_dict[sport[1]].append(sport[0])

print(players_dict)
