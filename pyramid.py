def pyramid(word):
	chars = set([c for c in word])
	counts = [word.count(c) for c in list(chars)]
	counts.sort()
	if counts[0] != 1: 
		return False
	else:
		for i in range(1, len(counts)):
			if counts[i] - 1 != counts[i-1]:
				return False
		return True

if __name__ == '__main__':
	print(pyramid('banana'))
	print(pyramid('bandana'))