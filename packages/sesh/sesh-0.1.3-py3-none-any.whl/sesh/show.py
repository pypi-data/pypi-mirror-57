"""
Sesh is a tool for managing music classes from the command line.
Copyright (C) 2019  Brian Farrell

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

Contact: brian.farrell@me.com
"""

import calendar
from datetime import datetime
import os
import sqlite3

from sesh.config.base_config import SESH_DB_PATH
from sesh.enum import Esc

SEP_COUNT = 4
SEP = ' ' * SEP_COUNT


def _get_conn_cursor():
    conn = sqlite3.connect(SESH_DB_PATH, detect_types=sqlite3.PARSE_DECLTYPES)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    return conn, cursor


def _show_account(args, kwargs):
    start, stop = _get_start_stop(args)
    kwargs['start'] = start
    kwargs['stop'] = stop
    time_span = datetime.strftime(start, '%B, %Y')
    header = (
        f"{Esc.BOLD}{Esc.BLUE}Accounting Report for {time_span}"
        f"{Esc.END}"
    )
    data = _get_account_data(args, kwargs)

    _show_result(header, data, args, kwargs)


def _show_instrument(args, kwargs):
    header = f"Instrument Report for "
    data = _get_account_data(args, kwargs)

    _show_result(header, data, args, kwargs)


def _show_schedule(args, kwargs):
    header = f"Schedule Report for "
    data = _get_account_data(args, kwargs)

    _show_result(header, data, args, kwargs)

#####################
# Get Data
#####################


def _get_start_stop(args):
    if args.month:
        start = datetime.strptime(args.month, '%m-%Y')
        month_info = calendar.monthrange(
            start.year, start.month
        )
        stop = datetime(
            start.year, start.month, month_info[1], 23, 59, 59
        )

    return start, stop


def _get_account_data(args, kwargs):
    conn, cursor = _get_conn_cursor()

    if hasattr(args, 'student') and args.student:
        email = args.student
        sql = \
            """
            SELECT
                cs.student_id,
                u.name_first,
                u.name_last,
                cs.session_start,
                cs.session_stop,
                (strftime('%s', cs.session_stop) -
                 strftime('%s', cs.session_start)) / 3600.0 AS 'duration',
                ei.instrument,
                cs.recording,
                cs.canceled,
                cs.amt_billed,
                cs.amt_paid,
                abs(cs.amt_paid - cs.amt_billed) AS 'amt_due'
            FROM class_session cs
            JOIN enum_instrument ei
            JOIN user u
            WHERE ei.id = cs.instrument_id
            AND u.id = cs.student_id
            AND cs.session_start >= ?
            AND cs.session_stop <= ?
            AND u.email_addr = ?
            ORDER BY session_start
            """
        records = cursor.execute(sql, (kwargs['start'], kwargs['stop'], email))
    else:
        sql = \
            """
            SELECT
                cs.student_id,
                u.name_first,
                u.name_last,
                cs.session_start,
                cs.session_stop,
                (strftime('%s', cs.session_stop) -
                 strftime('%s', cs.session_start)) / 3600.0 AS 'duration',
                ei.instrument,
                cs.recording,
                cs.canceled,
                cs.amt_billed,
                cs.amt_paid,
                abs(cs.amt_paid - cs.amt_billed) AS 'amt_due'
            FROM class_session cs
            JOIN enum_instrument ei
            JOIN user u
            WHERE ei.id = cs.instrument_id
            AND u.id = cs.student_id
            AND cs.session_start >= ?
            AND cs.session_stop <= ?
            ORDER BY name_last, name_first, session_start
            """

        records = cursor.execute(sql, (kwargs['start'], kwargs['stop']))

    return records


def _get_sum_amt_due(user_id, kwargs):
    conn, cursor = _get_conn_cursor()

    sql = \
        """
        SELECT SUM(abs(cs.amt_paid - cs.amt_billed)) AS total_due
        FROM class_session cs
        JOIN user u
        WHERE u.id = cs.student_id
        AND cs.student_id = ?
        AND cs.session_start >= ?
        AND cs.session_stop <= ?
        """

    record = cursor.execute(sql, (user_id, kwargs['start'], kwargs['stop']))

    return record


def _get_instrument_data(args, kwargs):
    pass


def _get_schedule_data(args, kwargs):
    pass


#####################
# SHOW RESULT
#####################


def _show_result(header, data, args, kwargs):
    if args.csv:
        _output_csv(header, data, args, kwargs)
    elif args.json:
        _output_json(header, data, args, kwargs)
    else:
        _output_table(header, data, args, kwargs)


def _get_table_len(records, args, kwargs):
    table_len = 0
    tabs = 0
    name_string = [f"{r['name_first']} {r['name_last']}" for r in records]
    kwargs['max_name_len'] = max([len(s) for s in name_string])
    table_len += kwargs['max_name_len']
    kwargs['session_date_len'] = 28
    table_len += kwargs['session_date_len']
    kwargs['duration_len'] = 8
    table_len += kwargs['duration_len']

    if args.verbose or os.environ.get('SESH_ALWAYS_VERBOSE'):
        instrument_string = [f"{r['instrument']}" for r in records]
        kwargs['max_instrument_len'] = max([len(s) for s in instrument_string])
        table_len += kwargs['max_instrument_len']
        kwargs['canceled_len'] = 8
        table_len += kwargs['canceled_len']
        kwargs['recorded_len'] = 8
        table_len += kwargs['recorded_len']
        tabs += 3

    kwargs['amt_len'] = 8
    table_len += (kwargs['amt_len'] * 3)
    tabs += 5
    table_len += (tabs * SEP_COUNT)

    return table_len

#####################
# CSV Output
#####################


def _output_csv(header, data, args):
    pass


#####################
# JSON Output
#####################


def _output_json(header, data, args):
    pass


#####################
# Table Output
#####################


def _output_table(header, data, args, kwargs):
    # Format
    records = list(data)
    table_len = _get_table_len(records, args, kwargs)

    # HEADER
    _print_header(header, table_len)

    # BODY
    head_row = [
        'Name'.rjust(kwargs['max_name_len']),
        'Session Date'.ljust(kwargs['session_date_len']),
        'Duration'.ljust(kwargs['duration_len']),
        'Billed'.rjust(kwargs['amt_len']),
        'Paid'.rjust(kwargs['amt_len']),
        'Due'.rjust(kwargs['amt_len'])
    ]

    if args.verbose or os.environ.get('SESH_ALWAYS_VERBOSE'):
        verbose_row = [
            'Instrument'.ljust(kwargs['max_instrument_len']),
            'Recorded'.ljust(kwargs['recorded_len']),
            'Canceled'.ljust(kwargs['canceled_len']),
        ]

        li = 3

        for field in verbose_row:
            head_row.insert(li, field)
            li += 1

    for field in head_row:
        print(f"{field}", end=SEP)

    print(f"\n{'-' * table_len}\n")

    amt_billable = 0.0
    name_first = None
    name_last = None
    student_id = None
    record_count = len(records)
    for i, record in enumerate(records):
        prev_name_first = name_first
        prev_name_last = name_last
        if i != 0:
            prev_id = student_id
        else:
            prev_id = record['student_id']

        name_first = record['name_first']
        name_last = record['name_last']
        student_id = record['student_id']

        kwargs['session_start'] = datetime.strptime(
            record['session_start'], '%Y-%m-%d %H:%M:%S'
        ).strftime('%b %d   %I:%M %p')

        kwargs['session_stop'] = datetime.strptime(
            record['session_stop'], '%Y-%m-%d %H:%M:%S'
        ).strftime('%I:%M %p')

        if ((name_first == prev_name_first and name_last == prev_name_last) or
                prev_name_first is None and prev_name_last is None):
            # We are still in the same set of student records
            _print_record(record, table_len, args, kwargs)
            if i + 1 == record_count:
                td = _get_sum_amt_due(prev_id, kwargs)
                total_due = td.fetchone()['total_due']
                amt_billable += total_due
                _print_total_due(total_due, table_len, kwargs)
        else:
            # We have a new set of student records
            td = _get_sum_amt_due(prev_id, kwargs)
            total_due = td.fetchone()['total_due']
            amt_billable += total_due
            _print_total_due(total_due, table_len, kwargs)
            print("\n")
            _print_record(record, table_len, args, kwargs)

    # FOOTER
    _print_footer(table_len, amt_billable, kwargs)


def _print_header(header, table_len):
    header = '\n' + header
    header += f'\n{"=" * table_len}\n'
    print(header)


def _print_record(record, table_len, args, kwargs):
    r = record

    print(
        f"{r['name_first']} "
        f"{r['name_last'] if r['name_last'] is not None else ''}"
        .rjust(kwargs['max_name_len']),
        end=SEP,
    )
    print(
        f"{kwargs['session_start']} - {kwargs['session_stop']}".ljust(
            kwargs['session_date_len']
        ),
        end=SEP
    )

    print(
        f"{r['duration']} h".rjust(kwargs['duration_len']),
        end=SEP
    )

    if args.verbose or os.environ.get('SESH_ALWAYS_VERBOSE'):
        print(
            f"{r['instrument']}".ljust(kwargs['max_instrument_len']),
            end=SEP
        )

        if r['recording'] == 0:
            recorded_value = '-'.rjust(kwargs['recorded_len'] // 2)
        else:
            recorded_value = 'Y'.rjust(kwargs['recorded_len'] // 2)

        print(
            f"{recorded_value}".ljust(kwargs['recorded_len']), end=SEP
        )

        if r['canceled'] == 0:
            canceled_value = '-'.rjust(kwargs['canceled_len'] // 2)
        else:
            canceled_value = 'Y'.rjust(kwargs['canceled_len'] // 2)

        print(
            f"{canceled_value}".ljust(kwargs['canceled_len']), end=SEP
        )

    print(
        f"{r['amt_billed']:.2f}".rjust(kwargs['amt_len']),
        end=SEP
    )

    print(
        f"{r['amt_paid']:.2f}".rjust(kwargs['amt_len']),
        end=SEP
    )

    print(
        f"{r['amt_due']:.2f}".rjust(kwargs['amt_len'])
    )


def _print_total_due(total_due, table_len, kwargs):
    sub_total_line = f'\n{"-" * table_len}'
    print(f"{sub_total_line}")

    total_due_label_len = table_len - (kwargs['amt_len'] + SEP_COUNT)

    print("Total Due: ".rjust(total_due_label_len), end=SEP)
    print(f"{total_due:.2f}".rjust(kwargs['amt_len']))


def _print_footer(table_len, amt_billable, kwargs):
    # FOOTER
    amt_label_len = table_len - (kwargs['amt_len'] + SEP_COUNT)
    time_span = datetime.strftime(kwargs['start'], '%B, %Y')
    print(f"\n{'=' * table_len}")
    print(f"Total Billable For {time_span}: ".rjust(amt_label_len), end=SEP)
    print(f"{amt_billable:.2f}".rjust(kwargs['amt_len']))
    print('\n')
