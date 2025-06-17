from flask import Blueprint, jsonify, request
from server.models.restaurant_pizza import RestaurantPizza
from server.extensions import db

restaurant_pizza_bp = Blueprint('restaurant_pizza', __name__)

@restaurant_pizza_bp.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    
    price = data.get('price')
    if not (1 <= price <= 30):
        return jsonify({'errors': ['Price must be  strictly between 1 and 30']}), 400
    
    try:
        restaurant_pizza = RestaurantPizza(
            price=price,
            pizza_id=data['pizza_id'],
            restaurant_id=data['restaurant_id']
        )
        
        db.session.add(restaurant_pizza)
        db.session.commit()
        
        return jsonify(restaurant_pizza.to_dict())
    
    except Exception as e:
        db.session.rollback()
        return jsonify({'errors': [str(e)]})