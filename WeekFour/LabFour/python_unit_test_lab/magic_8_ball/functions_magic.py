import requests

def main():
    question = input('Enter your question for the magic 8 ball: ')
    magic_8_ball_url = generate_url_for_question(question)
    magic_response = make_request_to_magic_8_ball(magic_8_ball_url)
    if magic_response:
        answer = extract_answer_from_response(magic_response)
        print(f'The magic 8 ball says....  {answer}')


def generate_url_for_question(question):
    url = f'https://8ball.delegator.com/magic/JSON/{question}'
    return url


def make_request_to_magic_8_ball(url):
    try:
        response = requests.get(url).json()
        return response
    except Exception as e:
        print(f'The magic 8 ball is mysteriously unavailable because {e}')


def extract_answer_from_response(response):
    """
    The response is a dictionary in the form

    {
        'magic': {
            'question': 'Will it be sunny tomorrow?', 
            'answer': 'Yes', 
            'type': 'Affirmative'
        }
    }

    This function returns the answer value from the nested dictionary.
    """


    #TODO Think about how to handle non dictionary structures and test for proper error handling
    try:
        answer = response['magic']['answer']
        return answer
    except KeyError:
        return None
    


if __name__ == '__main__':
    main()