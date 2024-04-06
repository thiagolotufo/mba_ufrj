from db import db


class Address(db.Model):
    __tablename__ = 'restaurant_address'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    postal_code = db.Column(db.String(100), unique=False, nullable=True)
    street_address = db.Column(db.String(100), unique=False, nullable=True)
    address_locality = db.Column(db.String(100), unique=False, nullable=True)
    address_region = db.Column(db.String(100), unique=False, nullable=True)
    address_country = db.Column(db.String(100), unique=False, nullable=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey(
        'restaurant.id'), nullable=False)

    def to_dict(self):
        return {
            'postalCode': self.postal_code,
            'streetAddress': self.street_address,
            'addressLocality': self.address_locality,
            'addressRegion': self.address_region,
            'addressCountry': self.address_country
        }

    @classmethod
    def find_by_postal_code(self, postal_code):
        return db.session().query(Address).filter_by(postal_code=postal_code)

    @classmethod
    def find_by_street_address(self, street_address):
        return db.session().query(Address).filter_by(street_address=street_address)

    @classmethod
    def find_by_address_locality(self, address_locality):
        return db.session().query(Address).filter_by(address_locality=address_locality)

    @classmethod
    def find_by_address_region(self, address_region):
        return db.session().query(Address).filter_by(address_region=address_region)

    @classmethod
    def find_by_address_country(self, address_country):
        return db.session().query(Address).filter_by(address_country=address_country)
