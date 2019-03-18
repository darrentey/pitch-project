from flask import Blueprint, render_template,request,url_for,redirect,flash
from models.user import User
from flask_login import current_user,login_required
from models.preference import Preference
from models.general import General
import json
from random import shuffle

marketings_blueprint = Blueprint('marketings',
                            __name__,
                            template_folder='templates/')



@marketings_blueprint.route("/tips", methods=['GET'])
@login_required
def show():
    calendar = General.get(name='calendar').contents
    events = []
    for event in calendar:
        events.append(json.loads(event))
    results = []
    marketing = General.get(name='marketing').contents
    for article in marketing:
        results.append(json.loads(article))
    shuffle(results)
    return render_template('marketings/show.html',results=results,events=events) 
