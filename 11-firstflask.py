#/user/bin/python3

from flask import Flask # lowcase is the name of the library; upper is a Class inside of the library

app = Flask(__name__) # must include this

@app.route('/') #decorator # when go goto the ROOT of your sere.. do the following
def endoftheday(): # function to trigger at ROOT
    return "Class is nearing the end for Wednesday" #RETURN this if you goto ROOT


@app.route("/hello/<name>", defaults={'position': 'Administrative Assistant'}) #intro to passing data 
#whatever data user gives here will pass the the function on the def line
def hellostudents(name, position):
    return "Hello {1} {0} I am please to meet to you {0}".format(name, position)
    # return "Welcom to class" +name

if __name__ == "__main__":
    app.run(port=5006) # run on port 5006
