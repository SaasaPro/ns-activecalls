from flask import Flask, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # habilita CORS globalmente

API_URL = "https://portal4.myvrv.com/ns-api/domains/verve.myvrv.com/calls"
ACCESS_TOKEN = "nss_LJ4V1HYTyfFk2LMWZlTwMKCKKz1WplCT9sgNySFdeno6r8Kx349dee24"

@app.route("/active-calls")
def active_calls():
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Accept": "application/json"
    }
    response = requests.get(API_URL, headers=headers)
    response.raise_for_status()
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(debug=True)
