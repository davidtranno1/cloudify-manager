#########
# Copyright (c) 2013 GigaSpaces Technologies Ltd. All rights reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
#  * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  * See the License for the specific language governing permissions and
#  * limitations under the License.

from flask_security import UserMixin, RoleMixin, SQLAlchemyUserDatastore

from manager_rest.storage.models import db, SerializableBase, UTCDateTime


roles_users_table = db.Table(
    'roles_users',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('roles.id'))
)


tenants_users_table = db.Table(
    'tenants_users',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('tenant_id', db.Integer, db.ForeignKey('tenants.id'))
)


class User(SerializableBase, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), index=True, unique=True)
    email = db.Column(db.String(255), index=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    last_login_at = db.Column(UTCDateTime)
    created_at = db.Column(UTCDateTime)

    roles = db.relationship(
        'Role',
        secondary=roles_users_table,
        backref=db.backref('users', lazy='dynamic')
    )

    tenants = db.relationship(
        'Tenant',
        secondary=tenants_users_table,
        backref=db.backref('users', lazy='dynamic')
    )


class Role(SerializableBase, RoleMixin):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, unique=True, nullable=False, index=True)
    allowed = db.Column(db.PickleType, nullable=False)
    denied = db.Column(db.PickleType)
    description = db.Column(db.Text)


user_datastore = SQLAlchemyUserDatastore(db, User, Role)
