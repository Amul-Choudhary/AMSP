import nltk
from nltk.metrics import edit_distance

def getDistance(x, y):
	return edit_distance(x, y)

def getMatch(word, wordList, thresh=5):
	min_dist = 50
	min_word = ''
	for w in wordList:
		d = getDistance(word, w)
		if (d < min_dist):
			min_dist = d
			min_word = w

	if (min_dist < thresh):
		return min_word
	return False


if __name__ == '__main__':
	x = "ciprofloxacin"
	y = "iprortoxacin"

	print(getDistance(x, y))

