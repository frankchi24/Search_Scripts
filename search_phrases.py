import glob
import linecache
import fnmatch
import os
import re
from search_functions import scope,check_words,text_is_word,check_phrases

counter = 0 
while counter == 0:
	result_list = []
	text = raw_input('Hi!!\nLooking for a phrase?\n> ').lower()
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
	check_phrases(files,text,counter,result_list)
	#create a txt file with the results