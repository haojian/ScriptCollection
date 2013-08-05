import sys
from optparse import OptionParser
import string

CHAR_MAP = dict(zip (string.ascii_lowercase, 
			string.ascii_lowercase[13:26] + string.ascii_lowercase[0:13]))
		
class RotateStream(object):
	"""
	General purpose ROT13 translator
	
	A ROT13 translator smart enough to skip Markup tags if that's what we want.
	"""
	MARKUP_START = '<'
	MARKUP_END = '>'
	
def rotate13_letter(letter):
	"""
	return the 13-char rotation of a letter.
	"""
	do_upper = False
	if letter.isupper():
		do_upper = True;
	letter = letter.lower()
	if letter not in CHAR_MAP:
		return letter
	else:
		letter = CHAR_MAP[letter]
		if do_upper:
			letter = letter.upper()
	return letter
	
if __name__ == '__main__':
	for line in sys.stdin:
		for char in line:
			sys.stdout.write(rotate13_letter(char))
	#sys.stdout.write('\n')
			
