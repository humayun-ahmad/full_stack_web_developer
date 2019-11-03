import re

patterns = ['term1', 'term2']

text = 'This is a string wit term1, not the oth!'

match = re.search('term1',text)

# first to term1 the number of character:
print(match.start())

split_term = '@'
email = "user@gmail.com"

# print(email)

x = re.split(split_term,email)

print(x)