import docx
import os


def extract(input_files, output_dir, words):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Iterate through the input files
    for input_file in input_files:
        # Open the input Word document
        document = docx.Document(input_file)

    # Extract the text from each paragraph
    texts = []
    for paragraph in document.paragraphs:
        texts.append(paragraph.text)

    # Filter the sentences that contain the word
    filtered_texts = []
    for text in texts:
        is_contained = True
        for word in words:
            if word not in text:
                is_contained = False
                break
        if is_contained:
            filtered_texts.append(text)

    # Create the subfolder for the output file
    filename = "-".join(words)
    subfolder = os.path.join(output_dir, filename)
    if not os.path.exists(subfolder):
        os.makedirs(subfolder)

    # Get the file name of the input file
    file_name = os.path.basename(input_file)

    # Create the output file path
    output_file = os.path.join(subfolder, file_name + '.txt')

    # Write the filtered text to the output file
    with open(output_file, 'w') as f:
        for text in filtered_texts:
            f.write(text + '\n\n')


# Set the input and output directories
input_dir = "inputs"
output_dir = "outputs"

# Get a list of the input files
input_files = [os.path.join(input_dir, file) for file in os.listdir(input_dir) if file.endswith(".docx")]

# Set the word to be contained in the sentence
# Extract and filter the text from the input files and write it to the output files
f = open("query.txt", "r")
lines = f.read().splitlines()

terms_group = [line.split(",") for line in lines if line != ""]

for terms in terms_group:
    extract(input_files, output_dir, terms)