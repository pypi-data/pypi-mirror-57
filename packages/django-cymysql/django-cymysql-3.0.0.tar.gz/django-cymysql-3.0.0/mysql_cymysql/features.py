from django.db.backends.mysql.features import DatabaseFeatures as BaseDatabaseFeatures


class DatabaseFeatures(BaseDatabaseFeatures):
    empty_fetchmany_value = []
    supports_paramstyle_pyformat = False
