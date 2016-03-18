# ShowMeEnglish Scripts and content management system
# Features now
# 1. search through stored subtitles(srt files), X
# 2. search by each tv series, seasons
# 3. search and present words in sentences and episodes
# 4. print the results as txt files
# 5. able to determine the how many lines are presented
# 6. able to search phrases and words separately
# 7. able to search a lists of words


# Features to add
# create a data base version instead of storing files in the os
# able to search by each multiple series or seasons
# able to search from multiple episodes
# able to choose different stems, or  
# able to list out terms that users don't wanna search
# make a web application version allow users to sign up and log in and search through their favorite tv seires

import glob
import linecache
import fnmatch
import os
import re
from search_functions import scope,check_words,text_is_word,check_phrases
#search in one or serveral specific tv series
counter = 0 
while counter == 0:
	text = raw_input('Hi!!\nLooking for a word?\n> ').lower()
	#if there are multiple words
	result_list = []
	if re.findall(r',',text):
		text = re.split(r',+',text.lower())
	#for windows
	# os_path = 'C:\Users\Frank/Desktop/ScriptSearch'
	#for linux=
	os_path = '/home/frank/Dropbox/ScriptSearch/'
	series = ["How I Met Your Mother", 
			  "The Big Bang Theory",
			  "Game of Thrones",
			  "House of Cards",
			  "Breaking Bad",
			  "Mad Men",
			  "Suits",
			  "The Newsroom",
			  "Sex and the City"
			  ]
	pick_series = int(raw_input('Search in a TV Show? Pick a number or type 99 to search in multiple series.\
		\n0.ALL\n1.How I Met Your Mother\n2.The Big Bang Theory\
		\n3.Game of Thrones\n4.House of Cards\n5.Breaking Bad\
		\n6.Mad Men\n7.Suits\n8.The Newsroom\n9.Sex and the City\n> '))

	#three different scopes, 
	#1.pick a tv show and a season and search through them
	files = scope(os_path,series,pick_series)
	if type(text)  ==  str:
		check_words(files,text,counter,result_list)
	elif type(text) == list:
		for t in text:
			check_words(files,t,counter,result_list)

	