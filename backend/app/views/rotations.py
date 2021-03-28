from flask import Blueprint, jsonify

from ..models.champion import Champion
from ..models.rotation import Rotation

rotations_api = Blueprint('rotations', __name__, url_prefix='/api/rotations')


@rotations_api.route('/', methods=['GET'])
def get_rotations():
    """
    Returns a JSON representation of all free champions for the given rotation week.
    """
    rotations = Rotation.query.all()
    return jsonify(rotations)


@rotations_api.route('/<int:week>', methods=['GET'])
def get_rotation_week(week: int):
    """
    Returns a JSON representation of all free champions for the given rotation week.
    """
    rotations = Rotation.query.filter(Rotation.week_number == week)
    champions = [rotation.champions.to_dict() for rotation in rotations]
    return jsonify(champions)


@rotations_api.route('/<string:champion_name>', methods=['GET'])
def get_rotation_by_champion(champion_name: str):
    """
    Returns a JSON representation of all free rotations for a given champion.
    """
    rotations = Rotation.query.join(Rotation.champions).filter(Champion.name == champion_name).all()
    rotations = [rotation.to_dict() for rotation in rotations]
    return jsonify(rotations)
