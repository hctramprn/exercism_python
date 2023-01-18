# -*- coding: utf-8 -*-
from datetime import datetime

# class that initialize each entry object


class LedgerEntry:
    def __init__(self, date, description, change):
        self.date = datetime.strptime(date, '%Y-%m-%d')
        self.description = description
        self.change = change

# creates each entry object


def create_entry(date, description, change):
    entry = LedgerEntry(date, description, change)
    return entry

# formats each entry into the table


def format_entries(currency, locale, entries):
    # sorts the entries A-Z by date, description, change, independently of the locale chosen
    entries_sorted = sorted(entries, key=lambda x: (
        x.date, x.description, x.change))

    # assigns the header and locale formats
    if locale == 'en_US':
        table = ['Date       | Description               | Change       ']
        date_format = '%m/%d/%Y'
        dot_separated_values = False
        negative_parentesis = True
    elif locale == 'nl_NL':
        table = ['Datum      | Omschrijving              | Verandering  ']
        date_format = '%d-%m-%Y'
        dot_separated_values = True
        negative_parentesis = False

    # assigns the currency sign
    if currency == 'USD':
        currency_sign = '$'
    elif currency == 'EUR':
        currency_sign = '€'

    # loops that adds each entry to the table
    for entry in entries_sorted:
        row = ''
        # write entry date to table
        date_table = entry.date.strftime(date_format)

        row += date_table.ljust(10, ' ') + ' | '

        # Write entry description to table
        description_table = entry.description
        if len(description_table) > 22:
            description_table = description_table[0:22] + '...'
        else:
            description_table = description_table.ljust(25, ' ')

        row += description_table + ' | '

        # Write entry change to table
        currency_table = '{:,.2f}'.format(entry.change / 100)
        if dot_separated_values:
            main_currency, fractional_currency = currency_table.split('.')
            new_main_currency = main_currency.replace(',', '.')
            currency_table = new_main_currency + ',' + fractional_currency

        # if the currency is negative, substitute negative sign for parentesis and add the currency sign
        if negative_parentesis:
            if currency_table[0] == '-':
                curr = f'({currency_sign}{currency_table[1:]})'
                currency_table = curr.rjust(13, ' ')
            else:
                curr = f'{currency_sign}{currency_table}'
                currency_table = curr.rjust(12, ' ') + ' '
        else:
            curr = f'{currency_sign} {currency_table}'
            currency_table = curr.rjust(12, ' ') + ' '

        row += currency_table

        table.append(row)

    return '\n'.join(table)
