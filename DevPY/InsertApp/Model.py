# # coding: utf-8

from InsertApp import app,db

# from sqlalchemy import BigInteger, CHAR, Column, Date, Float, Index, Integer, JSON, String, TIMESTAMP, Text
# from sqlalchemy.dialects.mysql import CHAR, TINYINT, VARCHAR


# class BizUnit(db.model):
#     __tablename__ = 'biz_unit'

#     code = db.Column(String(64), primary_key=True)
#     name = db.Column(String(45), nullable=False)
#     longitude = db.Column(Float(asdecimal=True))
#     latitude = db.Column(Float(asdecimal=True))
#     address = db.Column(String(255))
#     description = db.Column(String(255))
#     avatar = db.Column(CHAR(36))
#     model = db.Column(String(45), nullable=False)
#     pspe = db.Column(Text, comment='视角')
#     design_company = db.Column(String(45))
#     design_company_man = db.Column(String(45))
#     construction_company = db.Column(String(45))
#     construction_company_man = db.Column(String(45))
#     develop_company = db.Column(String(45))
#     develop_company_man = db.Column(String(45))
#     supervise_company = db.Column(String(45))
#     supervise_company_man = db.Column(String(45))
#     survey_company = db.Column(String(45))
#     survey_company_man = db.Column(String(45))
#     begin_date = db.Column(Date)
#     complete_date = db.Column(Date)
#     ms_std = db.Column(String(36), comment='测量标准')
#     def_template = db.Column(JSON)
#     file_name = db.Column(String(45))
#     storage = db.Column(String(100))
#     ts = db.Column(TIMESTAMP)
#     file_id = db.Column(String(45))


# class BuRolePerm(db.model):
#     __tablename__ = 'bu_role_perms'

#     bu_code = db.Column(String(64), primary_key=True, nullable=False)
#     role = db.Column(String(36), primary_key=True, nullable=False)
#     name = db.Column(String(45), nullable=False)
#     perms = db.Column(JSON)p


# class BuUserRel(db.model):
#     __tablename__ = 'bu_user_rel'
#     __table_args__ = (
#         Index('UK_buuser', 'bu_code', 'user', unique=True),
#     )

#     id = db.Column(BigInteger, primary_key=True)
#     bu_code = db.Column(String(64), nullable=False)
#     user = db.Column(String(45), nullable=False)


# class BuUserRole(db.model):
#     __tablename__ = 'bu_user_roles'

#     bu_code = db.Column(String(64), primary_key=True, nullable=False)
#     user = db.Column(String(45), primary_key=True, nullable=False)
#     roles = db.Column(JSON)


# class Building(db.model):
#     __tablename__ = 'building'

#     bid = db.Column(String(64), primary_key=True)
#     bu_code = db.Column(String(64), nullable=False)
#     name = db.Column(String(45), nullable=False)
#     model = db.Column(String(45), nullable=False)
#     pspe = db.Column(Text, comment='视角')


class ClDevice(db.Model):
    __tablename__ = 'cl_device'

    deviceid = db.Column(db.String(50), unique=True,primary_key=True,nullable=False,comment='设备mac地址')
    devname = db.Column(db.String(50), comment='设备名称')
    type = db.Column(db.String(50), comment='设备类型')
    serviceid = db.Column(db.String(150), comment='UUID')
    charid = db.Column(db.String(150), comment='蓝牙特征值')
    startSampling = db.Column(db.String(100), comment='开始命令')
    endSampling = db.Column(db.String(100), comment='结束命令')
    writrCharacteristicId = db.Column(db.String(150),comment='writrCharacteristicId')
    devtasktype = db.Column(db.JSON)

    


# class EqRecord(db.model):
#     __tablename__ = 'eq_record'

#     id = db.Column(BigInteger, primary_key=True)
#     asset_code = db.Column(String(155, 'utf8mb4_bin'))
#     before_proj = db.Column(String(100, 'utf8mb4_bin'))
#     after_proj = db.Column(String(100, 'utf8mb4_bin'))
#     ts = db.Column(Date)
#     user = db.Column(String(45, 'utf8mb4_bin'))
#     proj_code = db.Column(String(100, 'utf8mb4_bin'))
#     eid = db.Column(BigInteger, nullable=False)


# class Equipment(db.model):
#     __tablename__ = 'equipment'

#     id = db.Column(BigInteger, primary_key=True)
#     asset_code = db.Column(String(155, 'utf8mb4_bin'))
#     name = db.Column(String(60, 'utf8mb4_bin'))
#     size = db.Column(String(50, 'utf8mb4_bin'))
#     factory = db.Column(String(60, 'utf8mb4_bin'))
#     factory_code = db.Column(String(60, 'utf8mb4_bin'))
#     buy_ts = db.Column(Date)
#     price = db.Column(String(45, 'utf8mb4_bin'))
#     unit = db.Column(String(45, 'utf8mb4_bin'))
#     unit_ts = db.Column(Date)
#     proj_name = db.Column(String(100, 'utf8mb4_bin'))
#     company = db.Column(String(50, 'utf8mb4_bin'))
#     asset_type = db.Column(String(45, 'utf8mb4_bin'))
#     status = db.Column(String(45, 'utf8mb4_bin'))
#     proj_code = db.Column(String(100, 'utf8mb4_bin'), nullable=False)
#     user = db.Column(String(45, 'utf8mb4_bin'))
#     contents = db.Column(String(100, 'utf8mb4_bin'))


# class Floor(db.model):
#     __tablename__ = 'floor'
#     __table_args__ = (
#         Index('floor_uk', 'fid', 'bid', unique=True),
#     )

#     fid = db.Column(String(80), primary_key=True)
#     bu_code = db.Column(String(64), nullable=False)
#     bid = db.Column(String(64), nullable=False)
#     name = db.Column(String(45), nullable=False)
#     model = db.Column(String(45), nullable=False)
#     height = db.Column(Integer, nullable=False, server_default=text("'0'"), comment='mm')
#     pspe = db.Column(Text)


# class FlowMaster(db.model):
#     __tablename__ = 'flow_master'

#     id = db.Column(String(45), primary_key=True)
#     bu_code = db.Column(String(64), nullable=False)
#     name = db.Column(String(255), nullable=False)
#     type = db.Column(String(45), nullable=False)
#     status = db.Column(String(45), nullable=False, server_default=text("'PROC'"))
#     biz_status = db.Column(String(45), nullable=False)
#     create_ts = db.Column(TIMESTAMP, nullable=False)
#     close_ts = db.Column(TIMESTAMP)
#     dead_line = db.Column(Date)
#     bid = db.Column(String(64))
#     fid = db.Column(String(80))
#     delayed = db.Column(CHAR(1), nullable=False, server_default=text("'N'"))


# class FlowNuser(db.model):
#     __tablename__ = 'flow_nuser'
#     __table_args__ = (
#         Index('nuser_uk', 'flow_id', 'user', unique=True),
#     )

#     id = db.Column(BigInteger, primary_key=True)
#     flow_id = db.Column(String(45), nullable=False)
#     user = db.Column(String(45), nullable=False)


# class IdSeq(db.model):
#     __tablename__ = 'id_seq'

#     table_prefix = db.Column(String(45), primary_key=True, nullable=False)
#     seq_prefix = db.Column(String(45), primary_key=True, nullable=False)
#     date = db.Column(String(45), primary_key=True, nullable=False)
#     seq = db.Column(Integer, nullable=False)


# class ModelDoc(db.model):
#     __tablename__ = 'model_doc'

#     id = db.Column(String(45, 'utf8mb4_bin'), primary_key=True)
#     name = db.Column(String(255, 'utf8mb4_bin'))
#     file_name = db.Column(String(255, 'utf8mb4_bin'))
#     storage = db.Column(String(60, 'utf8mb4_bin'))
#     ts = db.Column(TIMESTAMP)
#     user = db.Column(String(45, 'utf8mb4_bin'))
#     downloads = db.Column(Integer)


# class MsCategory(db.model):
#     __tablename__ = 'ms_category'

#     fid = db.Column(VARCHAR(80), primary_key=True, nullable=False)
#     category = db.Column(VARCHAR(45), primary_key=True, nullable=False)
#     bu_code = db.Column(VARCHAR(64), nullable=False)
#     build_date = db.Column(Date)
#     detail = db.Column(JSON)
#     status = db.Column(VARCHAR(45), nullable=False, server_default=text("'P'"))


# class MsLedger(db.model):
#     __tablename__ = 'ms_ledger'

#     id = db.Column(BigInteger, primary_key=True)
#     mid = db.Column(String(45), nullable=False)
#     biz_type = db.Column(String(45), nullable=False)
#     data = db.Column(JSON)
#     update_ts = db.Column(TIMESTAMP, nullable=False)
#     update_user = db.Column(String(45), nullable=False)


# class MsMaster(db.model):
#     __tablename__ = 'ms_master'

#     id = db.Column(String(45), primary_key=True)
#     name = db.Column(String(80), nullable=False)
#     bu_code = db.Column(String(64), nullable=False)
#     bid = db.Column(String(64), nullable=False)
#     fid = db.Column(String(80), nullable=False)
#     type = db.Column(String(45), nullable=False)
#     status = db.Column(String(45), nullable=False)
#     curr_data = db.Column(JSON)
#     init_ts = db.Column(TIMESTAMP, nullable=False)
#     submit_deadline = db.Column(Date, nullable=False, server_default=text("'1986-01-01'"))
#     update_ts = db.Column(TIMESTAMP)
#     submit_delayed = db.Column(CHAR(1), nullable=False, server_default=text("'N'"))
#     submit_delayed_days = db.Column(Integer, nullable=False, server_default=text("'0'"))
#     rectify_limit_days = db.Column(Integer, nullable=False, server_default=text("'0'"))
#     total_comps = db.Column(Integer, nullable=False)
#     curr_comps = db.Column(Integer, nullable=False, server_default=text("'0'"))
#     comp_dtl = db.Column(JSON)
#     retest = db.Column(CHAR(1), server_default=text("'N'"))
#     rid = db.Column(String(45))
#     latest_ledger_id = db.Column(BigInteger)
#     pass_percent = db.Column(Float, nullable=False, server_default=text("'-1'"))
#     stage = db.Column(String(45))
#     position = db.Column(String(45))
#     fails = db.Column(Integer)
#     rectify_deadline = db.Column(Date)
#     rectify_delayed = db.Column(CHAR(1), nullable=False, server_default=text("'N'"))
#     rectify_delayed_days = db.Column(Integer, nullable=False, server_default=text("'0'"))
#     ms_mastercol = db.Column(String(45))
#     rect_date = db.Column(TIMESTAMP)


# class MsStatBuildingPop(db.model):
#     __tablename__ = 'ms_stat_building_pop'

#     bu_code = db.Column(String(64, 'utf8mb4_bin'), primary_key=True, nullable=False)
#     category = db.Column(String(45, 'utf8mb4_bin'), primary_key=True, nullable=False)
#     bid = db.Column(String(64, 'utf8mb4_bin'), primary_key=True, nullable=False)
#     pop = db.Column(Float(asdecimal=True), nullable=False)


# class MsStatCatePop(db.model):
#     __tablename__ = 'ms_stat_cate_pop'

#     bu_code = db.Column(String(64), primary_key=True, nullable=False)
#     category = db.Column(String(45), primary_key=True, nullable=False)
#     pop = db.Column(Float(asdecimal=True), nullable=False, server_default=text("'0'"))
#     point = db.Column(Integer, nullable=False, server_default=text("'0'"))


# class MsStatDetailPop(db.model):
#     __tablename__ = 'ms_stat_detail_pop'
#     __table_args__ = {'comment': '公司级详细合格率记录'}

#     bu_code = db.Column(String(64), primary_key=True, nullable=False)
#     category = db.Column(String(45), primary_key=True, nullable=False)
#     floor = db.Column(String(80), primary_key=True, nullable=False)
#     type = db.Column(String(45), primary_key=True, nullable=False)
#     pop = db.Column(Float(asdecimal=True), nullable=False, server_default=text("'0'"))
#     point = db.Column(Integer, nullable=False, server_default=text("'0'"))


# class MsStatFloorPop(db.model):
#     __tablename__ = 'ms_stat_floor_pop'

#     bu_code = db.Column(String(64), primary_key=True, nullable=False)
#     category = db.Column(String(45), primary_key=True, nullable=False)
#     floor = db.Column(String(80), primary_key=True, nullable=False)
#     bid = db.Column(String(64), nullable=False)
#     pop = db.Column(Float(asdecimal=True), nullable=False)


# class MsStatMonthDetailPop(db.model):
#     __tablename__ = 'ms_stat_month_detail_pop'

#     bu_code = db.Column(String(64), primary_key=True, nullable=False)
#     category = db.Column(String(45), primary_key=True, nullable=False)
#     floor = db.Column(String(80), primary_key=True, nullable=False)
#     type = db.Column(String(45), primary_key=True, nullable=False)
#     month = db.Column(String(45), primary_key=True, nullable=False)
#     pop = db.Column(Float(asdecimal=True), nullable=False, server_default=text("'0'"))


# class MsStatMonthFail(db.model):
#     __tablename__ = 'ms_stat_month_fail'

#     bu_code = db.Column(String(64), primary_key=True, nullable=False)
#     month = db.Column(String(45), primary_key=True, nullable=False)
#     fail_points = db.Column(Integer, nullable=False, server_default=text("'0'"))


# class MsStatMonthPop(db.model):
#     __tablename__ = 'ms_stat_month_pop'
#     __table_args__ = {'comment': '月份合格记录'}

#     bu_code = db.Column(String(64), primary_key=True, nullable=False)
#     category = db.Column(String(45), primary_key=True, nullable=False)
#     month = db.Column(String(45), primary_key=True, nullable=False)
#     pop = db.Column(Float(asdecimal=True), nullable=False, server_default=text("'0'"))


# class MsStatTypePop(db.model):
#     __tablename__ = 'ms_stat_type_pop'

#     bu_code = db.Column(String(64), primary_key=True, nullable=False)
#     category = db.Column(String(45), primary_key=True, nullable=False)
#     type = db.Column(String(45), primary_key=True, nullable=False)
#     pop = db.Column(Float(asdecimal=True), nullable=False, server_default=text("'0'"))
#     point = db.Column(Integer, nullable=False, server_default=text("'0'"))


# class MsTemplate(db.model):
#     __tablename__ = 'ms_template'

#     id = db.Column(String(36), primary_key=True)
#     name = db.Column(String(45), nullable=False, unique=True)
#     thresholds = db.Column(JSON)
#     rbstr_strategy = db.Column(String(45))
#     rbstr_sample_percent = db.Column(Integer, server_default=text("'100'"))
#     task_defs = db.Column(JSON)


# class SmsCodeRec(db.model):
#     __tablename__ = 'sms_code_rec'

#     phone_num = db.Column(VARCHAR(45), primary_key=True)
#     code = db.Column(VARCHAR(45), nullable=False)
#     ts = db.Column(TIMESTAMP, nullable=False)
#     interval_ts = db.Column(TIMESTAMP, nullable=False)
#     expire_ts = db.Column(TIMESTAMP, nullable=False)


# class SmsTmplMapping(db.model):
#     __tablename__ = 'sms_tmpl_mapping'

#     tmpl_type = db.Column(VARCHAR(45), primary_key=True)
#     tmpl_id = db.Column(VARCHAR(45), nullable=False)
#     comment = db.Column(VARCHAR(128))


# class StdDoc(db.model):
#     __tablename__ = 'std_doc'

#     id = db.Column(String(45), primary_key=True)
#     bu_code = db.Column(String(64))
#     sn = db.Column(String(64), nullable=False, unique=True)
#     name = db.Column(String(255), nullable=False)
#     category = db.Column(String(45), nullable=False)
#     storage = db.Column(String(36), nullable=False)
#     file_name = db.Column(String(255), nullable=False)
#     downloads = db.Column(Integer, nullable=False, server_default=text("'0'"))
#     user = db.Column(String(45), nullable=False)
#     ts = db.Column(TIMESTAMP, nullable=False)


# class Storage(db.model):
#     __tablename__ = 'storages'

#     id = db.Column(CHAR(36), primary_key=True)
#     ofilename = db.Column(String(255), nullable=False)
#     thumbnail = db.Column(CHAR(1), nullable=False, server_default=text("'N'"))
#     ts = db.Column(TIMESTAMP, nullable=False)
#     user = db.Column(String(45))


# class User(db.model):
#     __tablename__ = 'users'

#     username = db.Column(VARCHAR(45), primary_key=True)
#     password = db.Column(VARCHAR(255), nullable=False)
#     dispname = db.Column(VARCHAR(45), nullable=False)
#     enabled = db.Column(TINYINT, nullable=False, server_default=text("'1'"))
#     descr = db.Column(VARCHAR(80))
#     avatar = db.Column(CHAR(36))
#     admin = db.Column(CHAR(1), server_default=text("'N'"))
#     phone = db.Column(VARCHAR(45), unique=True)
#     email = db.Column(VARCHAR(45))
#     inst = db.Column(VARCHAR(150))



    
    
