#!/usr/bin/python3

import re

def main():
    with open("textcap.txt", "r") as testcap:
        for line in testcap:
            regmatch = re.search(r"^Contact:\ssip:\+(\d+)@\[(.*)\]:?(\d+)?", line)
            if regmatch:
                print(regmatch)            ## display match object
                print(regmatch.group())    ## display the full matcht
                print(regmatch.group(1))   ## display the digits of the caller
                print(regmatch.group(2))   ## display the IPv6
                print(regmatch.group(3))   ## display the port

if __name__ == "__main__":
    main()
