#!/usr/bin/python3
""" Author: SK | Email:  | Learning about API rquests """

import json #imports json library
import urllib.request

# Define API
MAJORTOM = "http://api.open-notify.org/astros.json" # If you define a variable inside a function, then it's lowercase
def main ():
    # make request
    resp = urllib.request.urlopen(MAJORTOM)
    print(dir(resp)) # return the methods avail to our resp object
    # make python strip JSON data FROM the 200 response
    jstring = resp.read()

    # convert string data to JSON
    #print(jstring) #display jstring currently
    #print(type(jstring)) # what class is jstring from?
    #print(dir(jstring)) # methods avail to jstring
    pyj = json.loads(jstring.decode('utf-8'))
    
    # parse out json attached to 200
    #print(pyj)
    astrocosmo = pyj.get("people")

    # display selected data on screen - names of people in space
    print("CURRENTLY IN SPACE:")
    for spaceperson in astrocosmo:
        print(spaceperson)

if __name__ == "__main__":
    main()
