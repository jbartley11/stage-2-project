questions = {'easy':[["Python is a programming ___1___. It was created by Guido \
                    van Rossum in 1989 and was named after ___2___ Python’s Flying Circus. \
                    Programming languages allows you to create a ___3___ which in \
                    turn tells a ___4___ what to do.",
                    ['language','Monty','program','computer']],
                    ['Python is not a compiled language but an ___1___ one. This means \
                    that ever time a ___2___ is ran the python interpreter',[]]
                    ["I'm losing my ___1___ mind!",['fucking']]],
            'medium':['Python is not a compiled language but an ___1___ one. This means \
            that ever time a ___2___ is ran the Python interpreter ___3___ the code \
            and converts it into a format, ___4___ code, so the computer can follow \
            the instructions you wrote in the code',
            ['interpreted','program','interprets','byte']],
            'hard':["",
            []]}

blanks = ['___1___','___2___','___3___','___4___']

def difficulty_level():

    """prompts user for difficulty level. Will not return value until
    one of easy, medium, or hard is given."""

    dl = raw_input("Please select your level of difficulty by entering easy, medium, or hard: ")
    if dl.lower() not in ['easy','medium','hard']:
        print "You did not enter a valid level!"
        difficulty_level()
    else:
        print "You've selected {}! \n".format(dl)
        return dl

def guess_count():

    """Allows user to specify the number of incorrect guesses they
    get before losing"""

    gc_input = raw_input("Please input the number of guesses you have to get each answer correct: ")
    try:
        gc = int(gc_input)
        print "OK, you've got {} chances to answer each question!".format(gc)
        return gc
    except:
        print "You did not enter a valid number!"
        guess_count()

def find_blank(word,blanks):

    """Searches word to see if it contains any of the blank strings"""

    for b in blanks:
        if b in word:
            return b
    return None

def tries_left(guess_count):

    """displays text for how many tries are left when an incorrect answer is given"""

    if guess_count > 1:
        return "Sorry, that is the wrong answer. {} tries left!".format(gc)
    else:
        return "Sorry, that is the wrong answer. This is your last chance!"

def ask_question(question_data,guesses):

    """Asks the question to the player and keeps track of the guesses remaining"""

    q = question_data[0]
    gc = guesses
    b_count = 0
    for word in question_data[0].split():
        b = find_blank(word,blanks)
        if b != None:
            while True:
                print "\nThe question is: \n {}\n".format(q)
                b_input = raw_input("What should filled in for {}? ".format(b))
                answer_result = check_answer(b_input,question_data[1][b_count],gc)
                if answer_result:
                    q = q.replace(b,question_data[1][b_count])
                    b_count += 1
                    break
                else:
                    gc -= 1
                    print tries_left(gc)


def check_answer(given_answer,correct_answer,guess_count):

    """Checks the given answer against the correct one"""

    if given_answer.lower() == correct_answer.lower():
        return True
    else:
        if guess_count == 1:
            print "Oh no! You have lost! The answer should have been {}.".format(correct_answer)
            exit()
        else:
            return False

def take_quiz():

    """Main function that pulls everything together"""

    dl_question_list = questions[difficulty_level()]
    gc = guess_count()
    for question_data in dl_question_list:
            ask_question(question_data,gc)
    print "Congratulations you won!"

take_quiz()
