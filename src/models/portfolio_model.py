from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Portfolio(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stock_symbol = db.Column(db.String(10), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    purchase_price = db.Column(db.Float, nullable=False)
    purchase_date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f"<Portfolio {self.stock_symbol}>"
