# Requirements : pip install langdetect
# not good just for educational purpose

from langdetect import detect
while True:
    txt = input("Enter text: ")
    if txt == "exit": break
    print("Language:", detect(txt))

