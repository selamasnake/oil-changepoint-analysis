# from flask import Flask
# from api.routes import api

# app = Flask(__name__)
# app.register_blueprint(api, url_prefix="/api")

# @app.route("/")
# def home():
#     return "<h1>Welcome to Brent Oil Dashboard API</h1><p>Use /api/... endpoints.</p>"

# if __name__ == "__main__":
#     app.run(debug=True)
from flask import Flask
from flask_cors import CORS
from api.routes import api

app = Flask(__name__)
CORS(app)  # <-- This allows all origins by default

app.register_blueprint(api, url_prefix="/api")

@app.route("/")
def home():
    return "<h1>Welcome to Brent Oil Dashboard API</h1><p>Use /api/... endpoints.</p>"

if __name__ == "__main__":
    app.run(debug=True)
