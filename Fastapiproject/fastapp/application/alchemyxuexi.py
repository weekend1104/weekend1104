from Datamodel import engine,Session
from Datamodel.DatabaseTable import warehouse,Items,ItemSpec,Inventory
# and_ or_ sql语句的查询条件and or
from sqlalchemy import MetaData,and_,or_,select


if __name__=="__main__":


    sqlexcute = Session()

    # 插值
    # wh_table = warehouse(name='预备仓库1',location='大门外1',username='王五1',comment='预备用，非正式仓库1') 

    result = sqlexcute.query(ItemSpec).filter(ItemSpec.id==5).first()
    
    print(result.spcname)
    print(type(result.comment))

    sqlexcute.close()

    # 创建数据库表
    # metaobject = MetaData()

    # Base1.metadata.create_all(engine)

    # 插入记录
    # with engine.connect() as conn:
    #     conn.execute(fuckyou_table.insert(),[
    #         {"name":"zhangsan","date":"2024-01-01 00:00:00"},
    #         {"name":"lisi","date":"2024-01-01 00:00:00"},
    #         {"name":"wangwu","date":"2024-01-01 00:00:00"}
    #     ])
    #     conn.commit()
    
    #查询记录,多条件
    # with engine.connect() as conn:
        # quert = fuckyou_table.select().where(fuckyou_table.c.name == 'tom')

        # quert = select(fuckyou_table).where(fuckyou_table.c.name == "tom")

        # quert = fuckyou_table.select().where(
        #     or_(
        #         fuckyou_table.c.name == 'tom',
        #         and_(
        #             fuckyou_table.c.date > '2024-01-01',
        #             fuckyou_table.c.date < '2024-04-01'
        #         )
        #     )
        # )

        # result = conn.execute(quert).fetchall()

        