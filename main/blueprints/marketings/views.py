from flask import Blueprint, render_template,request,url_for,redirect,flash
from models.user import User
from flask_login import current_user
from models.preference import Preference
from models.general import General
import json
from random import shuffle

marketings_blueprint = Blueprint('marketings',
                            __name__,
                            template_folder='templates/')



@marketings_blueprint.route("/tips", methods=['GET'])
def show():
    results = []
    marketing = General.get(name='marketing').contents
    for article in marketing:
        results.append(json.loads(article))
    shuffle(results)
    return render_template('marketings/show.html',results=results) 
