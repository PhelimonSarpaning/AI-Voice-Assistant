import speech_recognition as sr
import say
import os
import commands
import google
# gets the mic ready and also allow the hardware to recognize voice
r = sr.Recognizer()
mic = sr.Microphone()
# google.search_google("sharida holloway")

say.say("Hey, what should I do?")
# d = '/Applications'
# app = 'Messages'
# os.system('open ' +d+'/%s.app' %app.replace(' ','\ '))

# wake up call tp Voice Assistant
def call_assistant(phrase = 'Maame'):
	if text.lower() == phrase:
		return True
		print(text)
	else:
		return False
		print(text)
	print(text)
# ensures user keeps talking and speech is picked up
# and checks to see if user mentions name of Voice Assistant to ensure a conversation start
while True:
	with mic as source:
				r.adjust_for_ambient_noise(source, duration=0.5)
				audio = r.listen(source)
				text = r.recognize_houndify(audio,"ZNksyHa1eV8uu1wUq7Pbaw==",
				"_vz7PYsu2wLYqYXsmaLJOni5yZhBnxqDqWVv-zLqyPXa7GOGy7QFlbq0Y_3OwROgeWQdPXG5W6GNctL2loWGAQ==")
				print(text)
	if call_assistant() == True:
		try:
			say.say("Phelimon, How can I help you?")
			with mic as source:
				r.adjust_for_ambient_noise(source)
				audio = r.listen(source)
				transcript = r.recognize_houndify(audio,"ZNksyHa1eV8uu1wUq7Pbaw==",
				"_vz7PYsu2wLYqYXsmaLJOni5yZhBnxqDqWVv-zLqyPXa7GOGy7QFlbq0Y_3OwROgeWQdPXG5W6GNctL2loWGAQ==")
				print(transcript)
				# checks to see if user wants to search google
				phrase = " search "
				if phrase in transcript.lower():
					find = transcript.lower().split(phrase)[-1]
					search_google(find)
					say.say("I am searching for the results on Google..hangon")
				# then channels to open apps on phone
				else:
					sys_command = commands.search_es(transcript)
			    	print(sys_command)
			    	os.system(sys_command)
			    	say.say("I am opening the application for you...hang on")
				# else:
				# 	print("I don't understand what you're saying come again")

				
		except:
			pass
	else:
		pass
