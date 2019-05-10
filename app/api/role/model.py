from sqlalchemy import Model, Integer, String, Column, ForeignKey, relationship

class Role(Model):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    name = Column(String(64), unique=True)
    users = relationship('User', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role %r>' % self.name

