#!/usr/bin/python3
""" Author: SK | Email:  | Learning about API rquests """

import requests
# Define API
MAJORTOM = "http://api.open-notify.orgz/astros.json" # If you define a variable inside a function, then it's lowercase #added z to force an error
def main ():
    try:
        # make request
        pyj = requests.get(MAJORTOM).json()
    
        # convert string data to JSON
        #pyj = resp.json()
    
        # parse out json we stripped off response
        #print(pyj)
        astrocosmo = pyj.get("people")

        # display selected data on screen - names of people in space
        print("CURRENTLY IN SPACE:")
        for spaceperson in astrocosmo:
            print(spaceperson)
    except:
        print("API is unavailable at the moment")
        exit()

if __name__ == "__main__":
    main()
