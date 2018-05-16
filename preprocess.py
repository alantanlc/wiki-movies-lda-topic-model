import os
import re
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# import nltk
# nltk.download()

# Directories
raw_dir = './data/raw/'
preprocess_dir = './data/preprocess/'

# Get stop words
stop_words = set(stopwords.words('english'))

# Preprocess txt files
for file_name in os.listdir(raw_dir):
	if file_name.endswith('.txt'):
		print('Preprocessing ' + os.path.join(raw_dir, file_name) + '...')
		raw_path = os.path.join(raw_dir, file_name)
		preprocess_path = os.path.join(preprocess_dir, file_name)

		try:
			# Open file
			with open(raw_path, 'r', encoding='utf-8') as f:
				content = f.read()

			# Remove punctuation and multiple spaces using regular expression
			content = re.sub(r'[^\w\s]', ' ', content)

			# Convert to lower case
			content = content.lower()

			# Tokenize
			word_tokens = word_tokenize(content)

			# Remove stop words
			words = [w for w in word_tokens if not w in stop_words]

			# Write processed data to file
			words = [word + '\n' for word in words]
			with open(preprocess_path, 'w', encoding='utf-8') as f:
				f.writelines(words)
				print('\tPreprocessing completed and written to ' + preprocess_path)

		except Exception as e:
			print('\tPreprocess failed! ' + str(e))

