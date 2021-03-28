import re

from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.orm import relationship

from app import db
from .champion_rotation import champion_rotation

CHAMPION_IMAGE_URL_PREFIX = 'https://ddragon.leagueoflegends.com/cdn/img/champion/splash/'


def generate_key(context) -> str:
    """
    Removes all non alphanumeric characters to create the champion key used to get the champion images.
    """
    name = context.get_current_parameters()['name']
    return re.sub(r'\W+', '', name)


class Champion(db.Model):
    __tablename__ = 'champions'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    key = Column(String(50), unique=True, default=generate_key)
    subclass = Column(String(30))
    blue_essence = Column(Integer)
    riot_points = Column(Integer)
    date_released = Column(Date)
    rotations = relationship('Rotation', secondary=champion_rotation, back_populates='champions')

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'key': self.key,
            'subclass': self.subclass,
            'blueEssence': self.blue_essence,
            'riotPoints': self.riot_points,
            'dateRelease': self.date_released.isoformat(),
            'image': '{prefix}{key}_0.jpg'.format(prefix=CHAMPION_IMAGE_URL_PREFIX, key=self.key)
        }

    def __repr__(self) -> str:
        return '<Champion %r>' % (self.name)
