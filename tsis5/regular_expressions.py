import re
def zeromore(text):
        patterns = '^a(b*)$'
        if re.search(patterns,  text):
                return('Found a match!')
        else:
                return('Not matched!')

d = str(input())
print(zeromore(d))

#2
def twothree(text):
        patterns = 'ab{2,3}'
        if re.search(patterns,  text):
                return('Found a match!')
        else:
                return('Not matched!')
d = str(input())
print(twothree(d))
#3
def underscore(text):
        patterns = '^[a-z]+_[a-z]+$'
        if re.search(patterns,  text):
                return('Found a match!')
        else:
                return('Not matched!')

d = str(input())
print(underscore(d))

#4
def upperlower(text):
        patterns = '[A-Z][a-z]+$'
        if re.search(patterns, text):
                return('Found a match!')
        else:
                return('Not matched!')

d = str(input())
print(upperlower(d))
#5
def lastb(text):
        patterns = 'a.*?b$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

d = str(input())
print(lastb(d))
#6
d = str(input())
print(re.sub("[ ,.]", ":", d))

#7
def snake_to_camel(word):
        return ''.join(x.capitalize() or '_' for x in word.split('_'))

d = str(input())
print(snake_to_camel(d))

#8
d = str(input())
print(re.findall('[A-Z][^A-Z]*', d))

#9
def capital_words_spaces(str1):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", str1)

print(capital_words_spaces(d))

#10
def camel_to_snake(text):
        str1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', str1).lower()

d = str(input())
print(camel_to_snake(d))
