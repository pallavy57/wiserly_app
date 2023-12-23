from sqlalchemy import Column, types

from wiserly_app.services.extensions import db


class WiserlyShops(db.Model):

	__tablename__ = 'wiserlyshops'

	id = Column(db.Integer, primary_key=True)
	#<shopname>.myshopify.com
	shop = Column(db.String(255))

	#token is used to issue commands on behalf of a shop
	token = Column(db.String(255))

	#status of user, currently not used anywhere but maybe one day? ;)
	status = Column(db.SmallInteger, default=1)