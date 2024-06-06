from pynetbox
dr = pynetbox.api(host='10.16.32.17',port=443,use_ssl=True, auth_token='62a2ca8ee97b1d72b6b942d22f0ff87472d8e0a7')

nb_dev_role = netbox.dcim.get_device_roles()
print(nb_dev_role)