import re

text = "test phrase match in match middle"

result = re.findall('match', text)

# result type is list type
print(result)
