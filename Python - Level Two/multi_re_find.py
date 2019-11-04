import re

def multi_re_find(patterns, phrase):

	for pat in patterns:
		print("Searching for pattern {}".format(pat))
		print(re.findall(pat,phrase))

test_phrase = 'sdsd...sssddd...sdddsddd.....dsds....sddddddd'
# test_pattern = ['sd*']
# test_pattern = ['sd+']
# test_pattern = ['sd?']
# test_pattern = ['sd{3}'] #if get three d in the last 
# test_pattern = ['sd{1,3}'] #here find only one d or three d

test_pattern = ['s[sd]+'] #find one or more s or d 
test_pattern = ['s[sd]+']  



new_phrase = "this is a string! But is has pucntuation. How can we remove it?"
new_pattern = ['[^!.?]+']

new1_phrase = "This is a string! But is has pucntuation. How can we remove it?"
new1_pattern = ['[a-z]+']


# Searching number in text:
text_phrase = "This is a string with numbers 12312 and a symbol #hashtag"
text_pattern = [r'\d+']
text_pattern = [r'\s+'] #how many white space having there
text_pattern = [r'\S+'] # how many non white space



# call the function multi_re_find here:
multi_re_find(text_pattern,text_phrase)