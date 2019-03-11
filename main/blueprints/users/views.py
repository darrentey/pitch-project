from flask import Blueprint, render_template,request,url_for,redirect,flash
from models.user import User
from forms import RegistrationForm
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin,LoginManager,login_required,logout_user,login_user,current_user

# app.config['SECRET_KEY'] = '6c2895efeef56653c22f29249bb29924'

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