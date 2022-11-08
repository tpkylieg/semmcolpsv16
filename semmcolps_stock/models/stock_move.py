# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    # Field Declarations
    supplier_number = fields.Char(string="Supplier Number")
    # Base fields only added to change attributes
    lot_id = fields.Many2one(string="GRN")
    lot_name = fields.Char(string="GRN name")

    def _get_value_production_lot(self):
        """
        Inherited so that we can assign the Supplier number from move line to lot.
        """
        res = super()._get_value_production_lot()
        res.update({'supplier_number': self.supplier_number})
        return res
