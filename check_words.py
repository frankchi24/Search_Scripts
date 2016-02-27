import glob
import linecache
import fnmatch
import os
import re
import nltk
import tokenize
result_list = []
def scope(os_path,series,pick_series):
		if pick_series > 0 and pick_series!= 99:
			series_name = series[int(pick_series)-1]
			season_number = input('Which Season? Type 0 if search all seasons\n> ')	
			if season_number > 0:
				season = "Season %d" % season_number
			elif season_number == 0:
				season = "*" 
			path = os_path + "%s/%s/*.srt" % (series_name, season)
			files = glob.glob(path)
			return files

		#2.pick all tv shows in the database and search through them all
		elif pick_series == 0:
			series_name = "*" 
			season ="*"
			path = os_path + '%s/%s/*.srt' % (series_name, season)
			files = glob.glob(path)
			return files
			 
		#3. pick multiple tv shows and search through 
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
				files = files + glob.glob(os_path +'%s/%s/*.srt' % (series[number-1],"*"))
			return files
	

#run check phrases function with each line in each subtitles file 
def check_lines_in_files(files,text,counter,result_list):
	#three different scopes, 
	#1.pick a tv show and a season and search through them
	for file in files:
		fp = open (file, 'r')
		for i, line in enumerate(fp):
			if re.findall(r'%s\s|%s.|%s\,|%s\?|%s\!'%(text,text,text,text,text),line.lower()):
				counter = counter + 1
				filename = os.path.basename(fp.name)
				lines_presented = -2			
				result_list.append(
				"<Number %d match>\n<In file '%s'>\n<In line %d in the file>" % (counter,filename,i),
				)
				while lines_presented <= 3:
					result_list.append(
						linecache.getline(file, i+lines_presented)
						)
					lines_presented = lines_presented + 1
				result_list.append(
				"------------------------------------------------------\n"
				)
				linecache.clearcache()
		fp.close()	
	for x in result_list:
		print x
	print "Total %d matches" % counter
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


# def phrases_or_word(text):
# 	if re.findall(r' ',text.lower()):
# 		print text


# def check_phrases(files,text,counter,result_list):
# 	for file in files:
# 		fp = open (file, 'r')
# 		for i, line in enumerate(fp):
# 			if re.findall(r'%s\s|%s.|%s\,|%s\?|%s\!'%(text,text,text,text,text),line.lower()):
# 				counter = counter + 1
# 				filename = os.path.basename(fp.name)
# 				lines_presented = -2			
# 				result_list.append(
# 				"<Number %d match>\n<In file '%s'>\n<In line %d in the file>" % (counter,filename,i),
# 				)
# 				while lines_presented <= 3:
# 					result_list.append(
# 						linecache.getline(file, i+lines_presented)
# 						)
# 					lines_presented = lines_presented + 1
# 				result_list.append(
# 				"------------------------------------------------------\n"
# 				)
# 				for item in result_list:
# 					print item
# 				linecache.clearcache()
# 		fp.close()	
# 	print "Total %d matches" % counter
# 	if counter > 0:
# 		result_fiename = text + ".txt"
# 		make_files =  int(raw_input("Do you wanna print the results out as txt files?\n1.Yes\n2.No\n> "))
# 		if make_files == 1:
# 			results = open("results/%s"%result_fiename,"w")
# 			for item in result_list:
# 				results.write(item) 
# 			results.write( "Total %d matches" % counter)
# 			results.close()
# 			counter = 0
# 		else:
# 			counter = 0
