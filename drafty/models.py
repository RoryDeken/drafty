from . import db


class Player(db.Model):
    __tablename__ = 'players'
    id = db.Column(db.String(5), primary_key=True)
    rank = db.Column(db.String(30))
    espnId = db.Column(db.String(30))
    firstName = db.Column(db.String(200))
    lastName = db.Column(db.String(200))
    team = db.Column(db.String(5))
    position = db.Column(db.String(3))
    available = db.Column(db.Boolean)

    def __repr__(self):
        return "Player(id='%s', rank='%s', espnId='%s', firstName='%s', lastName='%s', team='%s', position='%s', available='%s')>" % (self.id, self.rank, self.espnId, self.firstName, self.lastName, self.team, self.position, self.available)


class Drafted(db.Model):
    __tablename__ = 'drafted'
    id = db.Column(db.String(5), primary_key=True)
    firstName = db.Column(db.String(200))
    lastName = db.Column(db.String(200))
    team = db.Column(db.String(5))
    position = db.Column(db.String(3))
    round = db.Column(db.Integer())
    ownedBy = db.Column(db.String(200))

    def __repr__(self):
        return "Player(id='%s', firstName='%s', lastName='%s', team='%s', position='%s', round='%s', ownedBy='%s')>" % (self.id, self.firstName, self.lastName, self.team, self.position, self.round, self.ownedBy)
