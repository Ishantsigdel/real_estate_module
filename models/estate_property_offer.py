from odoo import models, fields, api, exceptions
from datetime import timedelta
from odoo.exceptions import UserError, ValidationError


class EstatePropertyOffer(models.Model):
    _name = "estate.property.offer"
    _description = "Estate Property Offer"
    _order = "price desc"

    price = fields.Float(string="Offer Price")

    status = fields.Selection(
        selection=[("accepted", "Accepted"), ("refused", "Refused")],
        string="Status",
        copy=False,
    )

    partner_id = fields.Many2one("res.partner", string="Partner")
    property_id = fields.Many2one("real.estate.property", string="Property")

    validity = fields.Integer(string="Validity (days)", default=7)
    date_deadline = fields.Date(
        string="Deadline",
        compute="_compute_date_deadline",
        inverse="_inverse_date_deadline",
        store=True,
    )
    selling_price = fields.Float(related="property_id.selling_price", readonly=True)
    buyer_id = fields.Many2one(
        "res.partner", related="property_id.buyer_id", readonly=True
    )
    property_type_id = fields.Many2one(
        related="property_id.property_type_id", store=True
    )

    _sql_constraints = [
        (
            "check_offer_price_positive",
            "CHECK(price > 0)",
            "Offer price must be strictly positive.",
        )
    ]

    def action_accept(self):
        for offer in self:
            other_offers = self.search(
                [
                    ("property_id", "=", offer.property_id.id),
                    ("status", "=", "accepted"),
                ]
            )
            if other_offers:
                raise UserError("Only one offer can be accepted per property.")
            offer.status = "accepted"
            offer.property_id.buyer_id = offer.partner_id
            offer.property_id.selling_price = offer.price

    def action_refuse(self):
        for offer in self:
            offer.status = "refused"

    @api.depends("create_date", "validity")
    def _compute_date_deadline(self):
        for offer in self:
            create_date = offer.create_date or fields.Datetime.now()
            offer.date_deadline = create_date.date() + timedelta(days=offer.validity)

    def _inverse_date_deadline(self):
        for offer in self:
            create_date = offer.create_date or fields.Datetime.now()
            offer.validity = (
                (offer.date_deadline - create_date.date()).days
                if offer.date_deadline
                else 0
            )


    @api.model_create_multi
    def create(self, vals):
        offer = (
            self.env["estate.property.offer"]
            .search([("property_id", "=", vals[0]["property_id"])])
            .mapped("price")
        )
        if offer:
            max_offer = max(offer)
            if max_offer and vals[0]["price"] < max_offer:
                raise exceptions.ValidationError(
                    f"Cannot create offer with amount less than {int(max_offer)} :-("
                )
        res = super().create(vals)
        res.property_id.state = "offer_received"
        return res