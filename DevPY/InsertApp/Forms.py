from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,SelectMultipleField
from wtforms.validators import DataRequired,InputRequired


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
    WritrCharacteristicId = StringField("WritrCharacteristicId")
    cltype  = SelectMultipleField('type',choices=[('TASK_HNTJGGC_HTQD','混凝土工程-回弹强度'),('TASK_HNTJGGC_CZD','混凝土工程-垂直度'),('TASK_HNTJGGC_JMCC','混凝土工程-截面尺寸'),
                                                  ('TASK_HNTJGGC_LBHD','混凝土工程-楼板厚度'),('TASK_HNTJGGC_BMPZD','混凝土工程-表面平整度'),('TASK_HNTJGGC_GJBHC','混凝土工程-钢筋保护层厚度'),
                                                  ('TASK_QZGC_ZZD','砌筑工程-垂直度'),('TASK_QZGC_MCCC','砌筑工程-外门窗洞口尺寸'),('TASK_QZGC_BMPZD','砌筑工程-表面平整度'),
                                                  ('TASK_MHGC_DMSPDUJZ','抹灰工程-地面水平度极差'),('TASK_MHGC_DM_BMPZD_MP','抹灰工程-地面表面平整度-毛坯'),('TASK_MHGC_DM_BMPZD_ZX','抹灰工程-地面表面平整度-装修'),
                                                  ('TASK_MHGC_QMCZD_PT','抹灰工程-墙面垂直度-普通抹灰'),('TASK_MHGC_QMCZD_GJ','抹灰工程-墙面垂直度-高级抹灰'),('TASK_MHGC_QM_BMPZD_PT','抹灰工程-墙面表面平整度-普通抹灰'),
                                                  ('TASK_MHGC_QM_BMPZD_GJ','抹灰工程-墙面表面平整度-高级抹灰'),('TASK_MHGC_WQCMNCQTHDJC','抹灰工程-外墙窗内侧墙体厚度极差'),('TASK_MHGC_HNMDCCPC','抹灰工程-户内门洞尺寸偏差'),
                                                  ('TASK_MHGC_FJKJJS','抹灰工程-房间开间/进深'),('TASK_MHGC_YYJFZ','抹灰工程-阴阳角方正')],validators=[InputRequired()])
    savepush = SubmitField('提交')

