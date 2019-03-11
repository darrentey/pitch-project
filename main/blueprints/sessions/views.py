from flask import Blueprint, render_template,request,url_for,redirect,flash
from models.user import User
from forms import LoginForm
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin,LoginManager,login_required,logout_user,login_user,current_user
from app import app
from main.util.google_auth import oauth

sessions_blueprint = Blueprint('sessions',
                            __name__,
                            template_folder='templates')

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "sessions.new"

@login_manager.user_loader
def load_user(user_id):
    return User.get_or_none(User.id == user_id)

@sessions_blueprint.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        submitted_password = form.password.data
        user = User.get_or_none(User.email == form.email.data)
        if check_password_hash(user.password, submitted_password):
            login_user(user)
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))  
        else:
             flash('Login unsuccessful. Please check username and password', 'danger')   
    return render_template('login.html', title='Login', form=form)

@sessions_blueprint.route('/logout')
@login_required
def logout():
	logout_user()
	flash("You've been logged out!", "success")
	return redirect(url_for('home'))

@sessions_blueprint.route("/login/google")
def google_login():
    redirect_uri = url_for('sessions.authorize', _external=True)
    return oauth.google.authorize_redirect(redirect_uri)

@sessions_blueprint.route('/authorize/google')
def authorize():
    token = oauth.google.authorize_access_token()
    response = oauth.google.get('https://www.googleapis.com/oauth2/v2/userinfo').json()
    print(response)
    user = User.get_or_none(User.email == response['email'])
    if user:
        login_user(user)
        flash('You have been logged in!', 'success')
        return redirect(url_for('home'))  
    # this is a pseudo method, you need to implement it yourself
    return redirect(url_for('home'))