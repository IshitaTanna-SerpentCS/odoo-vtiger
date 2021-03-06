# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.
{
    'name': 'CRM VTiger Integration',
    'version': '10.0.1.0.0',
    'summary': 'CRM VTiger Integration',
    'description': """
        CRM VTiger Integration""",
    'author': 'Serpent Consulting Services Pvt. Ltd.',
    'website': 'https://www.serpentcs.com',
    'category': 'Marketing',
    'license': 'AGPL-3',
    'depends': ['crm',
                'vtiger_connector_partner'],
    'data': ['views/res_company_view.xml',
             'views/crm_view.xml'],
    'installable': True,
}
