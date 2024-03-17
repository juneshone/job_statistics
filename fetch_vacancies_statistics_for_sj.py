from itertools import count
from data_conversion import (get_vacancies,
                             predict_salary)


def fetch_sj_salaries(api_key, language):
    url = 'https://api.superjob.ru/2.0/vacancies/'
    headers = {
        'X-Api-App-Id': api_key
    }
    moscow_city = 4
    publication_period = 30
    industry_id = 48
    vacancies_found = 0
    vacancies_salaries = []
    for page in count(0):
        payload = {
            'keyword': language,
            'town': moscow_city,
            'period': publication_period,
            'catalogues': industry_id,
            'page': page
        }
        page_vacancies = get_vacancies(url, headers, payload)
        vacancies_found = page_vacancies['total']
        for vacancy in page_vacancies['objects']:
            vacancies_salaries.append(predict_rub_salary_sj(vacancy))
        if not page_vacancies['more']:
            break
    return vacancies_salaries, vacancies_found


def predict_rub_salary_sj(vacancy):
    salary_from = vacancy['payment_from']
    salary_to = vacancy['payment_to']
    if vacancy['currency'] == 'rub':
        return predict_salary(salary_from, salary_to)
    else:
        return None
