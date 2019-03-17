from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from models import db, User

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydb.db'
app.config['SECRET_KEY'] = 'not that secret'
db.init_app(app)
admin = Admin(app, name='DashBoard', template_mode='bootstrap3')


class UserView(ModelView):
    column_searchable_list = (User.name, User.cpf)
    edit_template = 'edit_user.html'
    create_template = 'create_user.html'


admin.add_view(UserView(User, db.session))

if __name__ == '__main__':
    app.run(debug=True)
