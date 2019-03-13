from flask import Blueprint, render_template,request,url_for,redirect,flash
from models.user import User
from forms import RegistrationForm
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin,LoginManager,login_required,logout_user,login_user,current_user
from models.preference import Preference
from models.user_preference import User_Preference
from models.general import General
import json
from random import shuffle

users_blueprint = Blueprint('users',
                            __name__,
                            template_folder='templates/')



@users_blueprint.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data
        )
        user.save()
        login_user(user)
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('users.show',username=user.username))
    return render_template('signup.html', form=form)

@users_blueprint.route("/<username>", methods=['GET'])
def show(username):
    insta_tag = General.get(name='instagram').contents
    twitter_tag = General.get(name='twitter').contents
    calendar = General.get(name='calendar').contents
    p_list = User_Preference.get_or_none(User_Preference.user==current_user.id)
    events = []
    for event in calendar:
        events.append(json.loads(event))
    if p_list:
        results = []
        p_id = User_Preference.select(User_Preference.preference).where(User_Preference.user==current_user.id)
        preferences = Preference.select().where(Preference.id.in_(p_id))
        for preference in preferences:
            for article in preference.articles:
                json_article = json.loads(article)
                json_article['category']=preference.categories
                results.append(json_article)
        shuffle(results)
        return render_template('show.html',results=results,insta_tag=insta_tag,twitter_tag=twitter_tag,events=events) 
    else:
        results = []
        preferences = Preference.select()
        for preference in preferences:
            for article in preference.articles:
                json_article = json.loads(article)
                json_article['category']=preference.categories
                results.append(json_article)
        shuffle(results)
        return render_template('show.html',results=results,insta_tag=insta_tag,twitter_tag=twitter_tag,events=events) 

@users_blueprint.route("/edit/<int:id>", methods=['GET'])
def edit(id):
    if current_user.id==id:
        user = User.get(User.id==id)
        p_list = User_Preference.get_or_none(User_Preference.user==user.id)
        if p_list:
            p_id = User_Preference.select(User_Preference.preference).where(User_Preference.user==user.id)
            preferences = Preference.select().where(Preference.id.in_(p_id))
            not_preferences = Preference.select().where(Preference.id.not_in(p_id))
            return render_template('edit.html',user=user,not_preferences=not_preferences,preferences=preferences) 
        else:
            not_preferences = Preference.select()
            return render_template('edit.html',user=user,not_preferences=not_preferences) 
    return render_template('401.html'), 401  

@users_blueprint.route('/<int:id>', methods=['POST'])
def update(id):
    if current_user.id==id:
        user = User.get(User.id == id)
        user_password = request.form['password']
        user.username = request.form['username']
        user.email = request.form['email']
        user.password = user_password
        user.save()
        flash("Successfully updated.","primary")
        return redirect(url_for('users.edit',id=id))
    else:
        return render_template('edit.html',errors=user.errors,user=user)
    return render_template('401.html'), 401 

@users_blueprint.route("/carousel") 
def carousel():
    return render_template('carousel.html')
