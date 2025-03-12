"""

Export CSV
Doc2Doc should be able to prepare and export a CSV file of whatever data you input. Comma-Separated Values are a ubiquitous text format that allows for information to be structured in a table. There is usually a header row, followed by data rows. Within rows, items are separated by commas.

Assignment
Complete the get_csv_status function. It should use a match case statement to select the correct response depending on the status of the export operation. Create functions to handle each operation as follows:

PENDING:
Return a tuple with the string "Pending..." and the data converted from a list of lists of anything, to a list of lists of strings. Try to use nested map functions to convert the data items into strings. Remember to convert from a map object back into a list.

PROCESSING:
Return a tuple with the string "Processing..." and the data converted from a list of lists of strings into one string in CSV format.

For each list of strings, combine the strings with join with commas inbetween to form a row.
For each row string, combine the strings with join with newlines "\n" inbetween to form a table.
SUCCESS:
Return a tuple with the string "Success!" and simply return the data as is.

FAILURE:
Return a tuple with the string "Unknown error, retrying..." and the data after it has been prepared and processed into a CSV string, by combining the steps for Pending and Processing.

Any Other Status:
If the input status is none of the above, raise an Exception with the string "unknown export status".

"""

from enum import Enum


class CSVExportStatus(Enum):
    PENDING = 1
    PROCESSING = 2
    SUCCESS = 3
    FAILURE = 4


def get_csv_status(status, data):
    match status:
        case CSVExportStatus.PENDING:
            def convert_to_string(item):
                if isinstance(item, list):
                    new_list = []
                    for value in item:
                        new_list.append(str(value))
                    return new_list
                else:
                    return str(value)
            return ("Pending...", list(map(convert_to_string, data)))
        case CSVExportStatus.PROCESSING:
            new_string = ""

            for item in data:
                if isinstance(item, list):
                    new_string += ",".join(item)
                new_string += "\n"
            return ("Processing...", new_string[:len(new_string)-1:])
        case CSVExportStatus.SUCCESS:
            return ("Success!", data)
        case CSVExportStatus.FAILURE:
            data = get_csv_status(CSVExportStatus.PENDING, data)
            data = get_csv_status(CSVExportStatus.PROCESSING, data[1])
            return ("Unknown error, retrying...", data[1])
        case _:
            raise Exception("unknown export status")
