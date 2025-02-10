import os
from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename

from portfolio_tracker.src.services.portfolio_service import process_portfolio

portfolio_bp = Blueprint("portfolio", __name__)

UPLOAD_FOLDER = "data"
ALLOWED_EXTENSIONS = {"csv"}


def allowed_file(filename):
    if "." in filename and filename.split(".")[-1] in ALLOWED_EXTENSIONS:
        return True
    else:
        return False


@portfolio_bp.route("/upload", methods=["POST"])
def upload_portfolio():
    if "file" not in request.files:
        return jsonify(
            {
                "error": "No file part"
            }
        ), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify(
            {
                "error": "No selected file"
            }
        ), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        file.save(filepath)

        # Process the portfolio data
        result = process_portfolio(filepath)
        return jsonify(result), 200

    return jsonify(
        {
            "error": "Invalid file format. Only csv allowed."
        }
    ), 400
