from flask import Blueprint, jsonify
from server.app import db
from server.models.restaurant import Restaurant

restaurant = Blueprint('restaurant', __name__)


@restaurant.route('/restaurants/<int:id>', methods=['DELETE'])


def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({'error': 'Restaurant not found'}), 404
    db.session.delete(restaurant)
    db.session.commit()
    return ''



@restaurant.route('/restaurants', methods=['GET'])
def get_restaurants_pizza():
    restaurants = Restaurant.query.all()
    return jsonify([restaurant.to_dict() for restaurant in restaurants])

    

@restaurant.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant_pizza(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({'error': 'Restaurant not found'})
    return jsonify(restaurant.to_dict())
