# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models, api


class StockLot(models.Model):
    _inherit = 'stock.lot'

    # Field Declarations
    supplier_number = fields.Char(string="Supplier Number", copy=False)

    @api.model
    def _get_next_serial(self, company, product):
        """
        Inherited so that we can generate lot as per GRN Sequence for Product having lot as tracking else base logic.
        """
        return product.tracking == "lot" and self.env.ref("semmcolps_stock.sequence_grn_number_lot",
                                                          raise_if_not_found=True).next_by_id() \
               or super()._get_next_serial(company, product)
