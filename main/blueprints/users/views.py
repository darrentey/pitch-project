from flask import Blueprint, render_template,request,url_for,redirect,flash
from models.user import User
from forms import RegistrationForm
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin,LoginManager,login_required,logout_user,login_user,current_user
from models.preference import Preference
import json

users_blueprint = Blueprint('users',
                            __name__,
                            template_folder='templates/')



@users_blueprint.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(
            username=form.username.data,
            email=form.email.data,
            password=generate_password_hash(form.password.data)
        )
        new_user.save()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('signup.html', title='Register', form=form)

@users_blueprint.route("/dashboard", methods=['GET'])
def dashboard():
    results = []
    tech = Preference.get(id=1)
    for article in tech.articles:
        results.append(json.loads(article))
    return render_template('show.html',results=results) 