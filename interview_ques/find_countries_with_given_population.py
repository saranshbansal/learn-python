#!/bin/python3

import requests


# Complete the function below.
# https://jsonmock.hackerrank.com/api/countries/search?name=
def getCountries(s, p):
    response = requests.get('https://jsonmock.hackerrank.com/api/countries/search?name={}'.format(s))
    result = (response.json())

    count = 0

    for page in range(result['total_pages']):
        next_page = requests.get('https://jsonmock.hackerrank.com/api/countries/search?name={}&page={}'.format(s, page))
        next_page_json = next_page.json()
        result_dict = next_page_json['data']
        results = [c for c in result_dict if c['population'] >= p]

        count += len(results)

    print(count)


getCountries('in', 1000000)
