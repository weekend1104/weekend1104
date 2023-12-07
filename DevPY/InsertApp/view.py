from InsertApp import app,db
from InsertApp import Forms
from flask import redirect,render_template,make_response,request,session,url_for,g,flash
from InsertApp.Model import ClDevice

auth_url = ['/datainsert','/delinfo']

def login_check(username,pwd):
    if username and pwd:
        if username == 'superadmin' and pwd == '1qaz@WSX':
            return True
    else:
        return False


@app.before_request
def BeforeDo():
    if request.path in auth_url:
        if not session.get("username"):
            return redirect(url_for('index'))



@app.route('/index',methods=["get","post"])
def index():
    server_name = app.servername
    form = Forms.LoginForm()
    if form.validate_on_submit():
        username = form.name.data
        password = form.password.data
        CheckOn = login_check(username,password)
        if CheckOn:
            session["username"] = username
            return redirect(url_for('devinfo'))
        else:
            return redirect(url_for('index'))
    return render_template('/view/index.html',servername= server_name,form=form)


@app.route('/devinfo',methods=["GET","POST"])
def devinfo():
    form = Forms.DevDataIn()
    # 字符串+0 可以让字符串按照数字排序
    DataResult = db.session.query(ClDevice).order_by(ClDevice.deviceid+0).all()
    if request.method=="POST":
        if form.validate_on_submit():
            if form.savepush.data:
                devdata = ClDevice(deviceid=form.deviceid.data,
                                    devname=form.name.data,
                                    type=form.type.data,
                                    serviceid=form.serviceid.data,
                                    charid=form.charid.data,
                                    startSampling=form.startSampling.data,
                                    endSampling=form.endSampling.data
                                    )
                try:
                    db.session.add(devdata)
                    db.session.commit()
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
