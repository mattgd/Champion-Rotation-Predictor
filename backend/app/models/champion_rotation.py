from sqlalchemy import Column, ForeignKey, Integer, Table

from app import db


champion_rotation = Table('champion_rotations', db.Model.metadata,
    Column('rotation_id', Integer, ForeignKey('rotations.week_number')),
    Column('champion_id', Integer, ForeignKey('champions.id'))
)
