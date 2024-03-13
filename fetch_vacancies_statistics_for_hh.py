from data_conversion import (get_vacancies_data,
                             get_average_salary,
                             get_count_of_vacancies,
                             predict_salary)


def fetch_hh_statistics(language, hh_vacancies_statistics):
    url = 'https://api.hh.ru/vacancies/'
    town_name = 1
    publication_period = 30
    vacancies_count_on_page = 20
    payload = {
        'text': language,
        'area': town_name,
        'period': publication_period,
        'per_page': vacancies_count_on_page,
    }
    vacancies = get_vacancies_data(url, None, payload)
    vacancies_salaries = []
    page = 0
    while page < vacancies['pages']:
        page += 1
        for vacancy in vacancies['items']:
            if not vacancy['salary']:
                continue
            vacancies_salaries.append(predict_rub_salary_hh(vacancy['salary']))
    hh_vacancies_statistics[language] = {
        'vacancies_found': vacancies['found'],
        'vacancies_processed': get_count_of_vacancies(vacancies_salaries),
        'average_salary': get_average_salary(vacancies_salaries)
    }
    return hh_vacancies_statistics


def predict_rub_salary_hh(vacancy):
    salary_from = vacancy['from']
    salary_to = vacancy['to']
    if vacancy['currency'] == 'RUR':
        return predict_salary(salary_from, salary_to)
    else:
        return None
