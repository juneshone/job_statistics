import time
from itertools import count
from data_conversion import (get_vacancies_data,
                             get_salary_calculation,
                             predict_salary)


def fetch_hh_statistics(language, hh_vacancies_statistics):
    url = 'https://api.hh.ru/vacancies/'
    town_name = 1
    publication_period = 30
    vacancies_count_on_page = 100
    vacancies_found = 0
    vacancies_salaries = []
    for page in count(0):
        payload = {
            'text': language,
            'area': town_name,
            'period': publication_period,
            'per_page': vacancies_count_on_page,
            'page': page
        }
        page_vacancies = get_vacancies_data(url, None, payload)
        vacancies_found = page_vacancies['found']
        for vacancy in page_vacancies['items']:
            if not vacancy['salary']:
                continue
            vacancies_salaries.append(predict_rub_salary_hh(vacancy['salary']))
        max_pages_count = 19
        if page >= page_vacancies['pages'] or page >= max_pages_count:
            time.sleep(30)
            break
    salary_calculation = get_salary_calculation(vacancies_salaries)
    hh_vacancies_statistics[language] = {
        'vacancies_found': vacancies_found,
        'vacancies_processed': salary_calculation[1],
        'average_salary': salary_calculation[0]
    }
    return hh_vacancies_statistics


def predict_rub_salary_hh(vacancy):
    salary_from = vacancy['from']
    salary_to = vacancy['to']
    if vacancy['currency'] == 'RUR':
        return predict_salary(salary_from, salary_to)
    else:
        return None
