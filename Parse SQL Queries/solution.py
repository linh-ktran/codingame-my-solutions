# This is a sample Python script.

def get_select():
    tab = sql_query[7:sql_query.index("FROM") - 1].split(", ")
    tab2 = []
    if tab[0] == "*":
        for i in range(len(table_header)):
            tab2.append(get_table_header_index(table_header[i]))
    else:
        for i in range(len(tab)):
            tab2.append(get_table_header_index(tab[i]))
    return tab2


def get_from():
    if "WHERE" in sql_query:
        return sql_query[sql_query.index("FROM") + 5:sql_query.index("WHERE") - 1]
    elif "ORDER BY" in sql_query:
        return sql_query[sql_query.index("FROM") + 5:sql_query.index("ORDER BY") - 1]
    else:
        return sql_query[sql_query.index("FROM") + 5:]


def get_where():
    index = sql_query.find("WHERE")
    if index != -1:
        tab = []
        if "ORDER BY" in sql_query:
            tab = sql_query[index + 6:sql_query.index("ORDER BY") - 1].split(" = ")
        else:
            tab = sql_query[index + 6:].split(" = ")
        tab[0] = get_table_header_index(tab[0])
        return tab
    return None


def get_order_by():
    index = sql_query.find("ORDER BY")
    if index != -1:
        tab = sql_query[index + 9:].split(" ")
        tab[0] = get_table_header_index(tab[0])
        return tab
    return None


def get_table_header_index(string):
    for i in range(len(table_header)):
        if table_header[i] == string:
            return i
    return -1


def write_table_name():
    output = ""
    for i in range(len(select)):
        output += table_header[select[i]] + " "
    print(output[:-1])


def execute_query():
    data_e = []
    for i in range(len(data)):
        line = []
        if where:
            if data[i][where[0]] == where[1]:
                for j in range(len(select)):
                    line.append(data[i][select[j]])
                data_e.append(" ".join(line))
        else:
            for j in range(len(select)):
                line.append(data[i][select[j]])
            data_e.append(" ".join(line))
    if order_by:
        index = 0
        for i in range(len(select)):
            if select[i] == order_by[0]:
                index = i
        data_e.sort(key=lambda x: float(x.split()[index]) if x.split()[index].replace('-', '', 1).replace('.', '',
                                                                                                          1).isdigit() else
        x.split()[index], reverse=(order_by[1] == "DESC"))

    print("\n".join(data_e))


sql_query = input()
ROWS = int(input())
table_header = input().split(" ")

select = get_select()
from_ = get_from()
where = get_where()
order_by = get_order_by()
data = []
for i in range(ROWS):
    table_row = input()
    data.append(table_row.split(" "))

write_table_name()
execute_query()
