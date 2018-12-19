import subprocess

# employs system speaker to speak
def say(text):
	subprocess.call(['say',text])