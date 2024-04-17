from sqlalchemy import create_engine

from .DBconfig import Test
from sqlalchemy.orm import sessionmaker

# Test env
databasecofig = Test()

# change '@#$%....' password in save mode
# pd = quote_plus(databasecofig.passwd)

# 需要安装mysqlclient 插件，本版本安装的2.2.0
# mysql link "mysql://username:passwd@hostip:port/DBname"
MySqlLink = 'mysql://{0}:{1}@{2}:{3}/{4}'.format(databasecofig.username,databasecofig.passwd,databasecofig.host,databasecofig.port,databasecofig.db)

# engine = create_engine('dialect+driver://username:password@host:port/database')
engine = create_engine(MySqlLink)
# engine = create_engine(MySqlLink,echo=True)

Session = sessionmaker(bind=engine)