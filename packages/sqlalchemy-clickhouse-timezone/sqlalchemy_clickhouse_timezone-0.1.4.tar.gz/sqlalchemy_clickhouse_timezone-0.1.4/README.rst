
sqlalchemy-clickhouse-timezone

add timezone support

Installation
------------

The package is installable through PIP::

   pip install sqlalchemy-clickhouse-timezone

Usage
-----
setting the environ param to start timezone support

  default is '0' using pytz.utc

  'CLICKHOUSE_USE_TIMEZONE': '0' => using utc

  'CLICKHOUSE_USE_TIMEZONE': '1' => using system timezone

  'CLICKHOUSE_USE_TIMEZONE': 'Asia/Shanghai' => using configed Asian/Shanghai


configed

   os.environ.setdefault('CLICKHOUSE_USE_TIMEZONE', '0')
   
   os.environ.setdefault('CLICKHOUSE_USE_TIMEZONE', '1')
   
   os.environ.setdefault('CLICKHOUSE_USE_TIMEZONE', 'Asia/Shanghai')

--------------------------------------------------
'infi.clickhouse_orm==1.0.4'
--------------------------------------------------

original project usage...
--------------------------------------------------

ClickHouse dialect for SQLAlchemy.

The DSN format is similar to that of regular Postgres::

    >>> import sqlalchemy as sa
    >>> sa.create_engine('clickhouse://username:password@hostname:port/database')
    Engine('clickhouse://username:password@hostname:port/database')

It implements a dialect, so there's no user-facing API.

Testing
-------

The dialect can be registered on runtime if you don't want to install it as::

    from sqlalchemy.dialects import registry
    registry.register("clickhouse", "base", "dialect")
