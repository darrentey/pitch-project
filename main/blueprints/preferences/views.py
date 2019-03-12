from flask import Blueprint, render_template,request,url_for,redirect,flash
from models.preference import Preference
import json
from main.util.fashion import *
from main.util.tech import *
from main.util.beauty import *
from main.util.lifestyle import *
from models.user_preference import User_Preference
from flask_login import current_user
from main.util.general import *

preferences_blueprint = Blueprint('preferences',
                            __name__,
                            template_folder='templates/')

from main.util.general import *
@preferences_blueprint.route("/general")
def general():
    insta_tag()
    twitter_tag()
    return redirect(url_for('home'))

@preferences_blueprint.route("/fashion")
def fashion_job():
    scrape_f1()
    scrape_f2()
    scrape_f3()
    scrape_f4()
    scrape_f5()
    scrape_f6()
    scrape_f7()
    scrape_f8()
    scrape_f9()
    scrape_f10()
    Preference.update(articles=fashion_result).where(Preference.categories=='Fashion').execute()
    return redirect(url_for('home'))

@preferences_blueprint.route("/tech")
def tech_job():
    scrape_t1()
    scrape_t2()
    scrape_t3()
    scrape_t4()
    scrape_t5()
    scrape_t6()
    scrape_t7()
    scrape_t8()
    scrape_t9()
    scrape_t10()
    Preference.update(articles=tech_result).where(Preference.categories=='Technology').execute()
    return redirect(url_for('home'))

@preferences_blueprint.route("/beauty")
def beauty_job():
    scrape_b1()
    scrape_b2()
    scrape_b3()
    scrape_b4()
    scrape_b5()
    scrape_b6()
    scrape_b7()
    scrape_b8()
    scrape_b9()
    scrape_b10()
    Preference.update(articles=beauty_result).where(Preference.categories=='Beauty').execute()
    return redirect(url_for('home'))

@preferences_blueprint.route("/lifestyle")
def lifestyle_job():
    scrape_l1()
    scrape_l2()
    scrape_l3()
    scrape_l4()
    scrape_l5()
    scrape_l6()
    scrape_l7()
    scrape_l8()
    scrape_l9()
    scrape_l10()
    Preference.update(articles=lifestyle_result).where(Preference.categories=='Lifestyle').execute()
    return redirect(url_for('home'))
    
@preferences_blueprint.route("/new/<int:id>",methods=['POST'])
def add(id):
    preference =  Preference.get(id=id)
    add = User_Preference(user=current_user.id,preference=id)
    if add.save():
            flash(f"You have added {preference.categories} to your preference list.","primary")
            return redirect(url_for('users.edit'))
    else:
        flash(f"Unable to add {preference.categories} to your preference list. Please try again later.","danger")
        return redirect(url_for('users.edit'))

@preferences_blueprint.route("/remove/<int:id>",methods=['POST'])
def remove(id):
    preference =  Preference.get(id=id)
    remove = User_Preference.delete().where(User_Preference.user==current_user.id,User_Preference.preference==id)
    if remove.execute():
        flash(f"You have removed {preference.categories} from your preference list.","primary")
        return redirect(url_for('users.edit'))
    else:
        flash(f"Unable to remove {preference.categories} from your preference list. Please try again later.","danger")
        return redirect(url_for('users.edit'))