from flask import Flask, render_template, redirect, session, url_for, request
from lossWeight import lossWeight
from muscleGain import muscleGain
import os


app = Flask(__name__)

app.register_blueprint(lossWeight, url_prefix="/lossWeight")
app.register_blueprint(muscleGain, url_prefix="/muscleGain")

picFolder = os.path.join('static', 'images')
app.config['UPLOAD_FOLDER'] = picFolder

app.secret_key = 'dsadsa'



@app.route('/')
def home():
    if 'username' in session:
        return render_template('home.html', username=session.get('username'))
    else:
        return render_template('home.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    logo = os.path.join(app.config['UPLOAD_FOLDER'], 'Logo.png')
    if request.method == "POST":
        username = request.form['username']
        fullname = request.form['fullname']
        # pwd = request.form['password']
        injuries = request.form['injuries']
        injuries2 = request.form['injuries2']
        exercise = request.form['exercise']
        
        # Check if either injuries or injuries2 is set to "yes"
        if injuries == "yes" or injuries2 == "yes":
            # If yes, return some message or redirect back to the registration page
            return render_template('register.html', not_allowed="Sorry, registration not allowed for users with injuries", logo = logo)
        
        # If neither injuries nor injuries2 is set to "yes", proceed with registration
        session['username'] = username
        session['fullname'] = fullname
        session['exercise'] = exercise
        
        return redirect(url_for('home'))
    
    return render_template('register.html', logo = logo)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route('/start_exercise')
def start_exercise():
    # ----------------------- FOR GAINING MUSCLE ------------------------------
    session['bicep_curl'] = os.path.join(app.config['UPLOAD_FOLDER'], 'bicep_curl.jpg')
    session['push_up'] = os.path.join(app.config['UPLOAD_FOLDER'], 'Pushups.jpg')
    session['shoulder_tap'] = os.path.join(app.config['UPLOAD_FOLDER'], 'shoulder_tap.jpg')
    session['dumbbell_frontraise'] = os.path.join(app.config['UPLOAD_FOLDER'], 'dumbbell_frontraise.jpg')
    session['chest_press'] = os.path.join(app.config['UPLOAD_FOLDER'], 'chest_press.jpg')
    session['alternatingleglunges'] = os.path.join(app.config['UPLOAD_FOLDER'], 'alternatingleglunges.jpg')
    session['bodyweightsquat'] = os.path.join(app.config['UPLOAD_FOLDER'], 'bodyweightsquat.jpg')
    session['dumbbellhiphinge'] = os.path.join(app.config['UPLOAD_FOLDER'], 'dumbbellhiphinge.jpg')
    session['gobletsquat'] = os.path.join(app.config['UPLOAD_FOLDER'], 'gobletsquat.jpg')
    session['highkneetap'] = os.path.join(app.config['UPLOAD_FOLDER'], 'highkneetap.jpg')
    # -------------------------- END FOR GAINING MUSCLE -------------------------

    # -------------------------- FOR LOSS WEIGHT -------------------------------
    session['buttkicks'] = os.path.join(app.config['UPLOAD_FOLDER'], 'buttkicks.jpg')
    session['joginplace'] = os.path.join(app.config['UPLOAD_FOLDER'], 'joginplace.jpg')
    session['jumpingjacks'] = os.path.join(app.config['UPLOAD_FOLDER'], 'jumpingjack.jpg')
    session['jumpinglunges'] = os.path.join(app.config['UPLOAD_FOLDER'], 'jumpinglunges.jpg')
    session['plankjacks'] = os.path.join(app.config['UPLOAD_FOLDER'], 'plankjacks.jpg')
    session['planktoetaps'] = os.path.join(app.config['UPLOAD_FOLDER'], 'planktoetaps.jpg')
    session['sidelegraise'] = os.path.join(app.config['UPLOAD_FOLDER'], 'sidelegraise.jpg')
    session['squatjacks'] = os.path.join(app.config['UPLOAD_FOLDER'], 'squatjacks.jpg')
    session['squatjump'] = os.path.join(app.config['UPLOAD_FOLDER'], 'squatjump.jpg')
    session['squatsidekick'] = os.path.join(app.config['UPLOAD_FOLDER'], 'squatsidekick.jpg')
    # -------------------------- END FOR LOSS WEIGHT ---------------------------

    if session['exercise'] == "muscle_gain":
        return redirect("/muscleGain")
    else:
        return redirect("/lossWeight")


if __name__ == "__main__":
    app.run(debug=True)