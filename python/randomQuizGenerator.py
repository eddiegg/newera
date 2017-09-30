#! python3
import os, shelve, random

capitals = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
            'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
            'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
            'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
            'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
            'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
            'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
            'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
            'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
            'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'New Mexico':
            'Santa Fe', 'New York': 'Albany', 'North Carolina': 'Raleigh',
            'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
            'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
            'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
            'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
            'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia':
            'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}

for quizNum in range(2):
    answerKeyFile = open('answer%s'%(quizNum+1),'w')
    quizFile = open('quiz%s'%(quizNum+1),'w')
    quizFile.write('''Name:
Date:
Period:
{0}State Capitals Quiz{1} 
        '''.format(' '*20,(quizNum + 1)))
    quizFile.write('\n\n')

    states = list(capitals.keys())
    random.shuffle(states)   #直接打乱了states列表的顺序


    for questionNum in range(50):
        correctAnswer = capitals[states[questionNum]]
        wrongAnswers = list(capitals.values())
        del wrongAnswers[wrongAnswers.index(correctAnswer)]
        wrongAnswers = random.sample(wrongAnswers,3)
        """
        list加入一个元素，加入前把元素放入【】转换成list，注意对比为什么不用list(元素)
        """
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)               #打乱答案顺序

        quizFile.write('{0}. What is the capital of {1}? \n'.format(questionNum+1,
                        states[questionNum]))
        for i in range(4):
            quizFile.write('{0}. {1}\n'.format('ABCD'[i], answerOptions[i]))
        quizFile.write('\n')

        answerKeyFile.write('{0}. {1} \n'.format(questionNum+1, 'ABCD'[answerOptions.index(correctAnswer)]))

    quizFile.close()
    answerKeyFile.close()
