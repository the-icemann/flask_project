# from market import app, db
# from market.models import Item


# def seed_data():
#     if not Item.query.first():  # only add if empty
#         items = [
#             Item(name="Laptop", price=1000, description="A high performance laptop", barcode="123456789012"),
#             Item(name="Phone", price=500, description="A smartphone with a great camera", barcode="987654321098"),
#             Item(name="Headphones", price=150, description="Noise-cancelling headphones", barcode="456789123456"),
#         ]
#         db.session.add_all(items)
#         db.session.commit()
#         print("Database seeded!")

# #Checks if the run.py file has executed directly and not imported
# if __name__ == '__main__':
#     app.run(debug=True)


#     with app.app_context():
#         db.create_all()
#         seed_data() # Create database tables for our data models


from market import app, db
from market.models import Item

def seed_data():
    # if not Item.query.first():  # only add if empty
    #     items = [
    #         Item(name="Laptop", price=1000, description="A high performance laptop", barcode="123456789012"),
    #         Item(name="Phone", price=500, description="A smartphone with a great camera", barcode="987654321098"),
    #         Item(name="Headphones", price=150, description="Noise-cancelling headphones", barcode="456789123456"),
    #     ]
    #     db.session.add_all(items)
    #     db.session.commit()
        print("Database seeded!")

if __name__ == '__main__':
    with app.app_context():
        db.create_all()   # make sure tables exist
        seed_data()       # seed items if empty
    app.run(debug=True)    # start server last
