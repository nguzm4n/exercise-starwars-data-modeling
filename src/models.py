import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String(120), unique=True, nullable=False)
    firstname = Column(String(120), nullable=False)
    lastname = Column(String(120))
    password = Column(String(120), nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    date = Column(Date, index=True)
    favorites = relationship("Favorite", back_populates="user")

class Character(Base):
    __tablename__ = "character"
    id = Column(Integer, primary_key=True)
    gender = Column(String(120))
    birth_year = Column(String(120))
    eye_color = Column(String(120))
    skin_color = Column(String(120))
    hair_color = Column(String(120))
    mass = Column(Integer)
    height = Column(Integer)
    favorites = relationship("Favorite", back_populates="character")

class Planet(Base):
    __tablename__ = "planet"
    id= Column(Integer, primary_key=True)
    surface = Column(String(120))
    terrain = Column(String(120))
    climate = Column(String(120))
    population = Column(Integer)
    gravity = Column(Integer)
    orbital_period = Column(Integer)
    rotation_period = Column(Integer)
    diameter = Column(Integer)
    favorites = relationship("Favorite", back_populates="planet")

class Favorite(Base):
    __tablename__ = "favorite"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    character_id = Column(Integer, ForeignKey('character.id'))
    user = relationship("User", back_populates="favorites")
    planet = relationship("Planet", back_populates="favorites")
    character = relationship("Character", back_populates="favorites")

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
