import csv
from datetime import datetime

from optKOLs import kolRoster


# CSV HEADERS
headers = ["Name", 
            "Gender", 
            "Intended Platform", 
            "Status",
            "Followers",  
            "Influence",            
            "Effective Audience", 
            "Percentage Engagement", 
            "Basic cost per post(¥)", 
            "Estimated Media Value, EMV(¥)", 
            "Basic rate per follower(¥)", 
            "EMV/Reach(¥)", 
            "EMV/Eng(¥)",
            "EMV Engagement Score", 
            "EMV Reach Score", 
            "Basic Cost Engagement Score", 
            "Basic Cost Reach Score",
            "Reach Optimized Post"]

# WRITING FROM IMPORTED CSV TO NEW OUTPUT CSV
with open('KOLPack.csv', 'w', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    for row in kolRoster:
        domain = [  row.name, 
                    row.gender, 
                    row.snsPlatform, 
                    row.status, 
                    row.followers, 
                    row.influence,
                    row.absEng, 
                    row.percEng, 
                    row.basicCost, 
                    row.emv, 
                    row.basicRate, 
                    row.reachRate, 
                    row.EngRate,
                    row.KlearEngScore, 
                    row.KlearReachScore, 
                    row.EngScore, 
                    row.ReachScore,
                    row.ReachOptPost]
        writer.writerow(domain)

# PRINT TO TERMINAL CHECK

timeNow = datetime.now()
print("\nModular/package version export at {t.hour:02}:{t.minute:02}:".format(t=timeNow))
print ("{:<11} {:<7} {:<11} {:<11} {:<11} {:<11} {:<11} {:<9} {:<9} {:<11} {:<11} {:<11}".format(
    "Name", 
    "Gender", 
    "Platform", 
    "Status",
    "Followers",
    "Influence",
    "TrueReach", 
    "AbsEng", 
    "Perc Eng", 
    "BaseCost(¥)", 
    "EMV(¥)", 
    "ReachOptPost"))
for entry in kolRoster:
    print ("{p.name:<11.11} {p.gender:<7} {p.snsPlatform:<11} {p.status:<11} {p.followers:<11} {p.influence:<11} {p.trueReach:<11} {p.absEng:<9} {p.percEng:<9} {p.basicCost:<11} {p.emv:<11} {p.ReachOptPost}".format(p=entry))

print()