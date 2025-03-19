from flask import Flask, render_template, request, redirect
from models import db, User
import re

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # Change for your DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    email = request.form["email"]
    phone = request.form["phone"]

    # Server-side validation
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    phone_pattern = r"^\d{10}$"

    if not re.match(email_pattern, email):
        return "Invalid email format!", 400
    if not re.match(phone_pattern, phone):
        return "Phone number must be exactly 10 digits!", 400

    # Save to database
    new_user = User(name=name, email=email, phone=phone)
    db.session.add(new_user)
    db.session.commit()

    return "Form submitted successfully!"

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Ensure tables are created
    app.run(debug=True)

