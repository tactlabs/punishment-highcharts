from flask import Flask,render_template, jsonify, request
import random
import json
import punish


app  = Flask(__name__)
PORT = 3000

@app.route("/", methods=["GET","POST"])
def startpy():

    result = {

        "Greetings" : "Tactlabs welcomes you"
    }

    # return jsonify(result)
    return render_template("index.html") 

'''
http://0.0.0.0:3000/api/data
'''

@app.route("/api/data", methods=["GET"])
def api_get_data():

    result = punish.get_data()

    # result_dict = {

    #     'Country'       : Country,
    #     'Punishment_Percent'    : Punishment_Severity_Percent,
    

    # }

    return jsonify(result)

'''
http://0.0.0.0:3000/api/add

'''
@app.route("/api/add", methods=["GET"])
def api_add_data():

    Country          = request.values.get('Country')
    Punishment_Percent   = request.values.get('Punishment_Severity_Percent')

    result = {
        'Country '          : Country,
        'Punishment_Percent' : Punishment_Percent,
    }
    result_data = punish.add_row(Country, Punishment_Percent)

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug = True,host="0.0.0.0",port = PORT)