import requests
se=requests.session()
se.cookies.update({'visit-Freq': 'Freq 2021'})
response=se.get('https://httpbin.org/cookies',cookies={'visit':'January 2021'})
response_json=response.json()
print(response_json)