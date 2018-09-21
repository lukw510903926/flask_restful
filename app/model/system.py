from app import db
from app.model.entity import BaseModel


class User(db.Model, BaseModel):
    __tablename__ = 'sys_user'
    # 表的结构:
    id = db.Column(db.String(20), primary_key=True)


class Role(db.Model, BaseModel):
    __tablename__ = 'sys_role'
    # 表的结构:
    id = db.Column(db.String(20), primary_key=True)


class Resource(db.Model, BaseModel):
    __tablename__ = 'sys_resource'
    # 表的结构:
    id = db.Column(db.String(20), primary_key=True)


class Permission(db.Model, BaseModel):
    __tablename__ = 'sys_permission'
    # 表的结构:
    id = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(20))

    # object 展示
    def __repr__(self):
        return "Permission : %r" % self.name
