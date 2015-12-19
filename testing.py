import twitter
import pyttsx

#help("twitter.Api.GetUserTimeline")
#help("twitter.Status")

engine = pyttsx.init()
engine.say('Greetings!')
engine.say('How are you today?')
engine.runAndWait()