import os
# Load wordids.txt
wordids_dir = './data/wordids/'
file_name = 'wordids.txt'
path = os.path.join(wordids_dir, file_name)
with open(path, 'r', encoding='utf-8') as f:
    words = f.readlines()
    words = [w.strip() for w in words]

# Sort words list
words.sort()

print('Program completed!')