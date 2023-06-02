def print_operation_table(operation, num_rows=6, num_columns=6):
    for row in range(1, num_rows + 1):
        for column in range(1, num_columns + 1):
            result = operation(row, column)
            print(result, end=' ')
        print()


# Пример использования
print_operation_table(lambda x, y: x * y)
