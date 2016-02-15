# ShowMeEnglish Scripts and content management system
# Features
# 1. store subtitles as srt files, search through them when
# 2. search by each tv series, seasons, episodes, sentences
# 3. search and present words in sentences and episodes
import glob
import linecache
import fnmatch
import os
#search in one or serveral specific tv series
counter = 0 
while counter == 0:
	text = raw_input('Search a term or a word\n> ').lower() 
	text1 = text + " "
	text2 = text + ","
	text3 = text + "."
	text4 = text + "?"

	series = ["How I Met Your Mother", "The Big Bang Theory","Game of Thrones","House of Cards","Breaking Bad"]
	pick_series = int(raw_input('Search in a TV Show? Pick a number.\n0.ALL\n1.How I Met Your Mother\n2.Big Bang Theory\n3.Game of Thrones\n4.House of Cards\n5.Breaking Bad\n> '))
	if pick_series > 0:
		series_name = series[int(pick_series)-1]
	elif pick_series == 0:
		series_name = "*"

	season_number = input('Which Season? Type 0 if search all seasons\n> ')
	if season_number > 0:
		season = "Season %d" % season_number
	elif season_number == 0:
		season = "*"
	#for windows
	# path = 'C:\Users\Frank/Desktop/ScriptSearch/%s/%s/*.srt' %(series_name,season)
	#for linux
	path = '/home/frank/Dropbox/ScriptSearch/%s/%s/*.srt' % (series_name, season)
	files = glob.glob(path)
	result_list = []
	#check if the input text matches the 
	def check_phrases():
		filename = os.path.basename(fp.name)
		line_before_last_line = linecache.getline(file, i-1)
		last_line = linecache.getline(file, i)
		next_line = linecache.getline(file, i+2)
		print "<Number %d match>" % counter
		print "<In file '%s'>" %filename
		print "<In line %d in the file>" % i
		print line_before_last_line
		print last_line
		print line
		print next_line
		print "------------------------------------------------------\n"	
		result_list.append("<Number %d match>" % counter)
		result_list.append(filename)
		result_list.append(line_before_last_line)
		result_list.append(last_line)
		result_list.append(line)
		result_list.append(next_line)
		result_list.append("----------------------\n")	
		linecache.clearcache()
	#run check phrases function with each line in each subtitles file 
	for file in files:
		fp = open (file, 'r')
		for i, line in enumerate(fp):
			if text1 in line.lower():
				counter = counter + 1
				check_phrases()
			elif text2 in line.lower():
				counter = counter + 1
				check_phrases()
			elif text3 in line.lower():
				counter = counter + 1
				check_phrases()
			elif text4 in line.lower():
				counter = counter + 1
				check_phrases()
		fp.close()	
	print "Total %d matches" % counter

	#create a txt file with the results
	if counter > 0:
		result_fiename = text + ".txt"
		make_files =  int(raw_input("Do you wanna print the results out as txt files?\n1.Yes\n2.No\n> "))
		if make_files == 1:
			results = open("results/%s"%result_fiename,"w")
			for item in result_list:
			  results.write("%s" % item)
			results.write( "Total %d matches" % counter)
			results.close()
			counter = 0
		else:
			counter = 0