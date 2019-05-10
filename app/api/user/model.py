from sqlalchemy import Model, Integer, String, Column, ForeignKey

class User(Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(64), unique=True, index=True)
    role_id = Column(Integer, ForeignKey('roles.id'))

    def __repr__(self):
        return '<User %r>' % self.username