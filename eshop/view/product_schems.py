from marshmallow import Schema, fields

class ProductCreateSchema(Schema):
    id = fields.String()
    name = fields.String(required=True)
    price = fields.Float(required=True)

class ProductShemas(Schema):
    id = fields.String()
    name = fields.String()
    price = fields.Float()

class ProductGetManyParams(Schema):
    page = fields.Int(required=True)
    limit = fields.Int(required=True)


