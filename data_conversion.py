import requests


def get_vacancies_data(url, headers, payload):
    response = requests.get(url, headers=headers, params=payload)
    response.raise_for_status()
    vacancies = response.json()
    return vacancies


def predict_salary(salary_from, salary_to):
    if salary_from and salary_to:
        return (salary_from + salary_to) * 0.5
    elif not salary_to and salary_from:
        return salary_from * 1.2
    elif not salary_from and salary_to:
        return salary_to * 0.8
    else:
        return None


def get_salary_calculation(salaries):
    salaries_data = [i for i in salaries if i is not None]
    salaries_count = len(salaries_data)
    try:
        average_salary = int(sum(salaries_data) / salaries_count)
    except ZeroDivisionError:
        average_salary = 0
    return average_salary, salaries_count
