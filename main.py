import time

General_knowledge = {
    'What country has the largest population in the world?': 'India',
    'What is the largest planet in our solar system': 'Jupiter',
    'Who wrote the play romeo and Juliet': 'Shakespear'
}

Math = {
    'What is the derivative of 3x² + 5x': '6x+5',
    'If a triangle has sides 6, 8, and 10, what type of triangle is it?': 'right angled triangle',
    'Convert 0.375 into a fraction': '37.5/100'
}

Programming = {
    'What does OOP stand for in programming': 'Object Oriented Programming',
    'In python, what keyword is used to define a function': 'def',
    'What data structure uses variables to vars': 'lists'
}

print('Welcome to quiz game, to quit type "quit"')
point = 0

while True:
    decision = input('Choose subject: math / programming / general_knowledge: ').lower()

    if decision in ['general_knowledge', 'general', 'gk']:
        for key, answer in General_knowledge.items():
            print(key)
            start = time.time()
            user_q = input('> ')
            end = time.time()
            duration = end - start

            if duration > 15:
                print('Too slow. No point.')
                continue

            if user_q.lower() == answer.lower():
                print('Correct')
                point += 1
            else:
                print('Incorrect')
                continue

    elif decision in ['math', 'maths']:
        for key, answer in Math.items():
            print(key)
            start = time.time()
            user_q = input('> ')
            end = time.time()
            duration = end - start

            if duration > 15:
                print('Time out. No point.')
                continue

            if user_q.lower() == answer.lower():
                print('Correct')
                point += 1
            else:
                print('Incorrect')
                continue

    elif decision in ['programming', 'code']:
        for key, answer in Programming.items():
            print(key)
            start = time.time()
            user_q = input('> ')
            end = time.time()
            duration = end - start

            if duration > 25:
                print('Too slow.')
                continue

            if user_q.lower() == answer.lower():
                print('Correct')
                point += 1
            else:
                print('Wrong.')
                continue

    print(f'\nScore: {point}')
    quit_choice = input('Quit? (y/n): ')
    if quit_choice.lower() == 'y':
        print('Goodbye')
        break
            
                
        
