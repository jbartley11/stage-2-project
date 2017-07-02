questions = {'easy':["Python is a programming ___1___. It was created by Guido van Rossum in 1989 and was named after ___2___ Python's Flying Circus. Programming languages allow you to create a ___3___ which in turn tells a ___4___ what to do.",
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

    """Searches word to see if it contains any of the blank template strings

    Arguments:
        word -- string to be checked for blank matches
        blanks -- list of possible blank template strings
    Return:
        blank template string or None
    """

    for blank in blanks:
        if blank in word:
            return blank
    return None

def tries_left(guess_count):

    """displays text for how many tries are left when an incorrect answer is given

    Arguments:
        guess_count -- the number of guesses left
    Return:
        string telling user how many tries are left"""

    if guess_count > 1:
        return "Sorry, that is the wrong answer. {} tries left!".format(guess_count)
    else:
        return "Sorry, that is the wrong answer. This is your last chance!"

def ask_question(question_data,guess_count):

    """Asks the question to the player and keeps track of the guesses remaining

    Arguments:
        question_data -- list that includes string of question and list of correct answers
        guess_count -- number of guesses left before question is answered
    Return:
        if question is completed it will return fully populated question string
        otherwise it will exit out when no guesses are left
        """

    question = question_data[0]
    blank_count = 0
    processed = []
    for word in question_data[0].split():
        blank = find_blank(word,blanks)
        if blank != None and blank not in processed:
            while True:
                print "\nThe question is: \n{}\n".format(question)
                blank_input = raw_input("What should filled in for {}? ".format(blank))
                answer_result = check_answer(blank_input,question_data[1][blank_count],guess_count)
                if answer_result:
                    question = question.replace(blank,question_data[1][blank_count])
                    blank_count += 1
                    break
                else:
                    guess_count -= 1
                    print tries_left(guess_count)
            processed.append(blank)
    return "\n{}".format(question)


def check_answer(given_answer,correct_answer,guess_count):

    """Checks the given answer against the correct one, if guess_count
    is 1 then it will exit program

    Arguments:
        given_answer -- answer user has provided
        correct_answer -- correct answer from question_data
        guess_count -- number of guesses left
    Return:
        returns True if answer is correct, False if wrong with guesses remaining,
        exits if wrong and no guesses left
    """

    if given_answer.lower() == correct_answer.lower():
        return True
    else:
        if guess_count == 1:
            print "Oh no! You have lost! The answer should have been '{}'.".format(correct_answer)
            exit()
        else:
            return False

def take_quiz():

    """Function that gets called to start the quiz, gets questions from ask_difficulty_level,
    guesses from ask_guess_count, then uses ask_question to prompt user for answer_result

    Return:
        if user is correct in all answers function will congratulate them"""

    question_data = questions[ask_difficulty_level()]
    guess_count = ask_guess_count()
    print ask_question(question_data,guess_count)
    print "Congratulations you won!"

take_quiz()
