from flask import Blueprint, jsonify
from .utils import load_historical_prices, load_change_points, load_key_events

api = Blueprint("api", __name__)

# ---------------------------
# 1. Historical Price Data
# ---------------------------
@api.route("/historical_prices", methods=["GET"])
def historical_prices():
    """
    Returns the Brent log returns as a list of dictionaries.
    """
    df = load_historical_prices()
    return jsonify(df.to_dict(orient="records"))

# ---------------------------
# 2. Change Point Results
# ---------------------------
@api.route("/change_points", methods=["GET"])
def change_points():
    """
    Returns the median change point, 95% CI, and delta in returns.
    """
    df = load_change_points()
    return jsonify(df.to_dict(orient="records"))

# ---------------------------
# 3. Key Events
# ---------------------------
@api.route("/events", methods=["GET"])
def events():
    """
    Returns all key events.
    """
    df = load_key_events()
    return jsonify(df.to_dict(orient="records"))
