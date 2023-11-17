from flask_app.controllers import observation_controller

from flask_app import app
from flask_cors import CORS

CORS(app)

if __name__ == "__main__":
    app.run(debug=True)