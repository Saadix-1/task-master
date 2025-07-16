from app import app, db

with app.app_context():
    db.create_all()

print("La base de données et les tables ont été créées avec succès !")
