# visitorDetector
This is a set of scripts and protocols to alert everyone in the Emory Tech Lab when a visitor enters the space. It is designed to run off a Raspberry Pi, currently running on Raspberry Pi 2 B



To open manually, in terminal, navigate to this directory and type

	python pi_surveillance.py

To exit, ctrl c

To modify its automatic opening:

Go to home directory:

	cd ~
Open the .bashrc file with admin rights:

	sudo nano .bashrc 

At the bottom of the file is says 

	sh launcher.sh &

This lets us know that on launch it will open the launcher.sh file in the same directory using shell and will continue booting while it does.


In the launcher.sh file we have:

	#!bin/sh

	#launcher.sh

	python /home/pi/visitorDetector/motionDetect.py

What that does is it opens the file motionDetect (the main file) in the visitorDetector directory with python.
