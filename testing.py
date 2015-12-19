import twitter
import pyttsx

#help("twitter.Api.GetUserTimeline")
#help("twitter.Status")

engine = pyttsx.init()
#engine.say('Greetings!')
#engine.say('How are you today?')
#engine.say("Hey logan you stupid fuck face I am gaybot")
#engine.runAndWait()

#help("pyttsx.voice")
voices = engine.getProperty('voices')
#for voice in voices:
#   engine.setProperty('voice', voice.id)
#   print "Current voice id: " + voice.id
engine.setProperty('voice', 'english')
engine.setProperty('rate', 150)
engine.say("The quick brown fox jumped over the lazy dog")
engine.runAndWait()