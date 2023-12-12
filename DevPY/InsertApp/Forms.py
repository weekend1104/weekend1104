from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired


class  LoginForm(FlaskForm):
    name = StringField("账户名称：",validators=[DataRequired()])
    password = PasswordField("密码：",validators=[DataRequired()])
    submit = SubmitField('Submit')


class  DevDataIn(FlaskForm):
    deviceid = StringField("MAC地址")
    name = StringField("设备名称")
    type = StringField("设备类型")
    serviceid = StringField("UUID",validators=[DataRequired()])
    charid = StringField("蓝牙特征值")
    startSampling = StringField("开始命令")
    endSampling = StringField("结束命令")
    savepush = SubmitField('提交')

