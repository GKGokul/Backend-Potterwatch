from sqlalchemy import Column, Integer
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Questions(Base):
    __tablename__ = 'questions'

    index = Column(Integer, primary_key=True)
    One = Column(Integer)
    Two = Column(Integer)
    Three = Column(Integer)
    Four = Column(Integer)
    Five = Column(Integer)
    Six = Column(Integer)
    Seven = Column(Integer)
    Eight = Column(Integer)
    Nine = Column(Integer)
    Ten = Column(Integer)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'index': self.index,
            'number': self.number,
        }


engine = create_engine('sqlite:///permutations.db')

Base.metadata.create_all(engine)
