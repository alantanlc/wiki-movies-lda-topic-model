import os

# Load wordids.txt
wordids_dir = './data/wordids/'
file_name = 'wordids.txt'
wordids_path = os.path.join(wordids_dir, file_name)
with open(wordids_path, 'r', encoding='utf-8') as f:
    words = f.readlines()
    words = [w.strip() for w in words]

# Sort words list
words.sort()

# Get unique list of words and  write to txt file
unique_wordids_file_name = 'unique-wordids.txt'
with open(wordids_dir + unique_wordids_file_name, 'w', encoding='utf-8') as f:
    # Get unique list of words
    w = ''
    for word in words:
        if word != w:
            f.write(word + '\n')
            w = word

print('Program completed!')