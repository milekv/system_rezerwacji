from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/system.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.DateTime, nullable=False)
    end_date = db.Column(db.DateTime, nullable=False)
    resource = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Reservation {self.name}>"

@app.route('/')
def index():
    reservations = Reservation.query.all()
    return render_template('index.html', reservations=reservations)

@app.route('/reservation', methods=['GET', 'POST'])
def create_reservation():
    if request.method == 'POST':
        name = request.form['name']
        start_date = datetime.strptime(request.form['start_date'], '%Y-%m-%d')
        end_date = datetime.strptime(request.form['end_date'], '%Y-%m-%d')
        resource = request.form['resource']

        new_reservation = Reservation(name=name, start_date=start_date, end_date=end_date, resource=resource)
        db.session.add(new_reservation)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('reservation.html')

@app.route('/delete/<int:id>')
def delete_reservation(id):
    reservation_to_delete = Reservation.query.get_or_404(id)
    db.session.delete(reservation_to_delete)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
