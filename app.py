import os
import config
from flask import Flask, render_template, request
from models.base_model import db
from flask_wtf.csrf import CSRFProtect

web_dir = os.path.join(os.path.dirname(
    os.path.abspath(__file__)), 'main')

app = Flask('CON-TEMP', root_path=web_dir)
csrf = CSRFProtect(app)

if os.getenv('FLASK_ENV') == 'production':
    app.config.from_object("config.ProductionConfig")
else:
    app.config.from_object("config.DevelopmentConfig")

@app.before_request
def before_request():
    db.connect()

@app.teardown_request
def _db_close(exc):
    if not db.is_closed():
        print(db)
        print(db.close())
    return exc

@app.route("/") 
def home():
    return render_template('home.html')

@app.errorhandler(401)
def unauthorized(e):
    return render_template('401.html'), 401

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(e):
    return render_template('500.html'), 500
