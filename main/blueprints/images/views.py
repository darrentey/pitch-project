from flask import Blueprint, render_template
import requests
from app import app

images_blueprint = Blueprint('images',
                            __name__,
                            template_folder='templates/')

@images_blueprint.route("/show", methods=['GET'])
def show():
    unsplash = app.config['UNSPLASH_ID']
    return render_template('search.html', unsplash=unsplash)
