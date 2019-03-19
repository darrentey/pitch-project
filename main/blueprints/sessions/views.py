from flask import Blueprint, render_template,request,url_for,redirect,flash
from models.user import User
from forms import LoginForm,RegistrationForm
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin,LoginManager,login_required,logout_user,login_user,current_user
from app import app
from main.util.google_auth import oauth
import os

sessions_blueprint = Blueprint('sessions',
                            __name__,
                            template_folder='templates')

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "sessions.login"

@login_manager.user_loader
def load_user(user_id):
    return User.get_or_none(User.id == user_id)

@sessions_blueprint.route("/login", methods=['GET', 'POST'])
def login():
    log_form = LoginForm()
    reg_form = RegistrationForm()
    if request.method == 'POST':
        if reg_form.submit_reg.data and reg_form.validate_on_submit():
            user = User(username=reg_form.username.data,email=reg_form.email.data,password=reg_form.password.data)
            user.save()
            login_user(user)
            # flash(f'Account created for {reg_form.username.data}.', 'success')
            flash('Please select your preferences, so we can start generating content for you.','primary')
            return redirect(url_for('users.edit',id=user.id))
        elif log_form.submit_log.data and log_form.validate_on_submit():
            user = User.get_or_none(User.email == log_form.email.data)
            if user:
                submitted_password = log_form.password.data
                if check_password_hash(user.password, submitted_password):
                    login_user(user)
                    flash('You have been logged in.', 'success')
                    return redirect(url_for('users.show',username=user.username))  
                else:
                    flash('Login unsuccessful. Please use valid password', 'danger')
                    return render_template('combine.html', log_form=log_form,reg_form=reg_form)
            else:
                flash('Login unsuccessful. Please using valid email.', 'danger')
                return render_template('combine.html', log_form=log_form,reg_form=reg_form)
        else:  
            flash('Some fields are invalid. Please try again.','danger')
            return render_template('combine.html', log_form=log_form,reg_form=reg_form)
    elif request.method == 'GET':
        return render_template('combine.html', log_form=log_form,reg_form=reg_form)

@sessions_blueprint.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('home'))

@sessions_blueprint.route("/login/google")
def google_login():
    redirect_uri = url_for('sessions.authorize', _external=True)
    return oauth.google.authorize_redirect(redirect_uri)

@sessions_blueprint.route('/authorize/google')
def authorize():
    token = oauth.google.authorize_access_token()
    response = oauth.google.get('https://www.googleapis.com/oauth2/v2/userinfo').json()
    user = User.get_or_none(User.email == response['email'])
    if user:
        login_user(user)
        flash('You have been logged in.', 'success')
        return redirect(url_for('users.show',username=user.username))  
    # this is a pseudo method, you need to implement it yourself
    else:
        name = oauth.google.get('https://www.googleapis.com/oauth2/v2/userinfo').json()['name']
        user_password = os.urandom(8)
        email = oauth.google.get('https://www.googleapis.com/oauth2/v2/userinfo').json()['email']
        user = User(username=name.lower(),email=email,password=user_password)
        user.save()
        login_user(user)
        flash("Successfully signed up and logged in.","success")
        return redirect(url_for('users.show',username=user.username))