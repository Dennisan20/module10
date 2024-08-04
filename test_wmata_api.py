# Importing the required items
from wmata_api import app
import json
import unittest


# Creating a class for the test
class WMATATest(unittest.TestCase):
    # Defining the first test as instructed
    def test_http_success(self):
        # Getting the status codes and making sure they match the expected ones
        escalator_response = app.test_client().get('/incidents/escalators').status_code
        self.assertEqual(escalator_response, 200)

        # Getting the status codes and making sure they match the expected ones
        elevator_response = app.test_client().get('/incidents/elevators').status_code
        self.assertEqual(elevator_response, 200)

################################################################################
    # Defining the second test as instructed
    def test_required_fields(self):
        required_fields = ["StationCode", "StationName", "UnitType", "UnitName"]

        # Getting the responses
        response = app.test_client().get('/incidents/escalators')
        json_response = json.loads(response.data.decode())

        # Going through each one
        for incident in json_response:
            for field in required_fields:
                self.assertIn(field, incident)

################################################################################
    # Defining the third test as instructed
    def test_escalators(self):
        # Getting the responses
        response = app.test_client().get('/incidents/escalators')
        json_response = json.loads(response.data.decode())

        # Checking that we get the expected values
        for incident in json_response:
            self.assertEqual(incident["UnitType"], "ESCALATOR")

################################################################################
    # Defining the fourth and final test as instructed
    def test_elevators(self):
        # Getting the responses 
        response = app.test_client().get('/incidents/elevators')
        json_response = json.loads(response.data.decode())

        # Checking that we get the expected values
        for incident in json_response:
            self.assertEqual(incident["UnitType"], "ELEVATOR")

################################################################################


# Running the test
if __name__ == "__main__":
    unittest.main()