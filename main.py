"""

HTML Table
Doc2Doc should have tools to create HTML boilerplate. One of the features should create a table. An HTML table has a header row and data rows. A header row has headers for the columns. Each normal row has data cells which contain the information in the table. It is essentially a 2-dimensional list.

Example HTML Table:

<table>
  <tr>
    <th>Row 1, Header 1</th>
    <th>Row 1, Header 2</th>
  </tr>
  <tr>
    <td>Row 2, Cell 1</td>
    <td>Row 2, Cell 2</td>
  </tr>
  <tr>
    <td>Row 3, Cell 1</td>
    <td>Row 3, Cell 2</td>
  </tr>
</table>

"td": Each item in a table goes in its own data cell, which are arranged in rows.
"tr": The table row tag goes around each row of cells.
"th": The header cells hold the headers for each column and belong in the first row.
"table": This is the parent tag of the entire table.
Result:

Row 1, Header 1	Row 1, Header 2
Row 2, Cell 1	Row 2, Cell 2
Row 3, Cell 1	Row 3, Cell 2
Assignment
Complete the create_html_table function. It takes a list of lists of strings, data_rows, and returns a function, create_table_headers. create_table_headers should take a list of strings, headers, and convert them into the header row of the table, then return the complete HTML table as a string without any added whitespace or indentation.

Use the provided functions to complete the create_html_table function. Within the create_table_headers function:

Access the nonlocal rows string.
Accumulate the strings in the headers list as header cells in a single table row.
Add the row of headers to the beginning of the rows string.
Add the final tag, "table", around all of the rows.
Return one single string containing the HTML table.

"""

from functools import reduce


def create_tagger(tag):
    def tagger(content):
        return f"<{tag}>{content}</{tag}>"

    return tagger


def create_accumulator(tagger):
    def accumulate(items):
        return reduce(lambda acc, item: acc + tagger(item), items, "")

    return accumulate


tag_data = create_tagger("td")
tag_header = create_tagger("th")
tag_row = create_tagger("tr")
tag_table = create_tagger("table")

accumulate_data_cells = create_accumulator(tag_data)
accumulate_rows = create_accumulator(tag_row)
accumulate_headers = create_accumulator(tag_header)


# don't touch above this line


def create_html_table(data_rows):
    rows = accumulate_rows(map(accumulate_data_cells, data_rows))

    def create_table_headers(headers):
        # ?
        nonlocal rows
        html = "<table><tr>"

#        for header in headers:
#            html += f"<th>{header}</th>"

        def concat_headers(acc, header):
            nonlocal html
            html += f"<th>{acc}</th><th>{header}</th>"
            return html

        html = reduce(concat_headers, headers)

        html += f"</tr>{rows}</table>"
        return html

    return create_table_headers
