from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired


class  LoginForm(FlaskForm):
    name = StringField("账户名称：",validators=[DataRequired()])
    password = PasswordField("密码：",validators=[DataRequired()])
    submit = SubmitField('Submit')
