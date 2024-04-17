from Datamodel import engine,Session
from Datamodel.DatabaseTable import Warehouse,Items,ItemSpec,Inventory
# and_ or_ sql语句的查询条件and or
from sqlalchemy import MetaData,and_,or_,select

# def sql_obj(obj):
#     return {key: getattr(obj, key) for key in obj.__dict__ if not callable(getattr(obj, key)) and not key.startswith('_')}


if __name__=="__main__":


    sqlsession = Session()
 
    # 插值
    # wh_table = warehouse(name='预备仓库1',location='大门外1',username='王五1',comment='预备用，非正式仓库1') 

    sql_query_excute = sqlsession.query(ItemSpec,Items.itmename).join(Items,onclause=ItemSpec.itemid == Items.id).all()
    relist = []

    # 利用 mapper 反查table的colum 进行数据封装
    # for line in sql_query:
    #     test_dict={'itmename':line[1]}
    #     for key in line[0].__mapper__.c.keys():
    #         test_dict[key]=getattr(line[0],key)
    #     result_list.append(test_dict)
    # print(result_list)

    for line in sql_query_excute:
        relist.append({
            'itmename':line[1],
            'spcid':line[0].id,
            'spcname':line[0].spcname,
            'comment':line[0].comment,
            'low':line[0].low,
            'enabled':line[0].enabled
            }
        )
    result_json = {"data":relist}
    print(result_json)
            

 
    # print(result)

    # 多对一ORM查询

    # result = sqlexcute.query(Inventory).all()

    # for line in result:
    #     print(f'存储仓库：{line.warehouse.name},货物名称：{line.specs.spcname}，货物单位：{line.quantity}')

    # 一对多ORM
    # result = sqlexcute.query(Warehouse).all()

    # for line in result:
    #     if line.quantitys:
    #         for lines in line.quantitys:
    #             print(f'{line.name},{line.location},{lines.quantity},{lines.itemspec.spcname}')
    #     else:
    #         print(f'{line.name},{line.location},[None]')

    sqlsession.close()

    # 创建数据库表
    # metaobject = MetaData()

    # Base1.metadata.create_all(engine)

    # 非类进行插入记录
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

        