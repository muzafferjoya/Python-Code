def top_search(keywords):
	counter=Counter(keywords)
	return f'{counter.most_common(1)[0][0]} was searched {counter.most_common(1)[0][1]} times'
