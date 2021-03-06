"""
    后台根据ID修改用户信息
"""

import encoding
import cgi
import re
from com.aowin.connect_table import new_user

f = cgi.FieldStorage()

id = f.getvalue('id')
name = f.getvalue('name')
province = f.getvalue('province')
city = f.getvalue('city')
address = f.getvalue('address')
zip = f.getvalue('zip')
date = f.getvalue('date')

if not id:
    print('access-control-allow-origin: *')
    print('')
    print('必须传入ID', end='')
elif not re.search('[\u4E00-\u9FA50-9a-zA-Z_]{3,6}', name):
    print('access-control-allow-origin: *')
    print('')
    print('用户名错误', end='')
elif not province:
    print('access-control-allow-origin: *')
    print('')
    print('省份必填', end='')
elif not city:
    print('access-control-allow-origin: *')
    print('')
    print('城市必填', end='')
elif not address:
    print('access-control-allow-origin: *')
    print('')
    print('地址必填', end='')
elif not re.search('^[0-9]{6}$', zip):
    print('access-control-allow-origin: *')
    print('')
    print('邮编错误', end='')
elif not re.search(r'(\d{4}-\d{2}-\d{2})', date):
    print('access-control-allow-origin: *')
    print('')
    print('出生日期格式：yyyy-mm-dd', end='')
else:
    up = (name, province, city, address, zip, date, id)
    update = new_user.update(up)
    if up:
        print('access-control-allow-origin: *')
        print('')
        print('success', end='')
    else:
        print('access-control-allow-origin: *')
        print('')
        print('error', end='')
