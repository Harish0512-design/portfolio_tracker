from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from src.routes.portfolio import portfolio_bp

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///portfolio.db"
app.config["UPLOAD_FOLDER"] = "data"

db = SQLAlchemy(app)

app.register_blueprint(portfolio_bp, url_prefix="/api")

if __name__ == "__main__":
    # while running app in production (debug=False)
    app.run(debug=True)
