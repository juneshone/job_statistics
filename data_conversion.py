import requests


def get_vacancies_data(url, headers, payload):
    response = requests.get(url, headers=headers, params=payload)
    response.raise_for_status()
    vacancies = response.json()
    return vacancies


def predict_salary_sj(salary_from, salary_to):
    if salary_from and salary_to:
        return (salary_from + salary_to) * 0.5
    elif not salary_to and salary_from:
        return salary_from * 1.2
    elif not salary_from and salary_to:
        return salary_to * 0.8
    else:
        return None


def get_average_salary(salaries):
    salaries_list = [i for i in salaries if i is not None]
    try:
        average_salary = sum(salaries_list) / len(salaries_list)
    except ZeroDivisionError:
        average_salary = 0
    return int(average_salary)


def get_count_of_vacancies(salaries):
    salaries_list = [i for i in salaries if i is not None]
    return len(salaries_list)
