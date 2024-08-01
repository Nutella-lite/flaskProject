from app import app, db
from app.models import User

# with app.app_context():
#     db.create_all()
#     db.session.commit()

if __name__ == '__main__':
    app.run()
