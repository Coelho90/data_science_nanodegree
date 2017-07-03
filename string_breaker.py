def string_breaker(list):
	"""
	Returns a String with 140 characters
	"""
	news_ticker = ""
	for item in list:
		if len(news_ticker + item + " ") <= 140:
			news_ticker += item + " "
		else:
			break

	return news_ticker



headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

print(len(string_breaker(headlines)))
print(string_breaker(headlines))