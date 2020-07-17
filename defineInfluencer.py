kolRoster = []

# TODO
#
# Add "adcommScore" function
# Add Pinterest, blogs, tiktok


class Influencer:
    '''This initialises the attributes and methods required to 
    turn the csv input data into the useful csv output data.'''
    def __init__(self, name, gender, snsPlatform, followers, trueReach, absEng, percEng, influence, emv, monthlyPosts):
        self.name = name
        self.gender = gender
        self.snsPlatform = snsPlatform
        self.followers = followers
        self.trueReach = trueReach
        self.absEng = absEng
        self.percEng = percEng
        self.influence = influence
        self.emv = emv
        self.monthlyPosts = monthlyPosts

        # Non-argument attributes go here
        self.status = None
        self.basicRate = None
        self.basicCost = None
        self.reachRate = None
        self.EngRate = None
        self.KlearEngScore = None
        self.KlearReachScore = None
        self.EngScore = None
        self.ReachScore = None
        self.rateDict = {"Facebook" :   [2.5], # {"Platform": [Platform rate, Average Platform followers]}
                        "Instagram" :   [1], 
                        "Twitter"   :   [0.2], 
                        "YouTube"   :   [2], 
                        "Snapchat"  :   [1],
                        "Multi"     :   [1]}

        # Set non-argument attributes (Should I add self.setCost here or is it fine nestled inside self.setRate)
        self.influencerClassification()
        self.setBasicRate()
        self.setReachRate()
        self.setEngRate()
        self.setKlearEngScore()
        self.setKlearReachScore()
        self.setEngScore()
        self.setReachScore()

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

    def setBasicRate(self): 
        '''Set rate per follower in yen based on platform using a dictionary.'''
        for word in self.rateDict:
            if word == self.snsPlatform:
                self.basicRate = self.rateDict[word][0]
        self.setBasicCost()

    def setBasicCost(self):
        '''Set cost per post based on rate and followers.'''
        self.basicCost = int(self.basicRate * self.followers)

    def setReachRate(self):
        '''Sets the cost per impression based on true reach and EMV'''
        self.reachRate = int(100*self.emv/self.trueReach)/100

    def setEngRate(self):
        '''Sets the cost per engagement based on absEng and EMV'''
        self.EngRate = int(100*self.emv/self.absEng)/100

    def setKlearEngScore(self):
        '''Sets the Ad-comm score based on Klear's Influence, absEng, and EMV'''
        self.KlearEngScore = int(1000*self.influence*self.absEng/self.emv)/1000

    def setKlearReachScore(self):
        '''Sets the Ad-comm score based on Klear's Influence, trueReach, and EMV'''
        self.KlearReachScore = int(1000*self.influence/self.reachRate)/1000

    def setEngScore(self):
        '''Sets the Ad-comm score based on Klear's Influence, absEng, and basicCost'''
        self.EngScore = int(1000*self.influence*self.absEng/self.basicCost)/1000

    def setReachScore(self):
        '''Sets the Ad-comm score based on Klear's Influence, trueReach, and basicCost'''
        self.ReachScore = int(1000*self.influence/self.basicRate)/1000


    # Sets the default return value of the print(Influencer)
    def __str__(self):
        '''This returns the string name of an influencer when calling e.g. print(Influencer) instead of returning object.'''
        return self.name

    # Final class method to append instances to Roster array
    def appendInfluencer(self):
        '''Simple method used to append each new influencer to the global Roster.'''
        kolRoster.append(self) # CSV METHOD