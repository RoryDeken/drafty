from . import db


class Player(db.Model):
    __tablename__ = 'players'
    id = db.Column(db.String(5), primary_key=True)
    rank = db.Column(db.Integer())
    espnId = db.Column(db.String(30))
    firstName = db.Column(db.String(200))
    lastName = db.Column(db.String(200))
    team = db.Column(db.String(5))
    position = db.Column(db.String(3))
    drafted = db.relationship('Drafted')

    def __repr__(self):
        return "Player(id='%s', rank='%s', espnId='%s', firstName='%s', lastName='%s', team='%s', position='%s')>" % (self.id, self.rank, self.espnId, self.firstName, self.lastName, self.team, self.position)


class Drafted(db.Model):
    __tablename__ = 'drafted'
    id = db.Column(db.Integer(), primary_key=True)
    player_id = db.Column(db.String(5), db.ForeignKey(
        'players.id'), nullable=False)
    draft_id = db.Column(db.Integer(), db.ForeignKey(
        'drafts.id'), nullable=False)
    firstName = db.Column(db.String(200))
    lastName = db.Column(db.String(200))
    team = db.Column(db.String(5))
    position = db.Column(db.String(3))
    round = db.Column(db.Integer())
    ownedBy = db.Column(db.String(200))

    def __repr__(self):
        return "Drafted(id='%s', firstName='%s', lastName='%s', team='%s', position='%s', round='%s', ownedBy='%s')>" % (self.id, self.firstName, self.lastName, self.team, self.position, self.round, self.ownedBy)


class Draft(db.Model):
    __tablename__ = 'drafts'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(200))
    rounds = db.Column(db.Integer())
    drafted = db.relationship('Drafted')

    def __repr__(self):
        return "Draft(id='%s', name='%s', self.rounds)>" % (self.id, self.name, self.rounds)


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    firstName = db.Column(db.String(200))
    lastName = db.Column(db.String(200))
    teamName = db.Column(db.String(200))

    def __repr__(self):
        return "User(id='%s', firstName='%s', lastName='%s', teamName='%s')>" % (self.id, self.firstName, self.lastName, self.teamName)
