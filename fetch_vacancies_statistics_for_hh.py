from data_conversion import (get_vacancies_data,
                             get_average_salary,
                             get_count_of_vacancies,
                             predict_salary)


def fetch_statistics_hh(language, vacancies_statistics_hh):
    url = 'https://api.hh.ru/vacancies/'
    payload = {
        'text': language,
        'area': 1,
        'period': 30,
        'per_page': 20,
    }
    vacancies = get_vacancies_data(url, None, payload)
    vacancies_salary = []
    page = 0
    while page < vacancies['pages']:
        page += 1
        for vacancy in vacancies['items']:
            if not vacancy['salary']:
                continue
            vacancies_salary.append(predict_rub_salary(vacancy['salary']))
    vacancies_statistics_hh[language] = {
        'vacancies_found': vacancies['found'],
        'vacancies_processed': get_count_of_vacancies(vacancies_salary),
        'average_salary': get_average_salary(vacancies_salary)
    }
    return vacancies_statistics_hh


def predict_rub_salary(vacancy):
    salary_from = vacancy['from']
    salary_to = vacancy['to']
    if vacancy['currency'] == 'RUR':
        return predict_salary(salary_from, salary_to)
    else:
        return None
