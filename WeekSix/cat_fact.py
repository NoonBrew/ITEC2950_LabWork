import requests

try:
    url = 'https://catfact.ninja/fact'
    response = requests.get(url)

    response.raise_for_status() # Raise an exception for 400 or 500 code. Pushes code to the exception block. 
    print(response.status_code)
    print(response.text)
    print(response.json())

    data = response.json()
    fact = data['fact']
    print(f'A random cat fact is {fact}')

except Exception as e:
    print(e)
    print('There was an error making the request.')