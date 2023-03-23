from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import check_password_hash, generate_password_hash

from blog.database import db
from blog.forms.users import UserRegisterForm
from blog.models import User
from flask_login import logout_user, login_user, login_required, current_user

auth = Blueprint('auth', __name__, static_folder='../static')


@auth.route('/login', methods=('GET',))
def check_login():
    if current_user.is_authenticated:
        return redirect(url_for('user.profile', pk=current_user.id))

    return render_template(
        'auth/login.html',
    )


@auth.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('auth/login.html')

    email = request.form.get('email')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    if not check_password_hash(user.password, password):
        flash('Check your login details')
        return redirect(url_for('.login'))
    login_user(user)
    return redirect(url_for('user.profile', pk=user.id))


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('.login'))


@auth.route('/registration', methods=['GET', 'POST'])
def registration():
    if current_user.is_authenticated:
        return redirect(url_for('user.profile', pk=current_user.id))

    form = UserRegisterForm(request.form)
    errors = []
    if request.method == "POST" and form.validate_on_submit():
        if User.query.filter_by(email=form.email.data).count():
            form.email.errors.append('User with this email already exists!')
            return render_template('users/registration.html', form=form)
        user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            password=generate_password_hash(form.password.data),
        )
        db.session.add(user)
        db.session.commit()
        login_user(user)

    return render_template('auth/registration.html', form=form, errors=errors)
