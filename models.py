from sqlalchemy import create_engine, insert, Column, Integer, String, Boolean, Sequence
from sqlalchemy.sql import text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine("mysql+pymysql://test@localhost/drafty", echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)


class Player(Base):
    __tablename__ = 'players'
    id = Column(String(5), primary_key=True)
    firstName = Column(String(200))
    lastName = Column(String(200))
    team = Column(String(5))
    position = Column(String(3))
    available = Column(Boolean)

    def __repr__(self):
        return "Player(id='%s', firstName='%s', lastName='%s', team='%s', position='%s', available='%s')>" % (self.id, self.firstName, self.lastName, self.team, self.position, self.available)


class Drafted(Base):
    __tablename__ = 'drafted'
    id = Column(String(5), primary_key=True)
    firstName = Column(String(200))
    lastName = Column(String(200))
    team = Column(String(5))
    position = Column(String(3))
    round = Column(Integer())
    ownedBy = Column(String(200))

    def __repr__(self):
        return "Player(id='%s', firstName='%s', lastName='%s', team='%s', position='%s', round='%s', ownedBy='%s')>" % (self.id, self.firstName, self.lastName, self.team, self.position, self.round, self.ownedBy)


Base.metadata.create_all(engine)
session = Session()
