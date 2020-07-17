import csv
import json
import os
import sys

# --------NOTES--------
# Estimated cost in ¥ per 1M Reach as benchmark:
# Facebook      Insta       Twitter     YouTube     Snapchat    Blog
# 2,500,000     1,000,000   200,000     2,000,000   1,000,000   6,000,000

# --------TO DO LIST--------
# add LinkedIn, Pinterest, TikTok
# 

# ***


# --------MAIN FUNCTIONS DEFINITIONS--------


# ***

# INITIALISE TOTAL LIST OF INFLUENCERS AND THEIR COST
newRoster = []
csvRoster = []

# DEFINING CLASS OF INFLUENCER
class Influencer:
    '''This initialises the attributes and methods required to 
    turn the csv input data into the useful csv output data.'''
    def __init__(self, name, sex, followers, engagement, snsPlatform, posts, weeklyPosts, selected):
        self.name = name
        self.sex = sex
        self.followers = followers
        self.engagement = engagement
        self.snsPlatform = snsPlatform
        self.posts = posts
        self.weeklyPosts = weeklyPosts
        self.selected = selected

        # Non-argument attributes go here
        self.status = None
        self.rate = None
        self.cost = None
        self.effAudience = None
        self.rateDict = {"Facebook" :   [2.5, 100], 
                        "Instagram" :   [1, 100], 
                        "Twitter"   :   [0.2, 100], 
                        "Youtube"   :   [2, 100], 
                        "Snapchat"  :   [1, 100]}

        # Set non-argument attributes (Should I add self.setCost here or is it fine nestled inside self.setRate)
        self.influencerClassification()
        self.setRate()
        self.setEffAudience()

        # Append Influencer to Roster
        self.appendInfluencer()


    # SET CLASS METHODS
    def influencerClassification(self):
        '''Defines the status of an influencer based on their follower count.'''
        status = ("Mega", "Macro", "Mid-Tier", "Micro", "Nano", "Pico")
        if self.followers >= 1e6:
            self.status = status[0]
        elif 1e6 > self.followers >= 5e5:
            self.status = status[1]
        elif 5e5 > self.followers >= 5e4:
            self.status = status[2]
        elif 5e4 > self.followers >= 1e4:
            self.status = status[3]
        elif 1e4 > self.followers >= 1e3:
            self.status = status[4]
        elif 1e3 > self.followers:
            self.status = status[5]

    def setRate(self): 
        '''Set rate per follower in yen based on platform using a dictionary.'''
        for word in self.rateDict:
            if word == self.snsPlatform:
                self.rate = self.rateDict[word][0]
        self.setCost()

    def setCost(self):
        '''Set cost per post based on rate and followers.'''
        self.cost = int(self.rate * self.followers)

    def setEffAudience(self):
        '''Set the effective audience based on followers and engagement.'''
        self.effAudience = int(self.followers * self.engagement/100)

    def __str__(self):
        '''This returns the string name of an influencer when calling e.g. print(Influencer) instead of returning object.'''
        return self.name

    # Final class method to append instances to Roster array
    def appendInfluencer(self):
        '''Simple method used to append each new influencer to the global Roster.'''
        newRoster.append(self) # NEW METHOD
        csvRoster.append(self) # CSV METHOD

# ***


# --------READING AND WRITING TO CSV--------


# ***

# READING FROM CSV FILE
with open('/Users/bolglo/Documents/VSC/python/KOL_Selection_Pack/KOL_Initialisation.csv', 'r') as file: #consider newline='' and dialect='excel' for later editions
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        newInfluencer = Influencer(row[0], row[1], int(row[2]), float(row[3]), row[4], int(row[5]), float(row[6]), row[7])


# WRITING TO CSV

# CSV HEADERS
headers = ["Name", "Sex", "Platform", "Followers", "Effective Audience", "Status", "Rate per follower", "Cost per post", "Selected"]

# WRITING FROM IMPROVED ARRAY
with open('KOL_SelectionNew.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    for row in newRoster:
        domain = [row.name, row.sex, row.snsPlatform, row.followers, row.effAudience, row.status, row.rate, row.cost, row.selected]
        writer.writerow(domain)

# WRITING FROM IMPORTED CSV TO NEW OUTPUT CSV
with open('newKOL_Selection.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    for row in csvRoster:
        domain = [row.name, row.sex, row.snsPlatform, row.followers, row.effAudience, row.status, row.rate, row.cost, row.selected]
        writer.writerow(domain)

# ***


#------------------ TERMINAL PRINT CHECK


# ***

print()

# Terminal print check - Placeholder
print("Self contained version:")
print ("{:<11} {:<11} {:<11} {:<11} {:<11} {:<11} {:<11} {:<11} {:<11}".format("Name", "Sex", "Platform", "Followers", "Eff Aud", "Status", "Rate", "Cost", "Selected"))
for entry in newRoster:
    print ("{p.name:<11} {p.sex:<11} {p.snsPlatform:<11} {p.followers:<11} {p.effAudience:<11} {p.status:<11} {p.rate:<11} {p.cost:<11} {p.selected:<11}".format(p=entry))

print()