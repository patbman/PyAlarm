import time
import subprocess
blah = False


while blah == False:
	
	now = time.localtime()
	
	if now.tm_wday == 3:
			subprocess.call(["screen", "-S", "pandora", "pianobar"])

                        blah = True

	if now.tm_wday == 0:
		if now.tm_hour == 10:

			subprocess.call(["screen", "-S", "pandora", "pianobar"])
	
			blah = True

	if now.tm_wday == 1 or 3:
		if now.tm_hour == 6:

			subprocess.call(["screen", "-S", "pandora", "pianobar"])
			
			blah = True
				
	if now.tm_wday == 2 or 4:
		if now.tm_hour == 7:
			if now.tm_min == 30:
				subprocess.call(["screen", "-S", "pandora", "pianobar"])
				
				blah = True
#Made By Patrick Bowden
