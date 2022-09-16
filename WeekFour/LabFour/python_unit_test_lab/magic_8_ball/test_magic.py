""" TODO create a test case to test the following functions,

generate_url_for_question
 - check that the expected URL is returned for an example question. 

extract_answer_from_response
 - one test should create some example dictionaries that match the expected response from the API,
 and check that the correct answer is extracted and returned.
 - another test should create example dictionaries with a different structure to the one returned from the API, 
 and check that the function returns None. 

 TODO to think about - what else could you test about this program? 
 What types of expected and unexpected behavior might happen? You may be able to write tests for some 
 of your ideas now. We'll talk about ways to test other aspects of this program in class.


 Other tests could be for if the internet is down. we could test to see if it is correctly raising the exception in that try except block
 
 We could test to see if the quetions are actually in a string format, what happens if the user just types numbers.

 How do we handle it if there are lists for the response.

 what should we do if there is no question?

"""
from unittest import TestCase
import functions_magic

class TestFunctionsMagic(TestCase):

    def test_generate_url_for_question_returns_correct_url(self):
        actual_url = functions_magic.generate_url_for_question('Will I drink coffee today?')
        expected_url = f'https://8ball.delegator.com/magic/JSON/Will I drink coffee today?'
        self.assertEqual(expected_url,actual_url)

    def test_extract_answer_from_response_with_expected_response(self):
        expected_response_dictionary = {'magic':{'question':'Will I win the lottery?','answer':'Absolutly Not','type':'Negative'}}

        self.assertEqual('Absolutly Not', functions_magic.extract_answer_from_response(expected_response_dictionary))


    def test_extract_answer_from_response_with_unexpected_dictionaries(self):
        unexpected_response_no_magic = {'eightBall':{'question':'Is this Fun?','answer':'Yes','type':'affirmative'}}

        unexpected_response_no_answer = {'magic':{'question':'Is this Fun?','response':'Definitly','type':'affirmative'}}

        self.assertIsNone(functions_magic.extract_answer_from_response(unexpected_response_no_magic))

        self.assertIsNone(functions_magic.extract_answer_from_response(unexpected_response_no_answer))

        
