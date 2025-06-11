import sys
import pyfiglet

text = input("Input: ")
if len(sys.argv) == 1:
    font = pyfiglet.Figlet()
    print("Output:\n ", font.renderText(text))
elif len(sys.argv) == 3:
    font = pyfiglet.Figlet(sys.argv[2])
    print("Output:\n",font.renderText(text))
else:
    print("Invalid Font!")
