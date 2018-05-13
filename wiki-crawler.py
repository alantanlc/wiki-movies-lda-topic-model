import json
import pycorpora
import requests

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--dns-prefetch-disable')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--lang=en-US')
chrome_options.add_argument('--headless')
chrome_options.add_experimental_option('prefs', {'intl.accept_languages': 'en-US'})
browser = webdriver.Chrome('./assets/chromedriver', chrome_options=chrome_options)

# Extract list of popular movies
movies = pycorpora.film_tv.popular_movies['popular-movies']

# Split entries into title and year
movies = [m[:-1].split(' (') for m in movies]

# Keep list of movies whereby crawling was unsuccessful
unsuccessfulMovies =[]

# Get url of movie
for m in movies:
	print('Extracting ' + m[0] + '...')

	title = str(m[0]).replace('The ', '')
	year = m[1]
	searchURL = 'https://en.wikipedia.org/w/index.php?title=Category:' + year + '_films&from=' + title[0]
	browser.get(searchURL)
	xpath = '//a[contains(@title, "' + title + '")]'

	try:
		# Get accurate wiki title of movie to perform wiki query
		wikiTitle = browser.find_element_by_class_name('mw-category-group').find_element_by_xpath(xpath).get_attribute('title') # Search for mw-category-group to be more precise
		query = 'https://en.wikipedia.org/w/api.php?action=query&format=json&prop=revisions&rvprop=content&titles=' + wikiTitle

		# Extract wiki content of movie
		response = requests.get(query)
		data = response.json()

		# Write wiki content to json file
		fileName = 'movies-wiki-content/' + m[0] + '.json'
		with open(fileName, 'w') as f:
			f.writelines(json.dumps(data, indent=4))
			print('\tExtraction successful and content written to ' + fileName + '!')
	except:
		unsuccessfulMovies.append(m)
		print('\tExtraction failed!')

# Print unsuccessful movies
print(str(unsuccessfulMovies))

print('Program completed!')