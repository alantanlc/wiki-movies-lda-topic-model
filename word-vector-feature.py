import os
import json

preprocess_dir = './data/preprocess/'
feature_dir = './data/features/'

for file_name in os.listdir(preprocess_dir):
	if file_name.endswith('.txt'):
		print('Preprocessing ' + os.path.join(preprocess_dir, file_name) + '...')
		preprocess_path = os.path.join(preprocess_dir, file_name)
		feature_path = os.path.join(feature_dir, file_name)

		# Load words
		with open(preprocess_path, 'r', encoding='utf-8') as f:
			words = f.readlines()
			words = [w.strip() for w in words]

		# Sort words
		words.sort()

		# Get unique count of words
		unique_words_count = []
		current_word = ''
		for word in words:
			if word != current_word:
				unique_words_count.append([word, 1])
				current_word = word
			else:
				unique_words_count[-1][1] += 1

		# Write to txt file
		with open(feature_path, 'w', encoding='utf-8') as f:
			f.writelines([w[0] + ' ' + str(w[1]) + '\n' for w in unique_words_count])