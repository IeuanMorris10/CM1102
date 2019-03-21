from shop import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(25), unique=True, nullable=False)
    username = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(50),nullable=False)
    description_1 = db.Column(db.String(120), nullable=False)
    description_2 = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Numeric(10,2), nullable=False)
    image_file = db.Column(db.String(30), nullable=False, default='default.jpg')
    size = db.Column(db.String(50), nullable=False, default='default.jpg')

    def __repr__(self):
        return f"Item('{self.item_name}', '{self.description_1}', '{self.description_2}', '{self.price}', '{self.size}')"

class W_item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(50),nullable=False)
    description_1 = db.Column(db.String(120), nullable=False)
    description_2 = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Numeric(10,2), nullable=False)
    image_file = db.Column(db.String(30), nullable=False, default='default.jpg')
    size = db.Column(db.String(50), nullable=False, default='default.jpg')

    def __repr__(self):
        return f"Item('{self.item_name}', '{self.description_1}', '{self.description_2}', '{self.price}', '{self.size}')"

class payment(db.Model):
	id = db.Column(db.Integer(), primary_key = True)
	total_price = db.Column(db.Integer())
	user_cart = db.Column(db.String(25), db.ForeignKey('user.username'))
	address = db.Column(db.String(100), nullable = False)
	card_no = db.Column(db.String(16), nullable = False)
	card_exp_date = db.Column(db.String(5), nullable = False)
	name_on_card = db.Column(db.String(20), nullable = False)

	def __repr__(self):
		return f"payment('{self.total_price}', '{self.name_on_card}')"

@login_manager.user_loader
def load_user(userID):
	return User.query.get(int(userID))
