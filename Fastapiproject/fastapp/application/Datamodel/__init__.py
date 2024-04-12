from sqlalchemy import create_engine
from urllib.parse import quote_plus
from .DBconfig import Test
from sqlalchemy.orm import sessionmaker

# Test env
databasecofig = Test()

# change '@#$%....' password in save mode
pd = quote_plus(databasecofig.passwd)

# 需要安装mysqlclient 插件，本版本安装的2.2.0
# mysql link "mysql://username:passwd@hostip:port/DBname"
MySqlLink = 'mysql://{0}:{1}@{2}:{3}/{4}'.format(databasecofig.username,pd,databasecofig.host,databasecofig.port,databasecofig.db)


engine = create_engine(MySqlLink,echo=True)

Session = sessionmaker(bind=engine)