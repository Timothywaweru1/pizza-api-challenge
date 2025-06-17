from server.app import db
from server.models.restaurant import Restaurant
from server.models.pizza import Pizza
from server.models.restaurant_pizza import RestaurantPizza

def seed_data_present():
    db.drop_all()
    db.create_all()

    r1 = Restaurant(name="Timo's Pizza", address="Koinage Street")
    r2 = Restaurant(name="ABC Place", address="Waiyaki Way")
    db.session.add_all([r1, r2])

    p1 = Pizza(name="Ugali", ingredients="Unga, Sukuma, Beef Stew")
    p2 = Pizza(name="Pilau", ingredients="Rice, Tomato Sauce, Chicken, Pepperoni")
    db.session.add_all([p1, p2])

    db.session.commit()

    rp1 = RestaurantPizza(price=100, restaurant_id=r1.id, pizza_id=p1.id)
    rp2 = RestaurantPizza(price=125, restaurant_id=r1.id, pizza_id=p2.id)
    rp3 = RestaurantPizza(price=190, restaurant_id=r2.id, pizza_id=p1.id)
    db.session.add_all([rp1, rp2, rp3])

    db.session.commit()
    print("Database successfully added!")

if __name__ == '__main__':
    seed_data_present()