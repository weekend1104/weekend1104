from InsertApp import app,db 

class usertable(db.Model):

    __tablename__ = "ms_device"

    deviceid = db.Column(db.String(30),primary_key=True,unique=True)
    name = db.Column(db.String(30))
    type = db.Column(db.String(50))
    serviceid = db.Column(db.String(100))
    charid = db.Column(db.String(100))


    
    
