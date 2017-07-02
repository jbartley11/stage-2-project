questions = {'easy':["Python is a programming ___1___. It was created by Guido van Rossum in 1989 and was named after ___2___ Python's Flying Circus. Programming languages allows you to create a ___3___ which in turn tells a ___4___ what to do.",
                    ['language','Monty','program','computer']],
            'medium':['Python is not a compiled language but an ___1___ one. This means that every time a ___2___ is ran, the Python interpreter ___3___ the code and converts it into a format, ___4___ code. This conversion is what gives the ___5___ the ability to process your code.',
                    ['interpreted','program','interprets','byte','computer']],
            'hard':["Python has builtin ___1___ structures that allow you to hold a variety of information. ___2___ are a sequence of characters in between single or double ___3___. ___2___ are ___4___, which means that once they are created they cannot be changed. Lists, which represent a sequence of ___5___ separated values, can be changed so they are mutable.",
                    ['data','Strings','quotes','immutable','comma']]}

blanks = ['___1___','___2___','___3___','___4___','___5___']

def ask_difficulty_level():

    """prompts user for difficulty level. Will not return value until
    one of easy, medium, or hard is given."""

    difficulty_level = raw_input("Please select your level of difficulty by entering easy, medium, or hard: ")
    if difficulty_level.lower() not in ['easy','medium','hard']:
        print "You did not enter a valid level!"
        ask_difficulty_level()
    else:
        print "You've selected {}! \n".format(difficulty_level)
        return difficulty_level

def ask_guess_count():

    """Allows user to specify the number of incorrect guesses they
    get before losing"""

    guess_count_input = raw_input("Please input the number of guesses you have to get each answer correct: ")
    try:
        guess_count = int(guess_count_input)
        print "OK, you've got {} chances to answer each question!".format(guess_count)
        return guess_count
    except:
        print "You did not enter a valid number!"
        ask_guess_count()

def find_blank(word,blanks):

    """Searches word to see if it contains any of the blank strings"""

    for b in blanks:
        if b in word:
            return b
    return None

def tries_left(guess_count):

    """displays text for how many tries are left when an incorrect answer is given"""

    if guess_count > 1:
        return "Sorry, that is the wrong answer. {} tries left!".format(guess_count)
    else:
        return "Sorry, that is the wrong answer. This is your last chance!"

def ask_question(question_data,guesses):

    """Asks the question to the player and keeps track of the guesses remaining"""

    q = question_data[0]
    gc = guesses
    b_count = 0
    processed = []
    for word in question_data[0].split():
        b = find_blank(word,blanks)
        if b != None and b not in processed:
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
            processed.append(b)
    return "\n {}".format(q)


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

    question_data = questions[difficulty_level()]
    gc = guess_count()
    print ask_question(question_data,gc)
    print "Congratulations you won!"

take_quiz()
