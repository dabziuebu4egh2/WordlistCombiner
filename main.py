# Script to combine wordlists and remove duplicate entries

import glob
read_files = glob.glob("~/SecLists/Discovery/Web-Content/*.txt")

with open("result.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())

inputFile = open("result.txt", "r")
def remove_duplicates(input_file):
    lines_seen = set()
    with open(input_file, "r") as in_file:
            for line in in_file:
                if line not in lines_seen:
                    lines_seen.add(line)

inputFile.close()

# todo: fix combination of duplicated entries, however these could be useful for enum as well