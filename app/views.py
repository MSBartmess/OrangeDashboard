from app import app
from flask import render_template, flash, redirect
from .forms import LoginForm
import json
import pickle
'''
Things that need to be done:
Bus Route Viewer
  Google Maps View
  CUMTD api request + plot
  Estimated time list
Weather Viewer
  Api Request
  Display
Calendar
  Calandar view
  Backend Calendar
  showing by person
Smart Home Status
  Philips Hue Light Status
  Roomba Dustbin
  Whos Home
'''
@app.route('/')
@app.route('/index')
def index():
	return render_template('index.html')

@app.route('/getSmarthomeData')
def getSmarthomeData():
  try:
    apartmentHistory = pickle.load(open( "apartmentHistory.pkl", "rb" ))
  except:
    return "Failure"
  listVers = []
  for room in apartmentHistory["roomHistory"]:
    listVers.append({"room":room,"utilization":len([val for val in apartmentHistory["roomHistory"][room] if val==True])*1.0/len(apartmentHistory["roomHistory"][room])})
  apartmentHistory["roomHistory"]=listVers
  return json.dumps(apartmentHistory)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' %
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html', 
                           title='Sign In',
                           form=form,
                           providers=app.config['OPENID_PROVIDERS'])