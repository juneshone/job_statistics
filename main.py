from environs import Env
from fetch_vacancies_statistics_for_hh import fetch_hh_salaries
from fetch_vacancies_statistics_for_sj import fetch_sj_salaries
from data_conversion import get_statistics
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
    for language, language_statistics in vacancies_statistics.items():
        table_data.append(
            [
                language,
                language_statistics['vacancies_found'],
                language_statistics['vacancies_processed'],
                language_statistics['average_salary']
            ]
        )
    table = AsciiTable(table_data, table_title)
    return table.table


def main():
    env = Env()
    env.read_env()
    sj_secret_key = env.str('SJ_SECRET_KEY')
    programming_languages = [
        'JavaScript',
        'Java',
        'Python',
        'Ruby',
        'PHP',
        'C++',
        'C#',
        'C',
        'Go',
        'Scala'
    ]
    hh_table_title = 'HeadHunter Moscow'
    sj_table_title = 'SuperJob Moscow'
    hh_vacancies_statistics = {}
    sj_vacancies_statistics = {}
    for language in programming_languages:
        hh_vacancies_salaries, hh_vacancies_found = fetch_hh_salaries(language)
        sj_vacancies_salaries, sj_vacancies_found = fetch_sj_salaries(
            sj_secret_key,
            language
        )
        hh_vacancies_statistics[language] = get_statistics(
            hh_vacancies_salaries,
            hh_vacancies_found
        )
        sj_vacancies_statistics[language] = get_statistics(
            sj_vacancies_salaries,
            sj_vacancies_found
        )
    print(get_table(hh_vacancies_statistics, hh_table_title))
    print(get_table(sj_vacancies_statistics, sj_table_title))


if __name__ == '__main__':
    main()
