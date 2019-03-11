from flask import Blueprint, render_template,request,url_for,redirect,flash
from models.preference import Preference
import json
from main.util.fashion import *
from main.util.tech import *

preferences_blueprint = Blueprint('preferences',
                            __name__,
                            template_folder='templates/')


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