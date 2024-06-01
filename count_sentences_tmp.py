import os

# Define the path to the tmp folder
folder_path = 'tmp'

# Function to count sentences in a file
def count_sentences(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        # Split text into sentences by newline
        sentences = text.split('\n')
        # Remove empty strings from the list
        sentences = [sentence for sentence in sentences if sentence.strip()]
        return len(sentences)

# Dictionary to store the count of sentences for each file
sentence_counts = {}

# Iterate over each file in the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        sentence_counts[filename] = count_sentences(file_path)

# Print the results
for filename, count in sentence_counts.items():
    print(f'{filename}: {count} sentences')