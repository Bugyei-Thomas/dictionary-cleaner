import os
import sys
import tempfile
from tqdm import tqdm  

def process_files(file_list):
    for wordlist_file in file_list:
        if os.path.isfile(wordlist_file):
            print(f"[+] Processing file: {wordlist_file}")
            remove_duplicates(wordlist_file)
        else:
            print(f"[-] File not found: {wordlist_file}")

def remove_duplicates(wordlist_file):
    temp_file = wordlist_file + '.tmp'
    temp_seen_file = tempfile.NamedTemporaryFile(delete=False)

    seen_file_path = temp_seen_file.name
    seen_words = set()
    
    with open(wordlist_file, 'r', errors='ignore') as infile, open(temp_file, 'w') as outfile:
        total_lines = sum(1 for _ in infile)
        infile.seek(0)  # Reset file pointer
        batch_size = 10000
        batch = []

        for line in tqdm(infile, total=total_lines, desc=f"[+] Processing {wordlist_file}"):
            word = line.strip()
            if word not in seen_words:
                outfile.write(f"{word}\n")
                seen_words.add(word)
                
            if len(seen_words) % batch_size == 0:
                # Write seen words to the temp file periodically
                with open(seen_file_path, 'a') as seen_file:
                    seen_file.write('\n'.join(seen_words) + '\n')
                seen_words.clear()  # Clear the set to free up memory

        # Write remaining seen words to the temp file
        if seen_words:
            with open(seen_file_path, 'a') as seen_file:
                seen_file.write('\n'.join(seen_words) + '\n')

    os.remove(wordlist_file)
    os.rename(temp_file, wordlist_file)
    os.remove(seen_file_path)
    print(f"[+] cleaned up wordlist, duplicates removed in: {wordlist_file}")

def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <file1> <file2> ... <fileN>")
        sys.exit(1)

    files = sys.argv[1:]
    process_files(files)

if __name__ == '__main__':
    main()

