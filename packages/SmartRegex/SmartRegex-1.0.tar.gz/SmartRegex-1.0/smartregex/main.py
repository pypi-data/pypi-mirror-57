from smartregex import SmartRegex
import sys
import pprint

def main():
    interpreter = SmartRegex()
    input_text = None
    if (len(sys.argv) == 2):
        print("Reading from file " + str(sys.argv[1]))
        with open(sys.argv[1], 'r') as f:
            input_text = f.read()
    else:
        print("To get started, enter text file name as secondary argument.")
        return ""
    
    if input_text:
        print("1. Raw Text is here:")
        pprint.pprint(input_text)
        smart = SmartRegex(input_text)
        print("2. Initiated SmartRegex parsed results:")
        pprint.pprint(smart.parsed)
        print("3. Checking specific elements:")
        print("3.a. Checking for emails:")
        print(smart.has('emails'))
        print("3.b. Checking for street address:")
        print(smart.has('street'))
        print("3.c. Checking for dates:")
        print(smart.has('dates'))

main()