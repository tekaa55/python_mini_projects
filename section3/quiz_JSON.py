import requests

# get quiz data from remote JSON file
quiz_url = 'https://raw.githubusercontent.com/arditsulceteaching/hosted_files/main/geo.json'
response = requests.get(quiz_url)
quizzes = response.json()
questions = quizzes['quizzes'][0]['questions']


def get_question(question_id):
    for question in questions:
        if int(question_id) == question['id']:
            return question
    return None


question_id = input('Which question`s answer would you like to see? Please enter the question number: ')
quiz_question = get_question(question_id)
if quiz_question is None:
    print('Sorry, the question you entered is invalid')
else:
    print(quiz_question['question'])
    for key in quiz_question['choices']:
        if quiz_question['choices'][key]:
            print(key)
            break
