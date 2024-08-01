from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from app.models import User
from flask_login import current_user

class RegistrationForm(FlaskForm):
    username = StringField('Как к Вам обращаться?', validators=[DataRequired(), Length(min=2, max=200)])
    password = PasswordField('Придумайте пароль', validators=[DataRequired(), Length(min=2, max=60)])
    confirm_password = PasswordField('Повторите пароль', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Подтердить')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Такое имя уже занято. Пожалуйста, выберите другое.')


class LoginForm(FlaskForm):
    username = StringField('Логин (обращение)', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')

class UpdateAccountForm(FlaskForm):
    username = StringField('Как к Вам обращаться?', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Пароль')
    confirm_password = PasswordField('Повторите пароль', validators=[EqualTo('password')])
    submit = SubmitField('Сохранить')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Такое имя уже занято. Пожалуйста, выберите другое.')
