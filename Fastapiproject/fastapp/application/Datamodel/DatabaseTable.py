from sqlalchemy import MetaData,Column,Table,Integer,String,Date,ForeignKey,Boolean,Float
from Datamodel import engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base1 = declarative_base()
metaobject = MetaData()

# fuckyou_table = Table(
#     "fuckyoutable",metaobject,
#     Column("id",Integer,primary_key=True),
#     Column("name",String(128)),
#     Column('date',Date,nullable=False),
#     Column('brithday',Date,nullable=False)
# )


class warehouse(Base1):
    __tablename__ = 'warehouse'

    id = Column(Integer,primary_key=True)
    name = Column(String(128),nullable=True)
    ## server_default 作用在mysql数据层面，创建表时想要默认值即可设置，只接受字符串
    ## default 作用在python 类的层面，以类做为对象并插入值时，default会自动插入该设定的默认值
    location = Column(String(255))
    username = Column(String(128),nullable=True)
    comment = Column(String(128))
    enabled = Column(Boolean,server_default='1')

class Items(Base1):
    __tablename__ = 'items'

    id = Column(Integer,primary_key=True)
    itmename = Column(String(128),nullable=False)
    comment = Column(String(128))
    enabled = Column(Boolean,server_default='1')

class ItemSpec(Base1):
    __tablename__ = 'item_spec'

    id = Column(Integer,primary_key=True)
    spcname = Column(String(128),nullable=False)
    comment = Column(String(128))
    low = Column(Integer,server_default='0')
    # 特别注意，外键对应的 表名.列名，不是类名.属性名
    itemid = Column(Integer,ForeignKey('items.id'))
    enabled = Column(Boolean,server_default='1')

class Inventory(Base1):
    __tablename__ = 'inventory'

    id = Column(Integer,primary_key=True)
    warehouseid = Column(Integer,ForeignKey("warehouse.id"))
    specid = Column(Integer,ForeignKey("item_spec.id"))
    quantity = Column(Float,server_default='0.00')



#利用对象创建表
# Base1.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

