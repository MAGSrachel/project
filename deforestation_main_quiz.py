import random
from time import sleep
import threading

num_of_scores = 0

list_of_random_facts = ["We Lose Around 10 Million Hectares of Forest Every "
                        "Single Year because The world has been "
                        "chopping down 10 million hectares of trees every year "
                        "to make space to grow crops and "
                        "livestock, and to produce materials such as paper.",
                        "Beef is Responsible for 41% of Global Deforestation "
                        "because The farming industry needs to "
                        "clear substantial pasture lands for cattle "
                        "(and livestock) in order to keep up with global "
                        "demand for beef. An estimated 81,081 square miles of "
                        "forest land is lost every year for meat "
                        "production, 80% of which occurs in the Amazon. ",
                        "Deforestation Contributes about 4.8 Billion Tonnes of "
                        "Carbon Dioxide A Year One of the most "
                        "stunning deforestation facts is that forest loss "
                        "contributes nearly 5 billion tons of carbon "
                        "dioxide into the atmosphere every year, which is "
                        "equivalent to nearly 10% of annual human "
                        "emissions. NASA researchers found that accelerated "
                        "slashing and burning methods of land "
                        "clearing in Borneo, the third-largest island in the "
                        "world and home to one of the oldest "
                        "rainforests in the world, contributed to the largest "
                        "single-year global increase in carbon "
                        "emissions in two millenniums, driving Indonesia up "
                        "towards a leading source of carbon "
                        "emissions. ",
                        "Brazil and Indonesia Account for Almost Half of "
                        "Tropical Deforestation That amounts to "
                        "approximately 1.7 million hectares each year. Both "
                        "Brazil and Indonesia are home to some of "
                        "the world’s largest and biodiversity tropical forests "
                        "in the world. As the agricultural "
                        "industry continues to practice land clearing for crop "
                        "and livestock farming, the threat to "
                        "biodiversity only worsens. Studies say observed "
                        "animal populations have experienced an "
                        "average 68% decline in population numbers. In Borneo, "
                        "Indonesia, the critically endangered "
                        "orangutan lost nearly 80% of its population within "
                        "the last 50 years. ",
                        "Soy Plays a Big Role in Deforestation While most "
                        "think of soy in the form of soy milk, "
                        "tofu and other soybean products that make up a "
                        "plant-based diet, soy in fact has been mostly "
                        "used as animal feed and to support the massive demand "
                        "of meat production. Animal feed makes "
                        "up 77% of soy production, while only 19.2% goes "
                        "directly into human food products. Globally, "
                        "soy is responsible for about 12% of deforestation. ",
                        "Deforestation Has Turned the Amazon Rainforest into a"
                        "Carbon Source One of the most shocking "
                        "deforestation facts in recent years is that the "
                        "Amazon, the world’s most biologically "
                        "diverse ecosystems and important carbon sinks, is "
                        "found to emit a greater amount of carbon "
                        "dioxide than it is absorbing as a result of "
                        "deforestation, wildfires and climate change. "
                        "According to a study between 2010 and 2018, "
                        "deforestation in eastern Amazonia has led to "
                        "greater warming and moisture stress to the forest "
                        "especially during dry seasons, "
                        "making it more susceptible to wildfires. ",
                        "More Than 100 Countries Have Pledged to End "
                        "Deforestation by 2030 Despite the current state "
                        "of deforestation, there is good news. At the recent "
                        "COP26 climate conference, a UN summit "
                        "for world leaders to conduct and negotiate policy "
                        "agreements on emissions reduction and "
                        "climate change mitigation, more than 100 countries "
                        "have joined a pledge to stop and reverse "
                        "deforestation by the end of the decade. Combined, "
                        "these 100+ countries make up 85% of the "
                        "world’s forests. Some of the most notable signatories "
                        "include Brazil, Russia, Colombia, "
                        "Indonesia and the Democratic Republic of the Congo. "
                        "The pact will see $19.2 billion of "
                        "private and public funds to help combat this global "
                        "environmental problem, from restoring "
                        "degraded land and supporting indigenous communities "
                        "to mitigating wildfire damage."]

list_of_option = ['a', 'A', 'b', 'B', 'c', 'C', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I']


# this function adds facts so when people are doing the quiz, they know some things about deforestation
def random_facts():
    for i in range(1):
        random_deforestation = random.choice(list_of_random_facts)
        print("Did you know?", random_deforestation)


def what_is():
    print("What is deforestation?")
    print("~~~~~~~~~~~~~~~~~~~~~~")
    print("Deforestation is the removal of a forest or stand of trees from "
          "land that is then converted to non-forest use like buildings, etc.")


# asking the user question
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            response = "Yes"
            return response

        elif response == "no" or response == "n":
            response = "No"
            return response
        else:
            print("Please answer yes/no")


# how to play the game
def how_to_play():
    print("This is a small quiz game where you need to answer the question "
          "about deforestation")
    print()
    print("The rules:")
    print("There are 10 question you need to answer")
    print("Answer the question by using the answers listed below")
    print("There will be some words that you won't know so there will be a "
          "list where it gives the definition")


def user_time():
    while True:
        # asking the user if they want to add a timer
        time_user = input("Do you wish to do a challenge where you have a limited "
                          "time to answer the question?")
        # if user said yes
        if time_user == "yes" or time_user == "y":
            timer()
            break
        elif time_user == "no" or time_user == "n":
            print("Continue")
            main()
            break
        else:
            print("Please choose one of the option")


def what_can_user_do():
    print("What can you do to reduce deforestation?")
    suggestion = ['Use less paper, plant trees or small plants, Buy recycled '
                  'products and then recycle them again'
                  'Buy certified wood products, Support the products of companies '
                  'that are committed to reducing deforestation.']
    print("=====================")
    print('You can', suggestion)
    print("____________________")
    print('Warning')
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print('If you are under 18, make sure you asked your guardian or parent '
          'permission first before doing those')


# asking the user question
def play_again():
    while True:
        play = input("Do you wish to play the quiz again?")
        if play == "yes" or play == "y":
            print("Welcome back to the quiz")
            user_time()
            break
        elif play == "no" or play == "n":
            print("------------------------------")
            print("Thank you for playing the quiz")
            print("------------------------------")
            exit(0)
        else:
            print("Please answer the question")


# the dictionary for the quiz
questions = {'questions': 'What is the cause of deforestation?', 'question2':
    'Why is the forest important?',
             'question3': 'Why do deforestation happen?', 'question4':
                 'What are the aftermath of the effects',
             'question5': 'How to reduce deforestation?',
             'question6': 'Why should be care about deforestation?',
             'question7': 'How many years until forest is gone?',
             'question8': 'What will happen if there are no more trees?',
             'question9': 'What will happen to the animals in the forest if it '
                          'is destroyed?',
             'question10': 'What will be the future for the Earth if the '
                           'forest is gone?'}
answer = {'answers': 'a', 'answer2': 'c', 'answer3': 'b', 'answer4': 'e',
          'answer5': 'd', 'answer6': 'f', 'answer7': 'h', 'answer8': 'g',
          'answer9': 'i', 'answer10': 'j'}

# list of answers where the user will see the list of answers which they will
# answer them
list_of_answer = ["A = Human activity", "B = The reasons for deforestation "
                                        "are logging, agriculture, cattle "
                                        "ranching, overpopulation, etc.",
                  "C = The forest is a water cycle, soil, home to many animals "
                  "and the source of oxygen, water and clean water which is "
                  "what living beings need to survive. Erosion , and act as "
                  "an important buffer against climate change.",
                  "D = Plant a tree, use less paper, reuse paper or cardboard",
                  "E = The loss of trees and other vegetation can cause "
                  "climate change, desertification, soil erosion, fewer "
                  "crops, flooding, increased greenhouse gases in the "
                  "atmosphere, and a host of problems for indigenous people. ",
                  "F = They purify the air we breathe, filter the water we "
                  "drink, prevent erosion, and act as an important buffer "
                  "against climate change.",
                  "G =The absence of trees would result in significantly "
                  "HIGHER amounts of carbon dioxide in the air and LOWER "
                  "amounts of oxygen!",
                  "H = 100 years"
                  "I =  It causes habitat destruction, increased risk of "
                  "predation, reduced food availability, and much more. As a "
                  "result, some animals lose their homes, others lose food "
                  "sources – and finally, many lose their lives.",
                  "J = There would be massive extinctions of all groups of "
                  "organisms, both locally and globally"]

random.shuffle(list_of_answer)

meaning = ["erosion is the action of surface processes that removes soil, "
           "rock, or dissolved material from one "
           "location on the Earth's crust, and then transports it to another "
           "location where it is deposited",
           "Greenhouse gases (also known as GHGs) are gases in the Earth's "
           "atmosphere that trap heat. During the day, "
           "the sun shines through the atmosphere, warming the Earth's "
           "surface. At night, Earth's surface cools, "
           "releasing heat back into the air. But some of the heat is trapped "
           "by the greenhouse gases in the atmosphere."]


def question_1():
    print("``````````````")
    random_facts()
    print("@@@@@@@@@@@@@")
    # these print the list that are on the top
    print(list_of_answer)
    print(meaning)
    # this inputs the question in the dictionary with the first question
    user_question = input(questions['questions'])
    user_question = user_question.lower()
    if user_question not in list_of_option:
        print("-------------------------------")
        print("Please choose one of the option")
        return question_1()
    elif user_question == answer['answers'] or user_question == "A":
        global num_of_scores
        num_of_scores += 1
        print("********")
        print("Correct!")
    else:
        print("#########")
        print("Incorrect")
        pass


def question_2():
    print("`````````````")
    random_facts()
    print("@@@@@@@@@@@@@")
    print(list_of_answer)
    print(meaning)
    user_question = input(questions['question2'])
    user_question = user_question.lower()
    if user_question not in list_of_option:
        print("-------------------------------")
        print("Please choose one of the option")
        return question_2()
    elif user_question == answer['answer2'] or user_question == "C":
        global num_of_scores
        num_of_scores += 1
        print("********")
        print("Correct!")
    else:
        print("#########")
        print("Incorrect")
        pass


def question_3():
    print("`````````````")
    random_facts()
    print("@@@@@@@@@@@@@")
    print(list_of_answer)
    print(meaning)
    user_question = input(questions['question3'])
    user_question = user_question.lower()
    if user_question not in list_of_option:
        print("-------------------------------")
        print("Please choose one of the option")
        return question_3()
    elif user_question == answer['answer3'] or user_question == "D":
        global num_of_scores
        num_of_scores += 1
        print("********")
        print("Correct!")
    else:
        print("#########")
        print("Incorrect")
        pass


def question_4():
    print("`````````````")
    random_facts()
    print("@@@@@@@@@@@@@")
    print(list_of_answer)
    print(meaning)
    user_question = input(questions['question4'])
    user_question = user_question.lower()
    if user_question not in list_of_option:
        print("-------------------------------")
        print("Please choose one of the option")
        return question_4()
    elif user_question == answer['answer4'] or user_question == "E":
        global num_of_scores
        num_of_scores += 1
        print("********")
        print("Correct!")
    else:
        print("#########")
        print("Incorrect")
        pass


def question_5():
    print("`````````````")
    random_facts()
    print("@@@@@@@@@@@@@")
    print(list_of_answer)
    print(meaning)
    user_question = input(questions['question5'])
    user_question = user_question.lower()
    if user_question not in list_of_option:
        print("-------------------------------")
        print("Please choose one of the option")
        return question_5()
    elif user_question == answer['answer5'] or user_question == "D":
        global num_of_scores
        num_of_scores += 1
        print("********")
        print("Correct!")
    else:
        print("#########")
        print("Incorrect")
        pass


def question_6():
    print("`````````````")
    random_facts()
    print("@@@@@@@@@@@@@")
    print(list_of_answer)
    print(meaning)
    user_question = input(questions['question6'])
    user_question = user_question.lower()
    if user_question not in list_of_option:
        print("-------------------------------")
        print("Please choose one of the option")
        return question_6()
    elif user_question == answer['answer6'] or user_question == "F":
        global num_of_scores
        num_of_scores += 1
        print("********")
        print("Correct!")
    else:
        print("#########")
        print("Incorrect")
        pass


def question_7():
    print("`````````````")
    random_facts()
    print("@@@@@@@@@@@@@")
    print(list_of_answer)
    print(meaning)
    user_question = input(questions['question7'])
    user_question = user_question.lower()
    if user_question not in list_of_option:
        print("-------------------------------")
        print("Please choose one of the option")
        return question_7()
    elif user_question == answer['answer7'] or user_question == "H":
        global num_of_scores
        num_of_scores += 1
        print("********")
        print("Correct!")
    else:
        print("#########")
        print("Incorrect")
        pass


def question_8():
    print("`````````````")
    random_facts()
    print("@@@@@@@@@@@@@")
    print(list_of_answer)
    print(meaning)
    user_question = input(questions['question8'])
    user_question = user_question.lower()
    if user_question not in list_of_option:
        print("-------------------------------")
        print("Please choose one of the option")
        return question_8()
    elif user_question == answer['answer8'] or user_question == "G":
        global num_of_scores
        num_of_scores += 1
        print("********")
        print("Correct!")
    else:
        print("#########")
        print("Incorrect")
        pass


def question_9():
    print("`````````````")
    random_facts()
    print("@@@@@@@@@@@@@")
    print(list_of_answer)
    print(meaning)
    user_question = input(questions['question9'])
    user_question = user_question.lower()
    if user_question not in list_of_option:
        print("-------------------------------")
        print("Please choose one of the option")
        return question_9()
    elif user_question == answer['answer9'] or user_question == "I":
        global num_of_scores
        num_of_scores += 1
        print("********")
        print("Correct!")
    else:
        print("#########")
        print("Incorrect")
        pass


def question_10():
    print("`````````````")
    random_facts()
    print("@@@@@@@@@@@@@")
    print(list_of_answer)
    print(meaning)
    user_question = input(questions['question10'])
    user_question = user_question.lower()
    if user_question not in list_of_option:
        print("-------------------------------")
        print("Please choose one of the option")
        return question_10()
    elif user_question == answer['answer10'] or user_question == "J":
        global num_of_scores
        num_of_scores += 1
        print("********")
        print("Correct!")
    else:
        print("#########")
        print("Incorrect")
        pass


def main():
    for i in range(1, 10):
        str = f"question_{i}()"
        print(str)

        eval(str)  # call function

    print("You got {}/10".format(num_of_scores))
    what_can_user_do()
    play_again()


def timer():
    def countdown():
        global my_timer
        # this is the time that they have which is 10 seconds
        my_timer = 10

        for x in range(10):
            my_timer = my_timer - 1
            sleep(1)
        print("!!!!!!!!!!!!!!!!!!!!!!!!")
        print("You have run out of time")
        print("You got {}/10".format(num_of_scores))
        what_can_user_do()
        print("<><><><><><><><><><><>")
        print("Please enter yes or no")
        print("Again when question appear")
        play_again()

        countdown_thread = threading.Thread(target=countdown)

        countdown_thread.start()

        while my_timer > 0:
            global num_of_scores

            print("//////////////////////////////////////////")
            print("You have 10 seconds to answer the question")
            print("//////////////////////////////////////////")

            for i in range(1, 10):
                str = f"question_{i}()"
                print(str)

                eval(str)  # call function

            if my_timer == 0:
                break


# main
name_user = input("Hello user, this is a little quiz about deforestation "
                  "what is your name?")
print("☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻☺☻")
print("Hello {}".format(name_user).title())
what_is()
print("{}{}{}{}{}{}{}{}{}{}{}{}{}")
how_to_play()
print("{}{}{}{}{}{}{}{}{}{}{}{}{}")
user_time()
