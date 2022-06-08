'''
how to use:

given that the url is "host"...
go to "host" for all data
go to "host/star?name={starname}" for info about star with the given name
go to "host/star?index={index}" for info about star with given index in the list of stars
'''

import csv
from flask import Flask, jsonify, request

app = Flask(__name__)

data = list(csv.reader(open("filtered.csv")))

@app.route("/")
def index():
    return jsonify({"message": "success", "data": data})

@app.route("/star")
def get_star():
    name = request.args.get("name")
    index = request.args.get("index")
    print("name", name)
    print("index", index)
    if (index == None and name == None):
        return jsonify({"message": "no name or index provided"})
    if (name == None):
        try: index = int(index)
        except: return(jsonify({"message": "index must be of type int"}))
    if (name == None):
        if (index == 0 or index >= len(data)):
            return jsonify({"message": "not found; if you entered index, it must be min 1 and max {}".format(len(data) - 1)})
    if (index == None):
        for i in range(len(data)):
            if (data[i][0].lower().replace(" ", "") == name.lower().replace(" ", "")):
                index = i
    
    if (index == None):
        return jsonify({"message": "not found"})
    
    return jsonify({"message": "success", "data": get_star_data(index)})

def get_star_data(index):
    star = data[index]
    return {
        "name": star[0],
        "distance": star[1],
        "mass": star[2],
        "radius": star[3],
        "gravity": star[4],
    }

if (__name__ == "__main__"):
    app.run(debug=True)