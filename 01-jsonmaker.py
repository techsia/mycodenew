#!/usr/bin/python3
"""Author: SK | Learning Json w/ Python | Dept: DevOps"""

# with python, the jsonbatteries are in the box, but you need to plug them in
import json
def main():
    # create a list of dictionaries
    videogames = [{"game1": "PacMan" , "game2": "Maat Light" , "game3": "Starcaft", "game4": "faster than light"}, {"game1": "paperboy", "game2": "donkey kong"}]

    # show the vaulues of videogames
    print(videogames)

    # create a local file  ; can put filename or fullpath
    with open("videogames.json", "w") as vidfile: #"w" = write, "r" = read, "a" = append
        json.dump(videogames, vidfile)


if __name__ == "__main__":
    main()

