from flask import Blueprint, jsonify

from ..models.rotation import Rotation

rotations_api = Blueprint('rotations', __name__, url_prefix='/api/rotations')


@rotations_api.route('/<int:week>', methods=['GET'])
def get_rotation_week(week: int):
    """
    Returns a JSON representation of all free champions for the given rotation week.
    """
    rotations = Rotation.query.filter(Rotation.week_number == week)
    champions = [rotation.champions.to_dict() for rotation in rotations]
    return jsonify(champions)
