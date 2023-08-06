# Copyright (C) 2019  Nexedi SA and Contributors.
#                     Romain Courteaud <romain@nexedi.com>
#
# This program is free software: you can Use, Study, Modify and Redistribute
# it under the terms of the GNU General Public License version 3, or (at your
# option) any later version, as published by the Free Software Foundation.
#
# You can also Link and Combine this program with other software covered by
# the terms of any of the Free Software licenses or any of the Open Source
# Initiative approved licenses and Convey the resulting work. Corresponding
# source of such a combination shall include the source code for all other
# software used.
#
# This program is distributed WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
# See COPYING file for full licensing terms.
# See https://www.nexedi.com/licensing for rationale and options.

import peewee
from playhouse.migrate import migrate, SqliteMigrator
from playhouse.sqlite_ext import SqliteExtDatabase
import datetime


class LogDB:
    def __init__(self, sqlite_path):
        self._db = SqliteExtDatabase(
            sqlite_path, pragmas=(("journal_mode", "WAL"), ("foreign_keys", 1))
        )
        self._db.connect()

        class BaseModel(peewee.Model):
            class Meta:
                database = self._db

        # This store the start, stop, loop time of the bot
        # All other tables point to it to be able to group some info
        class Status(BaseModel):
            text = peewee.TextField()
            timestamp = peewee.TimestampField(
                primary_key=True,
                # Store millisecond resolution
                resolution=6,
                # date is in UTC
                utc=True,
                default=datetime.datetime.now,
            )

        # Store the configuration modification
        class ConfigurationChange(BaseModel):
            status = peewee.ForeignKeyField(Status)
            parameter = peewee.TextField(index=True)
            value = peewee.TextField()

            class Meta:
                primary_key = peewee.CompositeKey("status", "parameter")
                # indexes = (
                # create a unique on from/to/date
                # (('status', 'parameter'), True),
                # )

        # Store the configuration modification
        class PlatformChange(BaseModel):
            status = peewee.ForeignKeyField(Status)
            parameter = peewee.TextField(index=True)
            value = peewee.TextField()

            class Meta:
                primary_key = peewee.CompositeKey("status", "parameter")

        # Store remote network status
        class NetworkChange(BaseModel):
            status = peewee.ForeignKeyField(Status)
            ip = peewee.TextField()
            transport = peewee.TextField()
            port = peewee.IntegerField()
            state = peewee.TextField()

            class Meta:
                primary_key = peewee.CompositeKey(
                    "status", "ip", "transport", "port"
                )

        class DnsChange(BaseModel):
            status = peewee.ForeignKeyField(Status)
            resolver_ip = peewee.TextField()
            domain = peewee.TextField()
            rdtype = peewee.TextField()
            response = peewee.TextField()

            class Meta:
                primary_key = peewee.CompositeKey(
                    "status", "resolver_ip", "domain", "rdtype"
                )

        class HttpCodeChange(BaseModel):
            status = peewee.ForeignKeyField(Status)
            ip = peewee.TextField()
            url = peewee.TextField()
            status_code = peewee.IntegerField()

            class Meta:
                primary_key = peewee.CompositeKey("status", "ip", "url")

        self.Status = Status
        self.ConfigurationChange = ConfigurationChange
        self.PlatformChange = PlatformChange
        self.NetworkChange = NetworkChange
        self.DnsChange = DnsChange
        self.HttpCodeChange = HttpCodeChange

    def createTables(self):
        # http://www.sqlite.org/pragma.html#pragma_user_version
        db_version = self._db.pragma("user_version")
        expected_version = 1
        if db_version == 0:
            with self._db.transaction():
                self._db.create_tables(
                    [
                        self.Status,
                        self.ConfigurationChange,
                        self.HttpCodeChange,
                        self.NetworkChange,
                        self.PlatformChange,
                        self.DnsChange,
                    ]
                )
                self._db.pragma("user_version", expected_version)
        elif db_version != expected_version:
            # migrator = SqliteMigrator(self._db)
            migration_list = []
            sql_query_list = []

            if migration_list or sql_query_list:
                with self._db.transaction():
                    if migration_list:
                        migrate(*migration_list)
                    if sql_query_list:
                        for sql_query in sql_query_list:
                            self._db.execute_sql(
                                sql_query, require_commit=False
                            )
                    self._db.pragma("user_version", expected_version)

    def close(self):
        self._db.close()
