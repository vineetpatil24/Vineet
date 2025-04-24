# -*- coding: utf-8 -*-
##############################################################################
#
# Odoo, Open Source Management Solution
# Copyright (C) 2025 ZestyBeanz Technologies(<http://www.zbeanztech.com>)R
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
'name': 'Education',
'version': '18.0.0.0',
'summary': 'This Module is for training purposes.',
'description': """This Module is for training purposes.
""",
'category':'',
'author': ' Vineet Patil',
'website': 'www.zbeanztech.com',
"license": "LGPL-3",
'depends': [],
'data': ['security/ir.model.access.csv','views/student.xml','views/course_taken.xml','views/fee_payment.xml','views/menu.xml'],
'test': [],
'demo': [],
'installable': True,
'auto_install': False,
'application': False,
}