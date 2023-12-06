from marshmallow import Schema, fields


class CreateShemas(Schema):
    id = fields.String()
    name = fields.String(required=True)
    price = fields.Float(required=True)


class ProductShemas(Schema):
    id = fields.String()
    name = fields.String(required=True)
    price = fields.Float(required=True)


class ProductGetMany(Schema):
    page = fields.Integer(required=True)
    limit = fields.Integer(required=True)


