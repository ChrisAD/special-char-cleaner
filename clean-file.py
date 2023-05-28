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
        "õ":"o",
        "â":"a",
        "ê":"e",
        "î":"i",
        "ô":"o",
        "û":"u",
        "ä":"a",
        "ë":"e",
        "ï":"i",
        "ö":"o",
        "ü":"u",
        "à":"a",
        "è":"e",
        "ì":"i",
        "ò":"o",
        "ù":"u",
        "á":"a",
        "é":"e",
        "í":"i",
        "í":"i",
        "ó":"o",
        "ú":"u",
        "Â":"A",
        "Ê":"E",
        "Î":"I",
        "Ô":"O",
        "Û":"U",
        "Ä":"A",
        "Ë":"E",
        "Ï":"I",
        "Ö":"O",
        "Ü":"U",
        "Á":"A",
        "É":"E",
        "Í":"I",
        "Ó":"O",
        "Ú":"U",
        "À":"A",
        "È":"E",
        "Ì":"I",
        "Ò":"O",
        "Ù":"U",
        "ñ","n",
        "Ñ","N",
        "Ø","O"
        # Add more replacements here
    }
   

    for key, value in character_replacements.items():
        clean = clean.replace(key, value)

    clean = re.sub(r'[^0-9a-zA-Z@.\n]+', '', clean)

file2_filename = args.f+"_clean"

with open(file2_filename, "w") as file2:
    print("Written to file " + file2_filename)
    file2.write(clean)
