# Tool generate a multiple-choice-quiz from a text file
# Version management:
# 1.0 - initial script
# 1.1 - more details in scrore report

# imports default
import sys
import random

# settings
app_version = 'v1.1'
question_loop = True
questions_dict = dict()
score = 0
question = 0
number_of_answers = 4
mode = 'A-to-B'
wrong_answers_dict = dict()

# Introduction
print('================================')
print('     Multiple Choice Quiz')
print('--------------------------------')
print('Python tool generate a Multiple ')
print('Choice Quiz from a text file')
print('--------------------------------')
print(app_version + ' Conscia - Erwin de Brouwer')
print('================================')
print(' ')
# Get text file
input_file_loop = True
while input_file_loop:
    input_file = input('Text file for quiz input: ')
    input_file_loop = False
    # Check file validity
    try:
        file = open(input_file)
    except:
        print('[ERROR] File can not be opened')
        print(' ')
        input_file_loop = True
# open file
file = open(input_file)
print(' ')
print(' o Opening file succesful')
print(' ')
#
# display choice of modes
print('Choose mode of operation:')
print(' [1] Ask A colomn, answer B colomn.')
print(' [2] Ask B colomn, answer A colomn.')
print(' ')
# Get mode
mode_loop = True
while mode_loop:
    input_mode = input('Mode of the questions: ')
    print(' ')
    mode_loop = False
    # Check answer validity
    try:
        int(input_mode)
        if int(input_mode) is not 0 and int(input_mode) < 3:
            mode_loop = False
            if int(input_mode) == 1:
                mode = 'A-to-B'
            if int(input_mode) == 2:
                mode = 'B-to-A'
        else:
            print('[ERROR] Not a valid option.')
            print(' ')
            mode_loop = True
    except:
        print('[ERROR] Answer not a number.')
        print(' ')
        mode_loop = True
#
# parsing file to dictionary with questions
print(' o Please wait while parsing questions')
if mode == 'A-to-B':
    for line in file:
        line = line.strip()
        line = line.split(',')
        questions_dict[line[0]] = line[1]
    print(' o Parsed questions in A-to-B mode')
if mode == 'B-to-A':
    for line in file:
        line = line.strip()
        line = line.split(',')
        questions_dict[line[1]] = line[0]
    print(' o Parsed questions in B-to-A mode')
#
# print total number of questions parsed
print(' o Total questions parsed = ' + str(len(questions_dict)))
# copy questions to pool-to-ask
questions_to_ask = list(questions_dict)
#
# Start quiz
print(' o Ready to start quiz, good luck!')    
print(' ')
# Any key to start
any_key = input('Press any key to start the quiz...')
print(' ')
# Start question loop random.choice(list(d.keys()))
while question_loop:
    # clear answer list
    answer_list = []
    # reset answer-count
    answer_count = number_of_answers
    # random choose question to ask and clear it from the dictionary questions_to_ask
    random_key = random.choice(questions_to_ask)
    questions_to_ask.remove(random_key)
    # increase question number
    question = question + 1
    # print questions
    print('--- ' + str(question) + '. What is the value linked to ' + random_key + '?')
    # reset the possible answer list
    answers_to_give = list(questions_dict)
    # fill the answer list with possible answers, including the correct one
    correct_answer = questions_dict[random_key]
    answer_list.append(correct_answer)
    answer_count = answer_count - 1
    # getting random other answers
    answers_to_give = list(questions_dict)
    answers_to_give.remove(random_key)
    while answer_count > 0:
        random_answer = random.choice(answers_to_give)
        possible_answer = questions_dict[random_answer]
        answer_list.append(possible_answer)
        answers_to_give.remove(random_answer)
        answer_count = answer_count - 1
    # print possible answers in random order
    random.shuffle(answer_list)
    answer_count = 0
    answer_loop = True
    for answer in answer_list:
        answer_count = answer_count + 1
        print('[' + str(answer_count) + '] ' + answer)
    print('---')
    # Get answer
    while answer_loop:
        answer = input('Correct answer number: ')
        print(' ')
        answer_loop = False
        # Check answer validity
        try:
            int(answer)
            if int(answer) is not 0 and int(answer) < number_of_answers + 1:
                answer_loop = False
            else:
                print('[ERROR] Answer is not valid.')
                print(' ')
                answer_loop = True
        except:
            print('[ERROR] Answer not a number.')
            print(' ')
            answer_loop = True
    # Check answer to correct answer
    if answer_list[int(answer) - 1] == correct_answer:
        score = score + 1
        print('GREAT JOB!')
        print('The answer "' + correct_answer + '" is correct.')
        print(' ')
    else:
        print('STUDY HARDER!')
        print('The answer "' + correct_answer + '" is correct.')
        print(' ')
        wrong_answers_dict[random_key] = correct_answer
    #
    # No questions left
    if len(questions_to_ask) == 0:
        question_loop = False
# give score to candidate
score_float = score/len(questions_dict)*100
score_bar_full = int(round(score_float/2,0))
score_bar_empty = int(50-score_bar_full)
print('==================================================')
print('Your FINAL SCORE REPORT is: ' + str(round(score_float,1)) + "%")
print(str(score) + ' out of ' + str(len(questions_dict)) + ' questions aswered correctly.')
print('--------------------------------------------------')
print('|'*score_bar_full + '_'*score_bar_empty)
print('--------------------------------------------------')
print('INCORRECT ANSWERED questions are:')
for wrong_answer in wrong_answers_dict:
    print(wrong_answer + " = " + wrong_answers_dict[wrong_answer])
print('--------------------------------------------------')
print(' ')
# Close application
any_key = input('Press any key to close this application...')
sys.exit()