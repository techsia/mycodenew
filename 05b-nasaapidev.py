#!/usr/bin/python3

import requests

import pprint
MYAPI = "https://api.nasa.gov/neo/rest/v1/neo/browse/?api_key="

def keyharvester():
    with open("/home/student/nasa.key", "r") as keyfile:
        mykey = keyfile.read()
        return mykey.rstrip('\n')

def main():
    # harvest our key from /home/student/kmt.key
    nasakey = keyharvester()

    # append our key to MYAPI
    # call the API (reqest.get()_ and putll off json (.json())
    print(MYAPI + nasakey)
    resp = requests.get(MYAPI + nasakey)
    asteroidz = resp.json()
    #asteroidz = requests.get(MYAPI + nasakey).json()  # combine the 2 lines into one
    
    # pull json off response
    
    # parse json - loop across "near_earth_objects" to reveal asteroids 
    # pprint.print(asteroidz["near_earth_objects"])
    #print(asteroidz)
    for bigrock in asteroidz["near_earth_objects"]:
        if (bigrock["is_potentially_hazardous_asteroid"]):
            print("Name -", bigrock["name"])
            print("Proximity - ", bigrock["close_approach_data"])
            print("Size - ", bigrock["estimated_diameter"], end="\n********\n")
       # else:
            #print("This asteroid is not one to concern yourself with")
        
    # only display those that may pose a danger

if __name__ == "__main__":
    main()
