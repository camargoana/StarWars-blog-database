import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er


Base = declarative_base()

class User(Base):
    __tablename__='user'
    id_user=Column(Integer, primary_key=True)
    name =Column(String(120), nullable=False)
    email =Column(String(120), nullable=False)
    password=Column(String(80),nullable=False)
    favorites1 = relationship("Favorite",back_populates="user1")
    def add_favorite():
        pass
    def delete_favorite():
        pass
    def see_more():
        pass
    def login():
        pass
    def log_out():
        pass
class item(Base):
    __abstract__ = True
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(256), nullable=False)

class Favorite(Base):
    __tablename__='favorite'
    favorite_id=Column(Integer, primary_key=True)
    user_id=Column(Integer,ForeignKey('user.user_id'))
    planet_id=Column(Integer,ForeignKey('planet.planet_id'))
    character_id=Column(Integer,ForeignKey('character.character_id'))
    vehicle_id=Column(Integer,ForeignKey('vehicle.vehicle_id'))
    user1= relationship("User", back_populates="favorites1")
    parent1=relationship("Character",back_populates="children1")
    parent2=relationship("Character",back_populates="children2")
    parent3=relationship("Character",back_populates="children3")

class Planet(item):
    __tablename__= 'planet'
    population = Column(Integer, nullable=False)
    terrain = Column(String(80),nullable=False)
    climate = Column(String(80), nullable=False)
    rotation_period = Column(String(100), nullable=False)
    orbital_period = Column(String(100), nullable=False)
    diameter = Column(String(80), nullable=False)
    gravity = Column(String(80), nullable=False)
    surface_water = Column(String(80), nullable=False)
    children2=relationship("Favorite",back_populates="parent2")   

class Character(item):
    __tablename__ = 'character'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    height =Column(String(80), nullable=False)
    mass = Column(String(80), nullable=False)
    eye_color = Column(String(40), nullable=False)
    skin_color= Column(String(40), nullable=False)
    birth_year= Column(String(10), nullable=False)
    gender= Column(String(20), nullable=False)
    children1=relationship("Favorite",back_populates="parent1")

class Vehicle(item):
    __tablename__='vehicle'
    vehicle_class = Column(String(80), nullable=False)
    model = Column(String(80), nullable=False)
    manufaturer =Column(String(80), nullable=False)
    cost_in_credits = Column(String(80), nullable=False)
    passengers= Column(String(80), nullable=False)
    cargo_capacity= Column(String(10), nullable=False)
    length = Column(String(80), nullable=False)
    consumables= Column(String(100), nullable=False)
    passengers = Column(String(80),nullable=False)
    children3=relationship("Favorite",back_populates="parent3")

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')