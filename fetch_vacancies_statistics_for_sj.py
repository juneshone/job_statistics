from itertools import count
from data_conversion import (get_vacancies_data,
                             get_average_salary,
                             predict_salary)


def fetch_sj_statistics(api_key, language, sj_vacancies_statistics):
    url = 'https://api.superjob.ru/2.0/vacancies/'
    headers = {
        'X-Api-App-Id': api_key
    }
    town_name = 4
    publication_period = 30
    industry_id = 48
    for page in count(0):
        payload = {
            'keyword': language,
            'town': town_name,
            'period': publication_period,
            'catalogues': industry_id,
            'page': page
        }
        page_vacancies = get_vacancies_data(url, headers, payload)
        vacancies_salaries = []
        for vacancy in page_vacancies['objects']:
            vacancies_salaries.append(predict_rub_salary_sj(vacancy))
        sj_vacancies_statistics[language] = {
            'vacancies_found': page_vacancies['total'],
            'vacancies_processed': get_average_salary(vacancies_salaries)[1],
            'average_salary': get_average_salary(vacancies_salaries)[0]
        }
        if page_vacancies['more'] is False:
            break
    return sj_vacancies_statistics


def predict_rub_salary_sj(vacancy):
    salary_from = vacancy['payment_from']
    salary_to = vacancy['payment_to']
    if vacancy['currency'] == 'rub':
        return predict_salary(salary_from, salary_to)
    else:
        return None
