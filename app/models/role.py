# -*- coding: utf-8 -*-

from flask_security import RoleMixin
from app import db
from .permission import Permission


class Role(db.Model, RoleMixin):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    permissions = db.Column(db.Integer, default=Permission.GUEST)
    default = db.Column(db.Boolean, default=False, index=True)
    description = db.Column(db.String(255))
    users = db.relationship('User', backref='role', lazy='dynamic')

    @staticmethod
    def insert_roles(self):
        roles = {
            'Guest': (Permission.GUEST, True),
            'User': (Permission.EDIT | Permission.GUEST, False),
            'Administrator': (Permission.ADMINISTRATOR, False)
        }

        for r in roles:
            role = Role.query.filter_by(name=r).first()
            if role is None:
                role = Role(name=r)
            role.permissions = roles[r][0]
            role.default = roles[r][1]
            db.session.add(role)
        db.session.commit()

    def __repr__(self):
        return '<Role %r>' % self.name


