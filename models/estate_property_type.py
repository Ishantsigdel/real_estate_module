from odoo import models, fields


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Estate Property Type"

    name = fields.Char(string="Title", required=True)


    _sql_constraints = [
            ('name_uniq', 'unique (name)', 'The code of the account must be unique per company !')
    ]