# Linguistic Tools

This project is a set of linguistic tools designed to assist my **lovely friend** 💕 with various language-related tasks.

* [Filter Words](#filter-words)
* [Count Senenteces](#count-sentences)

## Filter Words

The Filter Words tool is designed to process and filter specific words from a given text file, `query.txt`. This tool reads paragraphs from the input file located in the `inputs` folder, applies the necessary filters, and saves the processed output to separate files in the `outputs` folder.

### Usage

To use the Filter Words tool, follow these steps:

**Step 1:** Place your Microsoft Word file in the `inputs` folder.

Example:

```
inputs
 └── song_mon__nam_cao.docx
```

**Step 2:** Add your query in the `query.txt` file.

Example content for `query.txt`:

```
chớ
các
không,đã
đã,rồi
```

**Step 3:** Run the following command in your terminal:

```
python filter_words.py
```

This command will execute the script, process the input file, and generate the filtered outputs in the `outputs` folder.

### Output

The processed output files will be saved in the `outputs` folder, each corresponding to the words or word pairs specified in the `query.txt` file.

Example:

```
outputs
 ├── chớ.txt
 ├── các.txt
 ├── không-đã.txt
 └── đã-rồi.txt
```

## Count Sentences

The script described here is designed to count the number of sentences in Microsoft Word documents (.docx) located in a specified input directory. It processes each document to extract paragraphs, filters out empty paragraphs, and saves the text content into a temporary file. The script also prints the number of sentences (non-empty paragraphs) found in each document.

### Input

Place your Microsoft Word files (.docx) in the `inputs` folder. The script will automatically detect and process all .docx files within this directory.

Example:

```
inputs
 └── document1.docx
 └── document2.docx
```

### Command Line Usage

To execute the script, run the following command in your terminal:

```
python count_sentences.py
```

This command will initiate the script, which will process each .docx file in the `inputs` folder.

### Output

The script creates a temporary folder named `tmp` to store the output text files. Each output file corresponds to an input document and contains the extracted paragraphs. The script also prints the number of sentences found in each document to the console.

Example of the temporary folder structure and console output:

```
tmp
 └── document1.txt
 └── document2.txt
```

Console output:

```
inputs/document1.docx: 10 sentences
inputs/document2.docx: 8 sentences
```