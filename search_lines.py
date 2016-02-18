# ShowMeEnglish Scripts and content management system
# Features now
# 1. search through stored subtitles(srt files), X
# 2. able to search by each tv series, seasons
# 3. search and present words in sentences and episodes
# 4. print the results as txt files

# Features to add
# able to search by each multiple series or seasons or episodes
# able to search phrases and words separately
# able to determine the how many lines are presented
# able to choose different stems, or search a lists of words 
import glob
import linecache
import fnmatch
import os
import re
#search in one or serveral specific tv series
counter = 0 
while counter == 0:
	text = raw_input('Search a term or a word\n> ').lower() 
	text1 = text + " "
	text2 = text + ","
	text3 = text + "."
	text4 = text + "?"
	text5 = text + "!"


	#for windows
	# os_path = 'C:\Users\Frank/Desktop/ScriptSearch'
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
	if pick_series > 0 and pick_series!= 99:
		series_name = series[int(pick_series)-1]
		season_number = input('Which Season? Type 0 if search all seasons\n> ')	
		if season_number > 0:
			season = "Season %d" % season_number
		elif season_number == 0:
			season = "*" 
		path = os_path + '%s/%s/*.srt' % (series_name, season)
		files = glob.glob(path)
	elif pick_series == 0:
		series_name = "*" 
		season ="*"
		path = os_path + '%s/%s/*.srt' % (series_name, season)
		files = glob.glob(path)
	elif pick_series == 99:
		numbers_user_pick = []
		print "0.ALL\n1.How I Met Your Mother\n2.The Big Bang Theory\
			\n3.Game of Thrones\n4.House of Cards\n5.Breaking Bad\
			\n6.Mad Men\n7.Suits\n8.The Newsroom\n9.Sex and the City"
		user_input = int(raw_input('Type the number of the series.\n>')) 
		while user_input!=0:			
			numbers_user_pick.append(user_input)
			print "---------------------------------------------"
			print "Here're the series you chose:\n"
			for number in numbers_user_pick:
				print series[number-1]
			user_input = int(raw_input('\nPick again?Type 0 to start search\n>')) 
		files = []
		for number in numbers_user_pick:			
			files = files + glob.glob(os_path +'%s/%s/*.srt' % (series[number],"*"))

	result_list = []

	#print phrases, print our the lines the prases are in
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
			# if text = re.findall(r'%s'%text,line.lower())
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
			elif text5 in line.lower():
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