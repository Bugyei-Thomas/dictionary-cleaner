# Dictionary Cleaner

A Python tool for removing duplicate lines from wordlist files. Supports processing multiple files in a single run with a progress bar.

## Requirements

- Python 3
- tqdm

## Installation

```bash
git clone https://github.com/s4wbvnny/dictionary-cleaner
cd dictionary-cleaner
pip3 install -r requirements.txt
```

## Usage

```bash
python3 cleaner.py <file1> <file2> <file3>...
```

### Example

```bash
python3 cleaner.py wordlist1.txt wordlist2.txt
```

Each specified file will be processed in place -- duplicates are removed and the original file is replaced.

## How It Works

1. Reads each wordlist line by line.
2. Tracks unique entries and writes only the first occurrence of each line.
3. Replaces the original file with the deduplicated version.

## License

MIT
