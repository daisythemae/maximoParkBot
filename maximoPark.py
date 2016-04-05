#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, time, sys, random, os
 
argfile = str(sys.argv[1])
 
#enter the corresponding information from your Twitter application:
CONSUMER_KEY = os.environ['CONSUMER_KEY']
CONSUMER_SECRET = os.environ['CONSUMER_SECRET']
ACCESS_TOKEN = os.environ['ACCESS_KEY']
ACCESS_SECRET =  os.environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)



openfile = open(argfile,'r')
f = openfile.readlines()
openfile.close()
 
for lines in f:
	lines = open(argfile).read().splitlines()
	myline = random.choice(lines)
	api.update_status(status = myline)
	time.sleep(60)#Tweet every minute


