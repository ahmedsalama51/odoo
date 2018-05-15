{
    'name': 'Zad Account Bank Statement Auto Reconciliations',
    'version': '10.0.0.1',
    'category': 'Account Bank Statement',
    'summary': 'Accounting, Bank , Statement, Auto, Reconciliations',
    
    'description': """
This module is used for :
==============================================================
- Account Bank Statement:
    - Show account field on bank statement line to do automatic reconcile.\n
    - Add sequence field on each account bank statement. \n
    - Add constrain on statements to add sequence only 1 time for each statement. \n
    - Add Discharge field on each account bank statement to show if it is [Pay To/Income From]. \n
    - Add Receivable Name field on each account bank statement. \n
    - Add Actual Exchange Rate field on each account bank statement. \n
   """,
    'author': 'Ahmed Salama<asalama@zadsolutions.com>',
    'website': 'http://zadsolutions.com',
    'depends': ['account','account_accountant','account_cancel'],
    'data':[
        'security/account_bank_statment_security.xml',
        'views/res_currency_view_changes.xml',
        'views/account_bank_statemnet_line_view.xml',

    ],
    'installable': True,
    'auto_install': False,
}
