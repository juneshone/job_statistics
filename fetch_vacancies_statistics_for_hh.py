import time
from itertools import count
from data_conversion import (get_vacancies,
                             predict_salary)
from requests.exceptions import HTTPError


def fetch_hh_salaries(language):
    url = 'https://api.hh.ru/vacancies/'
    moscow_city_id = 1
    publication_period = 30
    vacancies_count_on_page = 100
    vacancies_found = 0
    vacancies_salaries = []
    for page in count(0):
        payload = {
            'text': language,
            'area': moscow_city_id,
            'period': publication_period,
            'per_page': vacancies_count_on_page,
            'page': page
        }
        try:
            page_vacancies = get_vacancies(url, None, payload)
            vacancies_found = page_vacancies['found']
            for vacancy in page_vacancies['items']:
                if vacancy['salary']:
                    vacancies_salaries.append(predict_rub_salary_hh(vacancy['salary']))
        except HTTPError:
            time.sleep(30)
            break
    return vacancies_salaries, vacancies_found


def predict_rub_salary_hh(vacancy):
    salary_from = vacancy['from']
    salary_to = vacancy['to']
    if vacancy['currency'] == 'RUR':
        return predict_salary(salary_from, salary_to)
    else:
        return None
