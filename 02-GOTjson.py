#!usr/bin/pyton3
'''Author: SK | Learning GOTjson.py" | Dept: DevOps'''

#pull in json lib so we can parse out json
import json

def main():
    #open the jonsnow.json file in read mode
    with open("jonsnow.json", "r") as gotdata:
        jonsnow = gotdata.read() # create a STRING of all the json
        GOTpy = json.loads(jonsnow) # convert STRING to pythonic LISTs and DICTs
    print(GOTpy) # display the GOTpy data
    print(GOTpy["url"]) # display values assoc w/ URL
    print(GOTpy["titles"][0]) # display vaulues assoc w/ TITLES
    
    # create a loop to move across aliases
    with open("aliases.txt", "w") as jsaliases: #our short hand way of referring to 'alias.txt' is 'jsaliases' ; can also use a path
        for gotalias in GOTpy["aliases"]: #keep going thru the loop until it reaches the end of the 'alias' collection
            print(gotalias), file=jsaliases) #print to file not the screen

    print(GOTpy["aliases"]) # display values assoc w/ ALIASES

if __name__ == "__main__":
    main()
