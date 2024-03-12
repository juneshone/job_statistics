from data_conversion import (get_vacancies_data,
                             get_average_salary,
                             get_count_of_vacancies,
                             predict_salary_sj)


def fetch_statistics_sj(api_key, language, vacancies_statistics_sj):
    url = 'https://api.superjob.ru/2.0/vacancies/'
    headers = {
        'X-Api-App-Id': api_key
    }
    count = 100
    payload = {
        'keyword': language,
        'town': 4,
        'period': 30,
        'catalogues': 48,
        'count': count,
    }
    vacancies = get_vacancies_data(url, headers, payload)
    vacancies_salary = []
    page = 0
    pages = int(vacancies['total'] // count) + 1
    while page < pages:
        page += 1
        for vacancy in vacancies['objects']:
            vacancies_salary.append(predict_rub_salary_sj(vacancy))
    vacancies_statistics_sj[language] = {
        'vacancies_found': vacancies['total'],
        'vacancies_processed': get_count_of_vacancies(vacancies_salary),
        'average_salary': get_average_salary(vacancies_salary)
    }
    return vacancies_statistics_sj


def predict_rub_salary_sj(vacancy):
    salary_from = vacancy['payment_from']
    salary_to = vacancy['payment_to']
    if vacancy['currency'] == 'rub':
        return predict_salary_sj(salary_from, salary_to)
    else:
        return None
