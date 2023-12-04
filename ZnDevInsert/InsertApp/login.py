from InsertApp import app,CheckForm
from flask import redirect,render_template,make_response,request,session,url_for,g

no_user_url = ['/index']

def login_check(username,pwd):
    if username and pwd:
        if username == 'superadmin' and pwd == '1qaz@WSX':
            return True
    else:
        return False
    
# @app.before_request
# def is_login():
#     if not session.get("username"):
#         url = request.path
#         print(url)
#         print('******************')
#         if request.path=="/index":
#             url = request.path
#             print(url)
#             print('----------------------')
#             return None
#         else:
#             return redirect(url_for('index'))



@app.route('/index',methods=["get","post"])
def index():
    form = CheckForm.LoginForm()
    if form.validate_on_submit():
        username = form.name.data
        password = form.password.data
        CheckOn = login_check(username,password)
        if CheckOn:
            session["username"] = username
            return redirect(url_for('datainsert'))
        else:
            return ('<h1>不对的等录</h1>')
    return render_template('/view/index.html',form=form)


@app.route('/datainsert')
def datainsert():
    if not session.get("username"):
        return redirect(url_for('index'))
    return render_template('/view/datainsert.html')


@app.route('/CLS')
def session_clear():
    session.pop("username",None)
    return ("<h1>清楚session！</h1>")
