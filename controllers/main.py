from odoo import fields, http
from odoo.http import request

class MyWebTest(http.Controller):
    @http.route('/myterms', type='http', auth='public', website=True)
    def terms_conditions(self, **kwargs):
        #return "Helo World"

        # // render a template example
        # return http.request.render('web_hr_recruit.my-subjects', {
        #     'subjects':
        #         ['maths', 'english', 'python']
        # })
        bookings = http.request.env['hr.applicant'].search([])
        return http.request.render('web_hr_recruit.htl_bookings', {
            'bookings': bookings
            })

    @http.route('/recruitment/form', type='http', auth='public', website=True)
    def recruitment_weform(self, **kwargs):
        return http.request.render('web_hr_recruit.create_recruit_web_form', {})

    @http.route('/create/recruitment', type='http', auth='public', website=True)
    def create_web_recruitment(self, **kwargs):
        request.env['hr.applicant'].sudo().create(kwargs)
        return http.request.render('web_hr_recruit.recruit_thanks', {})


