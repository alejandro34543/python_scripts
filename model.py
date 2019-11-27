"""Création des deux class compte et bucket"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, CHAR, ForeignKey

Base = declarative_base()

class Compte(Base):
    __tablename__ = 'compte'
    id = Column(Integer, primary_key=True)
    nom = Column(CHAR(75))
    description = Column(CHAR(150))

    def __repr__(self):
        return "<compte(nom='{}', description='{}')>"\
                .format(self.nom, self.description)


class Bucket(Base):
    __tablename__ = 'bucket'
    id = Column(Integer, primary_key=True)
    nom = Column(CHAR(75))
    taille = Column(CHAR(15))
    type = Column(CHAR(50))
    compteid = Column(Integer, ForeignKey('compte.id'))

    def __repr__(self):
        return "<bucket(nom='{}', taille='{}', type='{}', compteid='{}')>"\
            .format(self.nom, self.description, self.compteid)