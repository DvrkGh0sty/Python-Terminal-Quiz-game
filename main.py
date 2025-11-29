import time
import random

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
print('Welcome to quiz game')
point = 0
while True:
    decision = input('What would you like to be tested on: math,programming and General_knowledge: ')
    if decision.lower() in ['general knowledge', 'general']:
        for key, answer in General_knowledge.items():
            print(key)
            start = time.time()
            user_q = input('> ')
            end = time.time()
            duration = end - start
            if duration > 15:
                print('TO long no reward lol')
                if not user_q:
                    print('Bum')
            else:
                if user_q.lower() == answer.lower():
                    print('Correct')
                    point += 1
                else:
                    print('incorrct')
                    continue
        print(f'Here is your score: {point}')
    quit = input('Would you like to quit(y/n): ').strip().lower()
    if quit == 'y':
        print('Thank you good bye')
        break
            
                
        
