from sqlalchemy import Column, Date, Integer
from sqlalchemy.orm import relationship

from app import db
from .champion_rotation import champion_rotation


class Rotation(db.Model):
    __tablename__ = 'rotations'
    week_number = Column(Integer, primary_key=True)
    start_date = Column(Date)
    end_date = Column(Date)
    champions = relationship('Champion', secondary=champion_rotation, back_populates='rotations')

    def to_dict(self) -> dict:
        return {
            'weekNumber': self.week_number,
            'startDate': self.start_date.isoformat(),
            'endDate': self.end_date.isoformat()
        }

    def __repr__(self) -> str:
        return '<Rotation %d>' % (self.week_number)
