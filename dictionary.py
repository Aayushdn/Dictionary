def main():
	import json
	from difflib import get_close_matches

	data = json.load(open('data.json'))


	def case(inword):
	    inword = inword.lower()
	    if inword in data:
	        return data[inword]
	    elif inword.title() in data:
	        return data[inword.title()]
	    elif inword.upper() in data:
	        return data[inword.upper()]
	    elif len(get_close_matches(inword, data.keys())) > 0:
	        print('did you means %s instead' % get_close_matches(inword, data.keys())[0])
	        decide = input('press y/n')
	        if decide == 'y':
	            return data[get_close_matches(inword, data.keys())[0]]
	        elif decide == 'n':
	            print('sorry the word you have enter is not found')
	    else:
	        print('sorry the word you have enter is not found')


	inword = input('enter a word to be searched :  ')

	inwordop = case(inword)

	if type(inwordop) == list:
	    for i in inwordop:
	        print(i)
	        print('\r')
	else:
	    print(case(inword))
main()

out = input('do you want to exit  y/n')
if out == 'y':
	quit()
elif out == 'n':
	main()

else:
	print('Enter a valid character [y/n]')
	out = input('Do you want to exit')

