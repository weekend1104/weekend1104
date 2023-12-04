from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired


class  LoginForm(FlaskForm):
    name = StringField("账户名称：",validators=[DataRequired()])
    password = PasswordField("密码：",validators=[DataRequired()])
    submit = SubmitField('Submit')

class  DevdataForms(FlaskForm):
    deviceid = StringField("MAC地址",validators=[DataRequired()])
    name = StringField("设备名称",validators=[DataRequired()])
    type = StringField("设备类型",validators=[DataRequired()])
    serviceid = StringField("UUID",validators=[DataRequired()])
    charid = StringField("蓝牙特征值",validators=[DataRequired()])
    savepush = SubmitField('提交')
