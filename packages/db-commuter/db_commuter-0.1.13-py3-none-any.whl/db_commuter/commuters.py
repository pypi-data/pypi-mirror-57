# -*- coding: utf-8 -*-

"""Collection of methods for communication with database.
"""
__all__ = [
    "SQLiteCommuter",
    "PgCommuter"
]

import abc
from datetime import datetime
from io import StringIO
from typing import (
    Any,
    List,
    Optional,
    Sequence,
    Tuple,
    Union
)

import numpy as np
import pandas as pd
import psycopg2
from sqlalchemy import exc
import sqlite3

from .connections import *


class Commuter(abc.ABC):
    """Parent class for communication with SQL database.

    Args:
        connector:
            Instance of connection object.
    """

    def __init__(
            self,
            connector: Union[SQLiteConnector, PgConnector]
    ) -> None:
        self.connector = connector

    @abc.abstractmethod
    def delete_table(self, table_name: str, **kwargs: Any) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def is_table_exist(self, table_name: str) -> bool:
        raise NotImplementedError()

    @abc.abstractmethod
    def execute(
            self,
            cmd: str,
            vars: Optional[Sequence[Any]] = None,
            commit: Optional[bool] = True
    ) -> None:
        """Execute SQL command and commit changes to database.

        Args:
            cmd:
                SQL-query.
            vars:
                Parameters to command, may be provided as sequence or mapping.
            commit:
                Persist changes to database if True.
        """

        raise NotImplementedError()

    @abc.abstractmethod
    def execute_script(
            self,
            path2script: str,
            commit: Optional[bool] = True
    ) -> None:
        """Execute multiple SQL statements separated by semicolon.

        Args:
            path2script:
                Path to .sql script.
            commit:
                Persist changes to database if True.
        """

        raise NotImplementedError()

    def select(
            self,
            cmd: str,
            return_scalar: Optional[bool] = False
    ) -> pd.DataFrame:
        """Select data from table.

        Args:
            cmd:
                SQL query.
            return_scalar:
                if True then return scalar, otherwise return Pandas.DataFrame.

        Returns:
            Query result convert to Pandas.DataFrame
        """

        with self.connector.engine.connect() as conn:
            df = pd.read_sql_query(cmd, conn)

        if return_scalar:
            return df.iloc[0, 0]

        return df

    def insert(
            self,
            table_name: str,
            data: pd.DataFrame,
            schema: Optional[str] = None,
            chunksize: Optional[int] = None
    ) -> None:
        """Insert data from DataFrame to the table.

        Args:
            table_name:
                Name of the database table.
            data:
                Pandas.DataFrame with the data to be inserted.
            schema:
                Name of the database schema.
            chunksize:
                Rows will be written in batches of this size at a time.
        """

        with self.connector.engine.connect() as conn:
            try:
                data.to_sql(
                    table_name,
                    con=conn,
                    schema=schema,
                    if_exists='append',
                    index=False,
                    chunksize=chunksize)
            except (ValueError, exc.IntegrityError) as e:
                raise ValueError(e)


class SQLiteCommuter(Commuter):
    """Methods for communication with SQLite database.

    Args:
        path2db:
            Path to database file.

    """
    def __init__(self, path2db: str) -> None:
        super().__init__(SQLiteConnector(path2db))

    def delete_table(self, table_name: str, **kwargs: Any) -> None:
        self.execute('DROP TABLE IF EXISTS ' + table_name)

    def is_table_exist(self, table_name: str) -> bool:
        cmd = f"""
        SELECT 
            name 
        FROM 
            sqlite_master 
        WHERE 
            type=\'table\' AND 
            name=\'{table_name}\'"""

        data = self.select(cmd)

        if len(data) > 0:
            return data.name[0] == table_name

        return False

    def execute(
            self,
            cmd: str,
            vars: Optional[Sequence[Any]] = None,
            commit: Optional[bool] = True
    ) -> None:
        with self.connector.make_connection() as conn:
            try:
                cur = conn.cursor()

                if vars is None:
                    cur.execute(cmd)
                else:
                    cur.execute(cmd, vars)

                if commit:
                    conn.commit()
            except sqlite3.DatabaseError as e:
                # roll back the pending transaction
                if commit:
                    conn.rollback()
                raise e

        self.connector.close_connection()

    def execute_script(
            self,
            path2script: str,
            commit: Optional[bool] = True
    ) -> None:
        with open(path2script, 'r') as fh:
            script = fh.read()

        with self.connector.make_connection() as conn:
            cur = conn.cursor()
            cur.executescript(script)

            if commit:
                conn.commit()

        self.connector.close_connection()


class PgCommuter(Commuter):
    """PostgreSQL communication agent.

    Args:
        host:
            Database host address.
        port:
            Connection port number.
        user:
            User name.
        password:
            User password.
        db_name:
            The database name.

    Keyword args:
        schema:
            If schema is specified, then setting a connection to the schema only.

    Example:

          .. code::

          >>> conn_params = {
          'host': 'localhost', 'port': '5432',
          'user': 'postgres', 'password': 'password'}
          >>> commuter = PgCommuter(**conn_params)

    """

    def __init__(
            self,
            host: Optional[str] = None,
            port: Optional[str] = None,
            user: Optional[str] = None,
            password: Optional[str] = None,
            db_name: Optional[str] = None,
            **kwargs: str
    ) -> None:
        super().__init__(PgConnector(host, port, user, password, db_name, **kwargs))

    def execute(
            self,
            cmd: str,
            vars: Optional[Sequence[Any]] = None,
            commit: Optional[bool] = True
    ) -> None:
        with self.connector.make_connection() as conn:
            try:
                with conn.cursor() as cur:
                    if vars is None:
                        cur.execute(cmd)
                    else:
                        cur.execute(cmd, vars)

                if commit:
                    conn.commit()
            except psycopg2.DatabaseError as e:
                # roll back the pending transaction
                if commit:
                    conn.rollback()
                raise e

        self.connector.close_connection()

    def execute_script(
            self,
            path2script: str,
            commit: Optional[bool] = True
    ) -> None:
        with open(path2script, 'r') as fh:
            script = fh.read()

        with self.connector.make_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(script)

            if commit:
                conn.commit()

        self.connector.close_connection()

    def insert_row(
            self,
            table_name: str,
            schema: Optional[str] = None,
            return_id: Optional[str] = None,
            **kwargs: Any
    ) -> Union[int, None]:
        """Implements `INSERT INTO ... VALUES ...` command.

        Args:
            table_name:
                Name of the table to insert.
            schema:
                Name of the database schema.
            return_id:
                Name of the returned serial key.

        Example:
            .. code::
                >>> commuter.insert_row('people', name='Yeltsin', age=72)

        """

        sid = None
        table_name = self._get_table_name(table_name, schema=schema)

        keys = ', '.join(kwargs.keys())
        values = ''

        for key in kwargs.keys():
            if len(values) > 0:
                values += ','

            value = kwargs[key]

            if isinstance(value, datetime):
                values += f'\'{value}\''
            elif isinstance(value, str):
                values += f'\'{value}\''
            else:
                values += str(value)

        cmd = 'INSERT INTO ' + table_name + ' (' + keys + ') '
        cmd += 'VALUES (' + values + ')'

        if return_id is not None:
            sid = self.insert_return(cmd, return_id=return_id)
        else:
            self.execute(cmd)

        return sid

    def insert_return(
            self,
            cmd: str,
            values: Optional[Sequence[Any]] = None,
            return_id: Optional[str] = None
    ) -> int:
        """Insert a new row to the table and return the serial key of
        the newly inserted row.

        Args:
            cmd:
                INSERT INTO command.
            values:
                Inserted values.
            return_id:
                Name of the returned serial key.

        Example:

          .. code::

          >>> cmd = 'INSERT INTO task_manager (task, project) VALUES (%s, %s)'
          >>> values = ('my_task', 'my_project')
          >>> task_id = self.insert_return(cmd, values=values, return_id='task_id')

        """

        sid = None
        cmd += 'RETURNING ' + return_id

        with self.connector.make_connection() as conn:
            try:
                with conn.cursor() as cur:
                    if values is None:
                        cur.execute(cmd)
                    else:
                        cur.execute(cmd, values)

                    sid = cur.fetchone()[0]
                    conn.commit()
            except psycopg2.DatabaseError as e:
                # roll back the pending transaction
                conn.rollback()
                raise e

        self.connector.close_connection()

        return sid

    def insert_fast(
            self,
            table_name: str,
            data: pd.DataFrame,
            schema: Optional[str] = None,
            format_data: Optional[bool] = False
    ) -> None:
        """Places DataFrame to buffer and apply copy_from method.

        Args:
            table_name:
                Name of the table where to insert.
            data
                DataFrame from where to insert.
            schema:
                Name of the schema.
            format_data:
                Reorder columns and adjust dtypes wrt to table metadata.
        """

        if format_data:
            data = self._format_data(data, table_name, schema=schema)

        table_name = self._get_table_name(table_name, schema=schema)

        with self.connector.make_connection() as conn:
            with conn.cursor() as cur:
                # DataFrame to buffer
                s_buf = StringIO()
                data.to_csv(s_buf, index=False, header=False)
                s_buf.seek(0)

                # implement insert
                try:
                    cur.copy_from(s_buf, table_name, sep=',', null='')
                except (ValueError,
                        exc.ProgrammingError,
                        psycopg2.ProgrammingError,
                        psycopg2.IntegrityError) as e:
                    raise ValueError(e)

            conn.commit()

        self.connector.close_connection()

    copy_from = insert_fast

    def delete_table(
            self,
            table_name: str,
            schema: Optional[str] = None,
            cascade: Optional[bool] = False
    ) -> None:
        """Delete table.

        Args:
            table_name:
                Name of the table to delete
            schema:
                Name of the database schema.
            cascade:
                True if delete cascade.
        """

        table_name = self._get_table_name(table_name, schema=schema)
        cmd = f'DROP TABLE IF EXISTS {table_name}'

        if cascade:
            cmd += ' CASCADE'

        self.execute(cmd)

    def is_table_exist(
            self,
            table_name: str,
            schema: Optional[str] = None
    ) -> bool:
        """Return True if table exists, otherwise False.
        """

        schema, table_name = self.get_schema(
            table_name=table_name,
            schema=schema)

        cmd = f"""
        SELECT 
            table_name
        FROM 
            information_schema.tables 
        WHERE 
            table_name = \'{table_name}\' AND 
            table_schema=\'{schema}\'
        LIMIT 1
        """

        with self.connector.make_connection() as conn:
            with conn.cursor() as cur:
                cur.execute(cmd)

        self.connector.close_connection()

        return bool(cur.rowcount)

    def get_columns(
            self,
            table_name: str,
            schema: Optional[str] = None
    ) -> Union[List[str], pd.DataFrame]:
        """Return columns attributes of the given table.

        Args:
            table_name:
                Name of the table.
            schema:
                Name of the schema.

        Returns:
            Pandas.DataFrame having following columns:
                column_name, data_type.
        """

        schema, table_name = self.get_schema(
            table_name=table_name,
            schema=schema)

        cmd = f"""
        SELECT 
            column_name, data_type
        FROM 
            information_schema.columns
        WHERE 
            table_schema = \'{schema}\' AND 
            table_name = \'{table_name}\'
        ORDER BY 
            ordinal_position;
        """

        columns = self.select(cmd)

        return columns

    def get_connections_count(self):
        """Returns the amount of active connections.
        """

        cmd = f'SELECT SUM(numbackends) FROM pg_stat_database'

        return self.select(cmd, return_scalar=True)

    def resolve_primary_conflicts(
            self,
            table_name: str,
            data: pd.DataFrame,
            p_key: List[str],
            filter_col: str,
            schema: Optional[str] = None
    ) -> pd.DataFrame:
        """Resolve primary key conflicts in DataFrame.

        This method selects data from `table_name` where value in `filter_col`
        is greater or equal the minimal found value in `filter_col` of the given DataFrame.
        Rows having primary key which is already presented in selected data
        are deleted from the DataFrame.

        Args:
            table_name:
                Name of the table.
            data:
                DataFrame from where rows having existing primary key need to be deleted.
            p_key:
                Primary key columns.
            filter_col:
                Column used when querying the data from table.
            schema:
                Name of the schema.

        Returns:
            pd.DataFrame
        """

        table_name = self._get_table_name(table_name, schema=schema)

        df = data.copy()

        min_val = df[filter_col].min()
        cmd = f'SELECT * FROM {table_name} WHERE {filter_col} >= '

        if isinstance(min_val, pd.Timestamp):
            cmd += f'\'{min_val}\''
        else:
            cmd += f'{min_val}'

        # select from table
        table_data = self.select(cmd)

        # remove conflicting rows
        if not table_data.empty:
            df.set_index(p_key, inplace=True)
            table_data.set_index(p_key, inplace=True)

            # remove rows which are in table data index
            df = df[~df.index.isin(table_data.index)]
            # reset index and sort columns
            df = df.reset_index(level=p_key)
            df = df[data.columns]

        return df

    def resolve_foreign_conflicts(
            self,
            parent_table_name: str,
            data: pd.DataFrame,
            f_key: List[str],
            filter_parent: str,
            filter_child: str,
            schema: Optional[str] = None
    ) -> pd.DataFrame:
        """Resolve foreign key conflicts in DataFrame.

        This method selects data from `parent_table_name` where value in `filter_parent` column
        is greater or equal the minimal found value in `filter_child` column of the given DataFrame.
        Rows having foreign key which is already presented in selected data
        are deleted from DataFrame.

        Args:
            parent_table_name:
                Name of the parent table.
            data:
                DataFrame from where rows having existing foreign key need to be deleted.
            f_key:
                Foreign key columns.
            filter_parent:
                Column used when querying the data from parent table.
            filter_child:
                Column used when searching for minimal value in child.
            schema:
                Name of the schema.

        Returns:
            pd.DataFrame
        """

        parent_table_name = self._get_table_name(parent_table_name, schema=schema)

        df = data.copy()

        min_val = df[filter_child].min()
        cmd = f'SELECT * FROM {parent_table_name} WHERE {filter_parent} >= '

        if isinstance(min_val, pd.Timestamp):
            cmd += f'\'{min_val}\''
        else:
            cmd += f'{min_val}'

        table_data = self.select(cmd)

        # remove conflicting rows
        if not table_data.empty:
            df.set_index(f_key, inplace=True)
            table_data.set_index(f_key, inplace=True)

            # remove rows which are not in parent index
            df = df[df.index.isin(table_data.index)]
            # reset index and sort columns
            df = df.reset_index(level=f_key)
            df = df[data.columns]
        else:
            # if parent is empty then cannot insert data
            df = pd.DataFrame()

        return df

    def get_schema(
            self,
            table_name: Optional[str] = None,
            schema: Optional[str] = None
    ) -> Tuple[str, str]:
        """Return schema name and table name.

        Examples:

            .. code::

                >>> self.get_schema(table_name='my_schema.my_table')
                ('my_schema', 'my_table')
                >>> self.get_schema()
                ('public', None)
                >>> commuter.get_schema(schema='my_schema')
                ('my_schema', None)
                >>> commuter.get_schema(
                    table_name='my_schema.my_table', schema='schema_2')
                ('my_schema', 'my_table')

        """

        _schema = self.connector.schema
        _table_name = table_name

        if table_name is not None:
            names = str.split(table_name, '.')

            if len(names) == 2:
                _schema = names[0]
                _table_name = names[1]

                return _schema, _table_name

        if schema is not None:
            _schema = schema
        else:
            _schema = 'public'

        return _schema, _table_name

    def _format_data(
            self,
            df: pd.DataFrame,
            table_name: str,
            schema: Optional[str] = None
    ) -> pd.DataFrame:
        """Formatting DataFrame before applying copy_from.
        """

        # select column attributes
        table_columns = self.get_columns(table_name, schema=schema)

        # adjust dtypes of DataFrame columns
        for row in table_columns.itertuples():
            column = row.column_name

            if row.data_type in ['smallint', 'integer', 'bigint']:
                if df[column].dtype == np.float:
                    df[column] = df[column].astype(int)

        # set columns order according to ordinal position
        df = df[table_columns['column_name'].to_list()]

        return df

    @staticmethod
    def _get_table_name(
            table_name: str,
            schema: Optional[str] = None
    ) -> str:
        """Return name of the table.
        """

        if (schema is None) or (schema == 'public'):
            return table_name

        return schema + '.' + table_name
