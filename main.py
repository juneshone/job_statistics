from environs import Env
from get_statistics_in_table import get_table
from fetch_vacancies_statistics_for_hh import fetch_hh_statistics
from fetch_vacancies_statistics_for_sj import fetch_sj_statistics


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
        hh_vacancies_statistics = fetch_hh_statistics(language, hh_vacancies_statistics)
        sj_vacancies_statistics = fetch_sj_statistics(sj_secret_key,
                                                      language,
                                                      sj_vacancies_statistics)
    print(get_table(hh_vacancies_statistics, hh_table_title))
    print(get_table(sj_vacancies_statistics, sj_table_title))


if __name__ == '__main__':
    main()
