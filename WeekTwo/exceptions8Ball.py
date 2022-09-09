import requests

question = input('Enter your question for the magic 8 ball: ')

magic_8_ball_url = f'https://8ball.delegator.com/magic/JSON/{question}'
try:
    response = requests.get(magic_8_ball_url).json()

    answer = response['magic']['answer']

    print(f'The magic 8 ball says....  {answer}')
except Exception as e: # Exception lets you print the error message for developping
    print(e)
    print('Sorry, can\'t contact the magic 8 ball right now.')