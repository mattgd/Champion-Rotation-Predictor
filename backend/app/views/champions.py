from flask import Blueprint, jsonify

from ..models.champion import Champion

champions_api = Blueprint('champions', __name__, url_prefix='/api/champions')


@champions_api.route('/', methods=['GET'])
def get_champions():
    """
    API call that returns all champions.

    Returns: 
        JSON representation of all champions
    """
    champions = [champion.to_dict() for champion in Champion.query.all()]
    return jsonify(champions)


@champions_api.route('/<int:id>/', methods=['GET'])
def get_champion(id: int):
    """
    API call that returns a single champion by its supplied ID

    Parameters:
        id      (int): champion ID

    Returns: 
        JSON representation of champion with corresponding ID
    """
    champion = Champion.query.filter_by(id=id).first()
    if not champion: 
        # If empty query, return 404 error
        return 'Could not find champion with supplied ID', 404
        
    return champion.to_dict()

@champions_api.route('/<string:name>/', methods=['GET'])
def get_champion_by_name(name: str):
    """
    API call that returns a single champion by its name.

    Parameters:
        id      (int): champion ID

    Returns: 
        JSON representation of champion with corresponding name
    """
    champion = Champion.query.filter_by(name=name).first()
    if not champion: 
        # If empty query, return 404 error
        return 'Could not find champion with supplied name', 404
        
    return champion.to_dict()
