from InsertApp import app,Forms,db
from flask import redirect,render_template,make_response,request,session,url_for,g,flash
from InsertApp.Model import ClDevice

neet_login_url = ['/datainsert']

def login_check(username,pwd):
    if username and pwd:
        if username == 'superadmin' and pwd == '1qaz@WSX':
            return True
    else:
        return False


@app.before_request
def BeforeDo():
    if request.path in neet_login_url:
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
            return redirect(url_for('datainsert'))
        else:
            return ('<h1>不对的等录</h1>')
    return render_template('/view/index.html',servername= server_name,form=form)


@app.route('/datainsert',methods=["get","post"])
def datainsert():
    form = Forms.DevdataForms()
    DataResult = db.session.query(ClDevice).all()
    if form.validate_on_submit():
        if form.savepush.data:
            devdata = ClDevice(deviceid=form.deviceid.data,
                                 devname=form.name.data,
                                 type=form.type.data,
                                 serviceid=form.serviceid.data,
                                 charid=form.charid.data)
            db.session.add(devdata)
            db.session.commit()
            flash("提交完成！！！")
        return redirect(url_for('datainsert'))
    return render_template('/view/datainsert.html',form=form,devdata=DataResult)


# @app.route('/CLS')
# def session_clear():
#     session.pop("username",None)
#     return ("<h1>清楚session！</h1>")