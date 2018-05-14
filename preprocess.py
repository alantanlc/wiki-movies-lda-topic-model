import os

# Directories
raw_dir = './data/raw/'
preprocess_dir = './data/preprocess/'

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

			# Extract words
			words = content.split(' ')

			# Perform preprocessing
			# Remove punctuation, stop list, symbols...
			words = [word.strip() + '\n' for word in words]

			# Write processed data to file
			with open(preprocess_path, 'w', encoding='utf-8') as f:
				f.writelines(words)
				print('\tPreprocessing completed and written to ' + preprocess_path)

		except Exception as e:
			print('\tPreprocess failed! ' + e)

