import pymysql

pymysql.version_info = (2, 2, 7, "final", 0)
pymysql.install_as_MySQLdb()

# Bypasses Django 5.2's hard requirement for 8.4+ so 8.0 works seamlessly
from django.db.backends.mysql.base import DatabaseWrapper
DatabaseWrapper.check_database_version_supported = lambda self: None