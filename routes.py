from flask import render_template, session, redirect, url_for, flash
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from api.user.model import User
from api.role.model import Role


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')

def initialize_routes(app):

    @app.route('/', methods=['GET', 'POST'])
    def index():
        db = app.get('db')
        form = NameForm()
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.name.data).first()
            if user is None:
                user = User(username=form.name.data)
                db.session.add(user) 
                db.session.commit()
                session['known'] = False
            else:
                session['known'] = True
            session['name'] = form.name.data
            form.name.data = ''
            return redirect(url_for('index'))

        return render_template('index.html', form=form, name=session.get('name'), known=session.get('known',False))

    @app.route('/user', defaults={'name': None})
    @app.route('/user/<string:name>')
    def user(name):
        return render_template('user.html', name=name)

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def internal_server_error(e):
        return render_template('500.html'), 500
