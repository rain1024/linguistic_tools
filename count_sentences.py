import os
import docx


def count_sentences(input_file):
    document = docx.Document(input_file)
    texts = []
    texts = [paragraph.text for paragraph in document.paragraphs if paragraph.text.strip()]
    tmp_folder = "tmp"
    if not os.path.exists(tmp_folder):
        os.makedirs(tmp_folder)    
    
    base_name = os.path.splitext(os.path.basename(input_file))[0]
    file_name = f"{base_name}.txt"
    with open(f"{tmp_folder}/{file_name}", "w") as f:
        f.write("\n".join(texts))

    print(f"{input_file}: {len(texts)} sentences")

if __name__ == '__main__':
    input_dir = "inputs"
    input_files = [os.path.join(input_dir, file) for file in os.listdir(input_dir) if file.endswith(".docx")]

    for input_file in input_files:
        count_sentences(input_file)
