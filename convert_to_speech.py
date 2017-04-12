#!/usr/bin/env python
import pyttsx , os , signal
os.system("python twi.py");

def handler(signal , frame) :
        print "Cleanup"
        sys.exit(0)

signal.signal(signal.SIGINT , handler) #ctrl+C SIGINIT
signal.signal(signal.SIGTSTP , handler) #ctrl+Z SIGTSTP
signal.signal(signal.SIGTERM, handler) 

engine = pyttsx.init()
file = open("kcoddict_tweets.csv",'r')
alllines = file.readlines()
file.close()
for eachline in alllines :
	eachline = "the date is " + eachline
	print eachline
	rate = engine.getProperty('rate')
	engine.setProperty('rate',rate-50)
	engine.say(eachline)
engine.runAndWait()
