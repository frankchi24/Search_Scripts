import glob
import linecache
import fnmatch
import os
import re
import nltk
import tokenize


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

def text_is_word(text):
	if re.search(r'\s',text):
		return False
	else:
		return True

#run check phrases function with each line in each subtitles file 
def check_words(files,text,counter,result_list):
	#three different scopes, 
	#1.pick a tv show and a season and search through them
	for file in files:
		fp = open (file, 'r')
		for i, line in enumerate(fp):
			if re.search(r'\b%s\b'%(text),line.lower()):
				#'\bfoo\b' matches 'foo', 'foo.', '(foo)', 'bar foo baz' but not 'foobar' or 'foo3'.
				counter = counter + 1
				filename = os.path.basename(fp.name)
				lines_presented = -5			
				result_list.append(
				"<Number %d match>\n<In line %d in the file>\n<In file '%s'>" % (counter,i,filename),
				)
				while lines_presented <= 5:
					if re.search(r'^\w',linecache.getline(file, i+lines_presented)):
						if re.search(r'^\D',linecache.getline(file, i+lines_presented)):
							result_list.append(linecache.getline(file, i+lines_presented))
					if re.search(r'-->',linecache.getline(file, i+lines_presented)):
						result_list.append(linecache.getline(file, i+lines_presented))
					lines_presented = lines_presented + 1
				result_list.append(
				"------------------------------------------------------\n"
				)
				linecache.clearcache()
		fp.close()	
	for item in result_list:
		print item
	print "Total %d matches for \"%s\"" % (counter,text)
	print_or_not(counter,text,result_list)



def check_phrases(files,text,counter,result_list):
	tokens = nltk.word_tokenize(text)
	range_list = []
	for file in files:
		fp = open (file, 'r')
		filename = os.path.basename(fp.name)
		for i, line in enumerate(fp):
			# search the first word in the phrases, 
			if re.search(r'%s\s'%(tokens[0]),line.lower()):
				for x in range(-1,4):
					linecache_yo = linecache.getline(file,i+x)
					if re.search(r'\w',linecache_yo.lower()):
						range_list.append(linecache_yo)
				# once found, get the adjacent lines in a list
				# search for the remaining words in the list
				range_string = ''.join(range_list)
				if all(re.search(r'%s'%(token),range_string) for token in tokens):
					result_list.append(
					"<Number %d match>\n<In line %d in the file>\n<In file '%s'>" % (counter,i,filename),
					)
					result_list.append(range_string)
					result_list.append("---------------------------")
					counter = counter + 1
				range_list = []
		fp.close()
	for item in result_list:
		print item
	print "Total %d matches" % counter
	print_or_not(counter,text,result_list) 



def print_or_not(counter,text,result_list):
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



