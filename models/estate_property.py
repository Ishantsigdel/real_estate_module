from odoo import models, fields


class RealEstateProperty(models.Model):
    _name = "real.estate.property"
    _description = "Real Estate Property"

    name = fields.Char(string="Title", required=True, default="unknown")
    description = fields.Text(string="Description")
    postcode = fields.Char(string="Postcode")
    date_availability = fields.Date(string="Available From")
    expected_price = fields.Float(string="Expected Price", required=True)
    selling_price = fields.Float(string="Selling Price")
    bedrooms = fields.Integer(string="Bedrooms", default=2)
    living_area = fields.Integer(string="Living Area (sq ft)")
    garage = fields.Boolean(string="Garage")
    facades = fields.Integer(string="Number of Facades", default=1)
    garden = fields.Boolean(string="Garden")
    garden_area = fields.Integer(string="Garden Area (sq ft)")
    garden_orientation = fields.Selection(
        [("north", "North"), ("south", "South"), ("east", "East"), ("west", "West")],
        string="Garden Orientation",
    )
    last_seen = fields.Datetime(string="Last Seen", default=fields.Datetime.now)
    active = fields.Boolean(string="Active", default=True)
    state = fields.Selection(
        [
            ("new", "New"),
            ("offer_received", "Offer Received"),
            ("offer_accepted", "Offer Accepted"),
            ("sold", "Sold"),
            ("canceled", "Canceled"),
        ],
        string="Status",
        required=True,
        copy=False,
        default="new",
    )
