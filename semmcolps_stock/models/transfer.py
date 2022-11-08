# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    # Inherited Methods
    def button_validate(self):
        """
        Creation of the Lot Name (GRN Name) by the sequence field.
        """
        for picking in self:
            picking._auto_lot_name_logic()
        return super().button_validate()

    # Custom Methods
    def _auto_lot_name_logic(self):
        """
        This is the logic of creating new name for GRN.
        """
        sequence = self.env.ref('semmcolps_stock.sequence_grn_number_lot', raise_if_not_found=True)
        for filtered_move_line in self.move_line_ids.filtered(
                lambda ml: ml.product_id and ml.product_id.tracking == 'lot'):
            filtered_move_line.lot_name = sequence.next_by_id()
