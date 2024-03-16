from itertools import count
from data_conversion import (get_vacancies_data,
                             get_salary_calculation,
                             predict_salary)


def fetch_sj_statistics(api_key, language, sj_vacancies_statistics):
    url = 'https://api.superjob.ru/2.0/vacancies/'
    headers = {
        'X-Api-App-Id': api_key
    }
    town_name = 4
    publication_period = 30
    industry_id = 48
    vacancies_found = 0
    vacancies_salaries = []
    for page in count(0):
        payload = {
            'keyword': language,
            'town': town_name,
            'period': publication_period,
            'catalogues': industry_id,
            'page': page
        }
        page_vacancies = get_vacancies_data(url, headers, payload)
        vacancies_found = page_vacancies['total']
        for vacancy in page_vacancies['objects']:
            vacancies_salaries.append(predict_rub_salary_sj(vacancy))
        if page_vacancies['more'] is False:
            break
    salary_calculation = get_salary_calculation(vacancies_salaries)
    sj_vacancies_statistics[language] = {
        'vacancies_found': vacancies_found,
        'vacancies_processed': salary_calculation[1],
        'average_salary': salary_calculation[0]
    }
    return sj_vacancies_statistics


def predict_rub_salary_sj(vacancy):
    salary_from = vacancy['payment_from']
    salary_to = vacancy['payment_to']
    if vacancy['currency'] == 'rub':
        return predict_salary(salary_from, salary_to)
    else:
        return None
