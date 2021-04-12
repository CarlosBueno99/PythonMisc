valid_java=['1.6','1.7','1.8','1.9']
host_java='1.5'

if host_java in valid_java:
    print('host consist of valid Java version')

else:
    print('host deployed with invalid Java version')

db_user=['db_admin','cd_conf','db_installation']


random_user = 'db_admin'
if random_user in db_user:
    print('this user is allowed to start the db')
else:
    print('this user is not in a valid permission group to start the db')