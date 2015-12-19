# Two and a Half Penned
#
# Project by Matthew Bowden and Logan Pendergrass
# For further documentation see README.md

#import section
import twitter
from random import randint
import sys
reload(sys)
#due to tweet text encoding, default encoder must be changed
sys.setdefaultencoding("ISO-8859-1")

#external file for API keys
execfile("../APIkeys/key.py")

#help("twitter.User.status")
#dumbtest()
#print test

#Defining variables and functions
def setupAPI():
    api = twitter.Api(consumer_key = Ckey,
                      consumer_secret = Csecret,
                      access_token_key = AccKey,
                      access_token_secret = AccSecret)
    return api

def getUserToQuery():
    #For now, this will simply return the userID for Charlie Sheen
    #Eventually this may be made mutable
    return "charliesheen"

def status(statusList, degree = 1):
    #    Function definitions
    #
    #
    #cut the tweet once valid index is found
    def strDel(toDel):
        global tweet
        index = tweet.find(toDel)
        if(index > -1):
            print "Char " + repr(toDel) + " found at: " + str(index)
            tweet = tweet[:index]

    #newline cleaning
    def cleanNewline():
        global tweet
        newlineFlag = False
        while(not newlineFlag):
            if(tweet.endswith("\n") or tweet.endswith(' ')):
                tweet = tweet[:-1]
            else:
                newlineFlag = True

    #determine substring from degree
    #   degree = 1: full tweet is returned
    #   degree = 2: random 'paragraph' is returned (may end up being full tweet)
    #   degree = 3: random line from random paragraph is returned
    def subTweet():
        #internal function for randomly selecting paragraph/line
        def randSelect(newline):
            #finds the indexes of each newline
            numNewline = len(newline)
            global tweet
            start = 0
            breakList = [0] #append starting location
            flag = True
            while(flag):
                temp = tweet.find(newline, start)
                if (temp == -1):
                    breakList.append(len(tweet)) #append ending location
                    flag = False
                else:
                    breakList.append(temp + numNewline) #+2 to skip over newline
                    start = temp+1
                    print repr(newline) + " found at index: " + str(temp)
            print breakList
            count = len(breakList)
            start = randint(0,count-2) #-1 for zero indexed list and -1 to avoid string end as starting point
            print "Random selection: " + str(start + 1)
            tweet = tweet[breakList[start]:breakList[start+1]] #should return the portion of the string requested
            cleanNewline()

        #subTweet executed code
        global tweet
        if(degree == 1): #full tweet selected
            return
        else: #if degree is 2+
            randSelect('\n\n') #select random paragraph
            if(degree == 2):
                return
            else: #if degree is 3+
                randSelect('\n') #select random line
                if(degree == 3):
                    return
                elif(degree == 4):
                    randSelect(' ') #select random word
                    return

    #    Executed code
    #
    #find random tweet
    length = len(statusList)
    rand = randint(0,(length-1))
    global tweet
    tweet = statusList[rand].text
    print "Length: " + str(length)
    print "Random Number: " + str(rand)
    print "\nStripped Tweet: "

    #clean random tweet
        #Charlie has a lot of extra crap in his tweets
        #(copyrights, 'x', twitter links, etc)
        #This function will strip most of that away
        #NOTE: One trend I've found is that he includes all of his links
        #   and hashtags after the copyright symbol. Perhaps making
        #   a substring of everything up to the symbol will cut out a
        #   good deal. Then check after for his 'signature'.
    #Char cleaning
    strDel('\nx')
    strDel('xox')
    strDel('\xa9')
    cleanNewline()
    print "Double newline found at index: " + str(tweet.find('\n\n'))
    print tweet

    #determine tweet substring
    def scopetest():
        print "Degree is: " + str(degree)
    scopetest()
    subTweet()
    print tweet

api = setupAPI()
user = getUserToQuery()
timeline = api.GetUserTimeline(screen_name=user,count=20,include_rts=False)
print [t.GetText() for t in timeline]
#print timeline[0].text
status(timeline, 3)
print "EOT"