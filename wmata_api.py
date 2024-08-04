import json
import requests
from flask import Flask

# API endpoint URL's and access keys
WMATA_API_KEY = "153e4b63fa3b42db9d456151798986cc"
INCIDENTS_URL = "https://api.wmata.com/Incidents.svc/json/ElevatorIncidents"
headers = {"api_key": WMATA_API_KEY, 'Accept': '*/*'}

################################################################################

app = Flask(__name__)


# Defining the incidents based on the format given
@app.route("/incidents/<unit_type>", methods=["GET"])
def get_incidents(unit_type):
    # Creating an empty incidents dictionary
    incidents = []

    # Retrieving the responses
    response = requests.get(INCIDENTS_URL, headers=headers)
    json_response = response.json()

    # Going through each response and adding it to the incidents dictionary
    for stuff in json_response["ElevatorIncidents"]:
        if stuff["UnitType"] == unit_type[:-1].upper():
            incident = {}
            incident["StationCode"] = stuff["StationCode"]
            incident["StationName"] = stuff["StationName"]
            incident["UnitType"] = stuff["UnitType"]
            incident["UnitName"] = stuff["UnitName"]
            incidents.append(incident)

    # Returning the incidents
    return json.dumps(incidents)


# Running the file
if __name__ == '__main__':
    app.run(debug=True) 
