from odoo import models, fields, api


class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Estate Property Type"
    _order = "sequence, name asc"

    name = fields.Char(string="Title", required=True)
    property_ids = fields.One2many('real.estate.property', 'property_type_id', string="Properties")
    sequence = fields.Integer(string="Sequence", default=10)
    offer_ids = fields.One2many(
        "estate.property.offer", inverse_name="property_type_id", string="Offer ID"
    )

    offer_count = fields.Integer(
        string="Offer Count", compute="_compute_count_property"
    )

    @api.depends('offer_ids')
    def _compute_count_property(self):
        for record in self:
            record.offer_count = len(record.offer_ids)



    _sql_constraints = [
            ('name_uniq', 'unique (name)', 'The code of the account must be unique per company !')
    ]

    def action_stat_button(self):
        self.ensure_one()
        xml_id = self.env.context.get("xml_id")
        if xml_id:

            res = self.env["ir.actions.act_window"]._for_xml_id(xml_id)
            res.update(
                context=dict(
                    self.env.context, default_property_type_id=self.id, group_by=False
                ),
                domain=[("property_type_id", "=", self.id)],
            )
            return res
        return False