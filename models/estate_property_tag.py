from odoo import models, fields 

class EstatePropertyTag(models.Model):
    _name="estate.property.tag"
    _description="Estate Property Tag"
    _order = "name asc"

    name = fields.Char(string="Tag Name", required=True)
    color = fields.Integer(string="Color")

    _sql_constraints = [
        ('name_uniq', 'unique (name)', 'Tag name must be unique.')
    ]