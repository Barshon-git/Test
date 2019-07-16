class Questions:
    def __init__(self, prompt, answer):
           self.prompt= prompt
           self.answer= answer

question_prompt=[
    "What color is banana?\n(a)Red\n(b)Purple\n(c)Yellow\n\n",

    "What color is Sky?\n(a)Blue\n(b)Green\n(c)Red\n\n",

    "what color is Cheese?\n(a)Orange\n(b)Blue\n(c)Red\n\n"

]


questions =[
Questions(question_prompt[0], "c"),
Questions(question_prompt[1], "a"),
Questions(question_prompt[2], "a"),

]

def run_test(questions):
    score=0
    for questions in questions:
        answer= input(question_prompt)
        if answer==questions.answer:
            score+=1
    print("You got "+str(score)+ "/" + str(len(questions))+ " correct")

run_test(questions)








