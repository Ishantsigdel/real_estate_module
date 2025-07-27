{
    "name": "Real estate",
    "version": "1.0",
    "summary": "Manage real estate",
    "description": "CRUD for real estate",
    "author": "Ishant Sigdel",
    "category": "Tools",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/real_estate_views.xml",
        "views/estate_property_type_views.xml",
        "views/estate_property_tag_views.xml",
        "views/estate_property_offer_views.xml",
        "views/estate_property_inherited_model_views.xml"
    ],
    "installable": True,
    "application": True,
}
