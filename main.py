from environs import Env
from get_statistics_in_table import get_table
from fetch_vacancies_statistics_for_hh import fetch_statistics_hh
from fetch_vacancies_statistics_for_sj import fetch_statistics_sj


def main():
    env = Env()
    env.read_env()
    secret_key_sj = env.str('SECRET_KEY_SJ')
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
    table_title_hh = 'HeadHunter Moscow'
    table_title_sj = 'SuperJob Moscow'
    vacancies_statistics_sj = {}
    vacancies_statistics_hh = {}
    for language in programming_languages:
        vacancies_statistics_hh = fetch_statistics_hh(language, vacancies_statistics_hh)
        vacancies_statistics_sj = fetch_statistics_sj(secret_key_sj,
                                                      language,
                                                      vacancies_statistics_sj)
    print(get_table(vacancies_statistics_hh, table_title_hh))
    print(get_table(vacancies_statistics_sj, table_title_sj))


if __name__ == '__main__':
    main()
