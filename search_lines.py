# ShowMeEnglish Scripts and content management system
# Features now
# 1. search through stored subtitles(srt files), X
# 2. search by each tv series, seasons
# 3. search and present words in sentences and episodes
# 4. print the results as txt files
# 5. able to determine the how many lines are presented

# Features to add
# able to search by each multiple series or seasons or episodes
# able to search phrases and words separately
# able to choose different stems, or search a lists of words 
import glob
import linecache
import fnmatch
import os
import re
from check_words import scope,check_lines_in_files
#search in one or serveral specific tv series
counter = 0  
while counter == 0:
	text = raw_input('Hi!!\nLooking for a phrase or word?\n> ').lower()
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
	result_list = []			
	check_lines_in_files(files,text,counter,result_list)
	#create a txt file with the results
	if counter > 0:
		result_fiename = text + ".txt"
		make_files =  int(raw_input("Do you wanna print the results out as txt files?\n1.Yes\n2.No\n> "))
		if make_files == 1:
			results = open("results/%s"%result_fiename,"w")
			for item in result_list:
				results.write(item) 
			results.write( "Total %d matches" % counter)
			results.close()
			counter = 0
		else:
			counter = 0
