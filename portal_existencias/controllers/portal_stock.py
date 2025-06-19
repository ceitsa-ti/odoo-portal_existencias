from odoo import http
from odoo.http import request

class PortalStockController(http.Controller):

    @http.route(
        '/portal/existencias',
        type='http',
        auth='user',
        website=True,
        groups='base.group_portal',
    )
    def portal_stock(self, **kw):
        products = request.env['product.product'].search([
            ('sale_ok', '=', True),
            ('type', '!=', 'service'),
        ])
        return request.render('portal_existencias.portal_stock_template', {
            'productos': products,
        })

