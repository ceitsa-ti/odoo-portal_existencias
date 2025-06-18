from odoo import http
from odoo.http import request

class PortalStockController(http.Controller):

    @http.route('/portal/existencias', type='http', auth='user', website=True)
    def portal_stock(self, **kw):
        productos = request.env['product.product'].sudo().search([('categ_id', 'child_of', 564)])
        return request.render('portal_existencias.portal_stock_template', {
            'productos': productos
        })
