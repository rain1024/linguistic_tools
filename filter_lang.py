import docx
import os
from underthesea.pipeline.lang_detect import lang_detect

def extract(input_files, output_dir, lang):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Iterate through the input files
    for input_file in input_files:
        # Open the input Word document
        document = docx.Document(input_file)

        # Extract the text from each paragraph
        texts = [paragraph.text for paragraph in document.paragraphs]
        texts = [item.split("\n") for item in texts]
        texts = [item for sublist in texts for item in sublist]
        texts = [text for text in texts if text.strip()]

        # Filter the sentences that are in the specified language
        filtered_texts = [text for text in texts if lang_detect(text) == lang]

        # Get the file name of the input file
        file_name = os.path.basename(input_file)

        # Create the output file path
        output_file = os.path.join(output_dir, file_name + '.txt')

        # Write the filtered text to the output file
        with open(output_file, 'w') as f:
            for text in filtered_texts:
                f.write(text + '\n')


# Set the input and output directories
input_dir = "inputs"
output_dir = "tmp"

# Get a list of the input files
input_files = [os.path.join(input_dir, file) for file in os.listdir(input_dir) if file.endswith(".docx")]

# Set the language to filter by
lang = "vi"

# Extract and filter the text from the input files and write it to the output files
extract(input_files, output_dir, lang)
