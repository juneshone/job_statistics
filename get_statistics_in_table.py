from terminaltables import AsciiTable


def get_table(vacancies_statistics, table_title):
    table_data = [
        [
            'Язык программирования',
            'Вакансий найдено',
            'Вакансий обработано',
            'Средняя зарплата'
        ]
    ]
    for language, language_value in vacancies_statistics.items():
        table_data.append(
            [
                language,
                language_value['vacancies_found'],
                language_value['vacancies_processed'],
                language_value['average_salary']
            ]
        )
    table = AsciiTable(table_data, table_title)
    return table.table
