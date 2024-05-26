# Linguistic Tools

This project is a set of linguistic tools designed to assist my **lovely friend** 💕 with various language-related tasks.

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
python filtered_words.py
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
