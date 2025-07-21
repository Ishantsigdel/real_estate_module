from odoo import models, fields


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Estate Property Type"
    _order = "sequence, name asc"

    name = fields.Char(string="Title", required=True)
    property_ids = fields.One2many('real.estate.property', 'property_type_id', string="Properties")
    sequence = fields.Integer(string="Sequence", default=10)



    _sql_constraints = [
            ('name_uniq', 'unique (name)', 'The code of the account must be unique per company !')
    ]