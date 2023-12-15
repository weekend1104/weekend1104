from flask  import Flask
from urllib.parse import quote_plus
from InsertApp import MySQLconfig
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__,template_folder='templates',static_folder='Prostatic')
# app.jinja_env.auto_reload = True
# app.config['TEMPLATES_AUTO_RELOAD'] = True

# Test env
DBconfig = MySQLconfig.Test()
app.servername = "Test"
app.mainUrl = "http://www.youtwin.com.cn:19096"


# prod env
# DBconfig = MySQLconfig.Prod()
# app.servername = "Prod"
# app.mainUrl = "https://www.zjzncl.com"


# change '@#$%....' password in save mode
pd = quote_plus(DBconfig.passwd)

# pymysql link "mysql+pymysql://username:passwd@hostip:port/DBname?option"
MySqlLink = 'mysql+pymysql://{0}:{1}@{2}:{3}/{4}?charset={5}'.format(DBconfig.username,pd,DBconfig.host,DBconfig.port,DBconfig.db,DBconfig.chart)

app.config["SECRET_KEY"]="ZXSDFADDKAKJFAKJFDDAHUUYHUH!!!!!@guj2987@DJJJDAJKsjjdjjdaffffg$ddfadfadffadfdfakj@lkjldaf%jkfvkhjvcj@nkdfkjshajkhfdakjhl"
app.config["SQLALCHEMY_DATABASE_URI"] = MySqlLink
app.config["SQLALCHEMY_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)
# db.init_app(app)


from InsertApp  import view

