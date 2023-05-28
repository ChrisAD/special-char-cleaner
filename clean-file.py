import argparse
import re

parser = argparse.ArgumentParser(description='Clean an input file from special characters.')
parser.add_argument("f")
args = parser.parse_args()

with open(args.f, "r", encoding="utf-8") as file:
    print("Using file " + args.f + " as input...")
    clean = file.read()
    
    character_replacements = {
        "å": "a",
        "ø": "o",
        "æ": "ae",
        "ã": "a",
        # Add more replacements here
    }

    for key, value in character_replacements.items():
        clean = clean.replace(key, value)

    clean = re.sub(r'[^0-9a-zA-Z@.\n]+', '', clean)

file2_filename = args.f+"_clean"

with open(file2_filename, "w") as file2:
    print("Written to file " + file2_filename)
    file2.write(clean)
