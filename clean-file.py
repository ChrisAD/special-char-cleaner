# -*- coding: utf-8 -*-
import argparse
import re

parser = argparse.ArgumentParser(description='Clean an input file from special characters.')
parser.add_argument("f")
args = parser.parse_args()

file = open(args.f, "r")
print("Using file " + args.f + " as input...")
clean = file.read().replace(" ", "").replace("å", "a").replace("å", "a").replace("ø", "o").replace("æ", "ae").replace("ã", "a").replace("õ", "o").replace("â", "a").replace("ê", "e").replace("î", "i").replace("ô", "o").replace("û", "u").replace("ä", "a").replace("ë", "e").replace("ï", "i").replace("ö", "o").replace("ü", "u").replace("à", "a").replace("è", "e").replace("ì", "i").replace("ò", "o").replace("ù", "u").replace("á", "a").replace("é", "e").replace("í", "i").replace("í", "i").replace("ó", "o").replace("ú", "u").replace("Â", "A").replace("Ê", "E").replace("Î", "I").replace("Ô", "O").replace("Û", "U").replace("Ä", "A").replace("Ë", "E").replace("Ï", "I").replace("Ö", "O").replace("Ü", "U").replace("Á", "A").replace("É", "E").replace("Í", "I").replace("Ó", "O").replace("Ú", "U").replace("À", "A").replace("È", "E").replace("Ì", "I").replace("Ò", "O").replace("Ù", "U").replace("ñ","n").replace("Ñ","N").replace("Ø","O")
clean = re.sub('[^0-9a-zA-Z@\.\n]+', '', clean)

file.close()
file2_filename = args.f+"_clean"
file2 = open(file2_filename, "w")
print("Written to file " + file2_filename)
file2.write(clean)
file2.close()
