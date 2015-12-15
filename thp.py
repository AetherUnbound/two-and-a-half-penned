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

def strDel(toDel, delFrom):
    if(toDel > -1):
        print "Char found at: " + str(toDel)
        #delFrom = delFrom[:toDel]
        return True
    else:
        return False

def stripTweet(tweet):
    #Charlie has a lot of extra crap in his tweets
    #(copyrights, 'x', twitter links, etc)
    #This function will strip most of that away
    #NOTE: One trend I've found is that he includes all of his links
    #   and hashtags after the copyright symbol. Perhaps making
    #   a substring of everything up to the symbol will cut out a
    #   good deal. Then check after for his 'signature'.

    #Char cleaning
    xIndex = tweet.find('\nx')
    xoxIndex = tweet.find('xox')
    cIndex = tweet.find('\xa9')
    #'x' cleaning
    if(strDel(xIndex, tweet)):
        tweet = tweet[:xIndex]
    #'xox' cleaning
    elif(strDel(xoxIndex,tweet)):
        tweet = tweet[:xoxIndex]
    # copyright cleaning
    elif(strDel(cIndex, tweet)):
        tweet = tweet[:cIndex]
    #end of string newline cleaning
    newlineFlag = False
    while(not newlineFlag):
        if(tweet.endswith("\n")):
            tweet = tweet[:-1]
        else:
            newlineFlag = True
    print "Double newline found at index: " + str(tweet.find('\n\n'))
    print tweet

def status(statusList, degree = 1):
    length = len(statusList)
    rand = randint(0,(length-1))
    tweet = statusList[rand].text
    print "Length: " + str(length)
    print "Random Number: " + str(rand)
    #print "Text output: \n" + tweet
    print "\nStripped Tweet: "
    stripTweet(tweet)

api = setupAPI()
user = getUserToQuery()
timeline = api.GetUserTimeline(screen_name=user,count=10,include_rts=False)
print [t.GetText() for t in timeline]
#print timeline[0].text
status(timeline)
print "EOT"