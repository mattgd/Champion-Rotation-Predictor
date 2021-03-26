from sqlalchemy import Column, Date, Integer, String
from sqlalchemy.orm import relationship

from app import db
from .champion_rotation import champion_rotation

CHAMPION_SQUARE_IMAGE_URL_PREFIX = 'https://ddragon.leagueoflegends.com/cdn/5.15.1/img/champion/'
CHAMPION_TALL_IMAGE_URL_PREFIX = 'https://ddragon.leagueoflegends.com/cdn/img/champion/loading/'


class Champion(db.Model):
    __tablename__ = 'champions'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    key = Column(String(50), unique=True)
    title = Column(String(50))
    tags = Column(String(255))
    date_released = Column(Date)
    rotations = relationship('Rotation', secondary=champion_rotation, back_populates='champions')

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'key': self.key,
            'title': self.title,
            'tags': self.tags,
            'dateRelease': self.date_released.isoformat(),
            'squareImage': '{prefix}{key}.png'.format(prefix=CHAMPION_SQUARE_IMAGE_URL_PREFIX, key=self.key),
            'tallImage': '{prefix}{key}_0.jpg'.format(prefix=CHAMPION_TALL_IMAGE_URL_PREFIX, key=self.key)
        }

    def __repr__(self) -> str:
        return '<Champion %r>' % (self.name)
