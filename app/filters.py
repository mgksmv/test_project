# Функция для фильтра колонок, связанные с цифрами (количество и расстояние)
def filter_int_table_objects(table_data, column_value, condition_value, searchbar_value):
    if column_value == 'quantity':
        if condition_value == '=':
            return table_data.filter(quantity=searchbar_value)
        elif condition_value == 'in':
            return table_data.filter(quantity__in=searchbar_value)
        elif condition_value == '>':
            return table_data.filter(quantity__gt=searchbar_value)
        elif condition_value == '<':
            return table_data.filter(quantity__lt=searchbar_value)
    elif column_value == 'distance':
        if condition_value == '=':
            return table_data.filter(distance=searchbar_value)
        elif condition_value == 'in':
            return table_data.filter(distance__in=searchbar_value)
        elif condition_value == '>':
            return table_data.filter(distance__gt=searchbar_value)
        elif condition_value == '<':
            return table_data.filter(distance__lt=searchbar_value)


# Функция для фильтра колонки, связанным со строкой (название)
def filter_str_table_objects(table_data, column_value, condition_value, searchbar_value):
    if column_value == 'name':
        if condition_value == '=':
            return table_data.filter(name=searchbar_value)
        elif condition_value == 'in':
            return table_data.filter(name__icontains=searchbar_value)
