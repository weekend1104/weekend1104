from InsertApp import app,db
import requests
from requests.auth import HTTPBasicAuth
from InsertApp import Forms
from flask import redirect,render_template,make_response,request,session,url_for,g,flash
from InsertApp.Model import ClDevice

auth_url = ['/devinfo','/delinfo']

def login_check(username,pwd):
    url = app.mainUrl + "/smart-bee/curr-user-info/admin/"
    auth = HTTPBasicAuth(username,pwd)
    response = requests.request("GET", url, auth=auth)
    # if username and pwd:
    #     if username == 'superadmin' and pwd == '1qaz@WSX3edc':

    if response.status_code == 200:
        return True
    else:
        return False


@app.before_request
def BeforeDo():
    if request.path in auth_url:
        if session.get("is_login"):
            return None
        else:
            return redirect(url_for('login'))



@app.route('/login',methods=["get","post"])
def login():
    session["is_login"] = False
    server_name = app.servername
    form = Forms.LoginForm()
    if form.validate_on_submit():
        username = form.name.data
        password = form.password.data
        CheckOn = login_check(username,password)
        if CheckOn:
            session["username"] = username
            session["is_login"] = True
            return redirect(url_for('devinfo'))
        else:
            flash("账户名或密码错误！")
            return redirect(url_for('login'))
    return render_template('/view/login.html',servername= server_name,form=form)


@app.route('/devinfo',methods=["GET","POST"])
def devinfo():
    form = Forms.DevDataIn()
    # 字符串+0 可以让字符串按照数字排序
    DataResult = db.session.query(ClDevice).order_by(ClDevice.deviceid+0).all()
    devtasks = {}
    if request.method=="POST":
        print('没有按钮！')
    if form.validate_on_submit():
        if form.savepush.data:
            devtasks["cltasks"]=form.cltype.data
            devdata = ClDevice(deviceid=form.deviceid.data,
                                    devname=form.name.data,
                                    type=form.type.data,
                                    serviceid=form.serviceid.data,
                                    charid=form.charid.data,
                                    startSampling=form.startSampling.data,
                                    endSampling=form.endSampling.data,
                                    writrCharacteristicId=form.WritrCharacteristicId.data,
                                    devtasktype=devtasks
                                    )
            print(devtasks["cltasks"])
            print('有按按钮NNNNNNNNNNNNNNNNNNNNNNNN！')
            try:
                db.session.add(devdata)
                # db.session.commit()
                flash("提交完成！！！")
            except BaseException:
                db.session.rollback()
                flash("提交失败！！！")
        return redirect(url_for('devinfo'))
        
    return render_template('/view/devinfo.html',form=form,devdata=DataResult)

@app.route('/deldev',methods=["POST"])
def deldev():
    if request.method=="POST":
        devdata = request.get_json()
        devid = devdata.get('devid')
        dataresult = ClDevice.query.filter_by(deviceid=devid).first()
        try:
            db.session.delete(dataresult)
            db.session.commit()
            responsejson = {
                "message":'Data is delete!',
                "code":200
            }
            response = make_response(responsejson)
        except BaseException:
            db.session.rollback()
            responsejson = {
                "message":'Data Roll Back!',
                "code":500
            }
            response = make_response(responsejson)
        return response

@app.route('/getdevinfoById',methods=["POST"])
def getdevinfoById():
    if request.method=="POST":
        devdata = request.get_json()
        devid = devdata.get('devid')
        dataresult = ClDevice.query.filter_by(deviceid=devid).first()
        print(dataresult)

# @app.route('/devinsert',methods=["POST"])
# def devinsert():
#     form = Forms.DevDataIn()
#     devtasks = {}

#     res = request.get_json()
#     devid = res.get('devid')

#     form.deviceid.data=
#     form.name.data=
#     form.type.data=
#     form.serviceid.data=
#     form.charid.data=
#     form.startSampling.data=
#     form.endSampling.data=
#     form.WritrCharacteristicId.data=

#     if request.method=="POST":
#         devtasks["cltasks"]=form.cltype.data
#         devdata = ClDevice(deviceid=form.deviceid.data,
#                             devname=form.name.data,
#                             type=form.type.data,
#                             serviceid=form.serviceid.data,
#                             charid=form.charid.data,
#                             startSampling=form.startSampling.data,
#                             endSampling=form.endSampling.data,
#                             writrCharacteristicId=form.WritrCharacteristicId.data,
#                             devtasktype=devtasks
#                             )
#         try:
#             db.session.add(devdata)
#             db.session.commit()
#             flash("更新完成！！！")
#         except BaseException:
#             db.session.rollback()
#             flash("更新失败！！！")
#     return redirect(url_for('devinfo'))