from sqlalchemy import create_engine, Column, Integer, UniqueConstraint, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.schema import MetaData, Table

# Base = declarative_base()
#
#
# class UsersTable(Base):
#
#     __tablename__ = "users"
#
#     id = Column(Integer, primary_key=True)
#     login = Column(String)
#
#     check_1 = UniqueConstraint("login")
#
#     def __init__(self, login):
#         self.login = login
#
#     def __repr__(self):
#
#         return "UsersTable<uid = {}, login = {}>".format(self.id, self.login)
#
#
# class MessagesTable(Base):
#
#     __tablename__ = "messages"
#
#     mid = Column(Integer(), primary_key=True)
#     message = Column(String)
#     user_from = Column(Integer(), ForeignKey("users.id"))
#     user_to = Column(Integer(), ForeignKey("users.id"))
#
#     p_user_from = relationship("UsersTable", foreign_keys=[user_from])
#     p_user_to = relationship("UsersTable", foreign_keys=[user_to])
#
#     def __repr__(self):
#
#         return "MessagesTable<mid = {}, user_from = {}, user_to = {}, message = {}>".format(self.mid, self.user_from, self.user_to, self.message)
#
#
# engine = create_engine('sqlite:///memory.sqlite3', echo=True)
# pool_recycle = 7200
#
# session = sessionmaker(bind=engine)()
#
# MetaData.create_all(engine)

engine = create_engine('sqlite:///memory.sqlite3', echo=True)

metadata = MetaData()

user = Table('user', metadata,
    Column('user_id', Integer, primary_key=True),
    Column('user_name', String(16), nullable=False)
    )
message = Table('message', metadata,
                Column('message_id', Integer, primary_key=True),
                Column('message', String(64)),
                Column('user_from', Integer, ForeignKey('user.user_id')),
                Column('user_to', Integer, ForeignKey('user.user_id')),
                )

session = sessionmaker(bind=engine)()
metadata.create_all(engine)
