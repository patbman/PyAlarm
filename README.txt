This is a alarm clock that I made in python I have only tested it on Linux machines what it does is that if you have a internet connection it will wake you up with your pandora station but if you don't have a connection it will just play tracks from a library that you set.

dependancies 

to make this work you will need to install screen pianobar and python easily by doing by running sudo apt-get install screen pianobar python

once that is done quickly edit both clock.py and localclock.py to have the days (below is the guide on how python reads days) and times you would like the alarm to go off

on localclock.py you will also need to set where the local music files that you want to be woken up to the format for editing the location looks the same as if you are changing directories that have spaces so if there is a space put a backslash them the space

this\ is\ a\ test\ to\ show\ the\ formating\

to setup pianobar do

nano ~/.config/pianobar/config

change the username "user" in event_command to suit your system and change 123456 in autostart_station to the station you want to be woken up to 

you can find the ID of the station by going over to your browser and going to pandora.com and click on the desired station and the list of digits after play in the url is what you want to insert

tls_fingerprint = 2D0AFDAFA16F4B5C0A43F3CB1D4752F9535507C0
user = myemail@mail.com
password = mypassword
event_command = /home/user/.config/pianobar/eventcommand.sh
autostart_station = 123456

then run this command

cd ~/.config/pianobar && wget http://raspberrypiserver.no-ip.org/eventcommand.sh && chmod +x eventcommand.sh && mkfifo ctl

once that is finished test to see if every thing works by running the pianobar

if you would like to control pianobar with your android phone in order to say stop it when the alarm goes off you just need to download the app at this link http://raspberrypiserver.no-ip.org/pianobar_remote.apk and input your information and make sure that ssh is installed on your system and then you are good to go

for people that have IOS you will need to just download any ssh app from the app store and once you are logged into the system you can just run the command screen -X -S pandora kill and that will kill the alarm clock this same procedure can be done on android as well you can also use the ssh app to start the alarm clock

once all your settings are set all you have to do is run the command ./alarm.sh what this will do is check to see if you have a IP address and then if you do it will run clock.py and if you don't it will run localclock.py after the alarm goes off at the time you set it you will need to go and run ./alarm.sh again to start the process over again

Monday = 0

Tuesday = 1

Wednesday = 2

Thursday = 3

Friday = 4

Saturday = 5

Sunday = 6

