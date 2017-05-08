import sys

class English():
	def __init__(self):
		self.letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
		self.lettsrs_and_spaces=self.letters+self.letters.lower()+" \t\n"
		self.english_words = self.loadDictionary()

	def loadDictionary(self):
		try:
			file = open('words.txt','r')
			words={}
			for line in file.readlines():
				words[line.strip()]=None
			file.close()
			return words
		except IOError:
			sys.exit('\'words.txt\' file does not exit, or it can not be read!')

	def removeNonLetters(self,msg):
		"""removes non-alphabetic words"""
		lst=[]
		for letter in msg:
			if letter in self.lettsrs_and_spaces:
				lst.append(letter)
		return ''.join(lst)

	def getEnglishCount(self,msg):
		#msg=msg.upper()
		msg=self.removeNonLetters(msg)
		words = msg.split()
		if words == []:
			return 0.0
		match=0
		for word in words:
			if word in self.english_words:
				match += 1
		return float(match) / len(words) * 100.0

	def isEnglish(self,msg):
		# By default, 20% of the words must exist in the dictionary file, and
		# 85% of all the characters in the message must be letters or spaces
		# (not punctuation or numbers).
		wordsMatch = self.getEnglishCount(msg) >= 70.0
		"""numLetters = len(removeNonLetters(msg))
		messageLettersPercentage = float(numLetters) / len(msg)
		lettersMatch = messageLettersPercentage >= 80"""
		return wordsMatch

	
def main():
	#cipher='PHHW PH DIWHU WKH WRJD SDUWB'
	letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	eng=English()
	while True:	
		plains=[]
		cipher=raw_input('\nEnter your cipher (q or -1 to terminate): ')
		if cipher=='q' or cipher=='-1': break
		cipher=cipher.upper()
		for i in range(26):
			p=[]
			for c in cipher:
				if c in letters: p.append(chr((ord(c)-65+i)%26+65))
				else: p.append(c)
			#p=''.join([chr((ord(c)-65+i)%26+65) for c in cipher if c in letters])
			plains.append(''.join(p))
		engPlains=[]
		for plain in plains:
			#print plain
			if eng.isEnglish(plain.lower()): engPlains.append(plain)
		print '\n\nThe following plains seem to be correct:'
		for p in engPlains:
			print p
	print 'bye...'
	
if __name__ == "__main__":
	main()