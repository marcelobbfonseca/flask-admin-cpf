from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import event
from pycpfcnpj import cpfcnpj
from sqlalchemy.orm.session import object_session

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    rg = db.Column(db.String(20), unique=True, nullable=False)
    orgao_exp = db.Column(db.String(30), nullable=False)
    cpf = db.Column(db.String(14), unique=True, nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    phone = db.Column(db.String(30))

    def __repr__(self):
        return '<User %r>' % self.name


def validate_cpf(target, value, oldvalue, initiator):
    # cpf = value
    assert cpfcnpj.validate(value), 'CPF Invalido!'
    return value


event.listen(User.cpf, 'set', validate_cpf, retval=True)
