print("welcom to our quiz.")

dict_questions = {
    
        "What is the basic unit of information in computing?" : "Bit"
    ,
    
    
        "What does CPU stand for?" : "Central Processing Unit"
    ,
    
    
        "What does URL stand for?" : "Uniform Resource Locator"
    ,
    
    
        "What does HTML stand for?" : "Hypertext Markup Language"
    ,

    
        "What does RAM stand for?" : "Random Access Memory"
    ,

    
        "What does the term “BIOS” stand for in computer systems?" : "Basic Input/Output System"
    ,

    
        "What does the term “WAN” stand for in computer networking?" : "Wide Area Network"
    ,

    
        "What does HTTP stand for?" : "Hypertext Transfer Protocol"
    ,
}

class InvalidInputError(Exception):
    pass

def user_playing() -> str:
    while True:
        playing = input("Do you want to take our test?[y/n] ")
        try:
            if playing.lower() in ['y', 'n']:
                return playing
            raise InvalidInputError()
        except InvalidInputError:
            print("You input is invalid. Please enter y or n.")
        
def start_quiz(questions:dict, playing:str) -> int: 
    if playing == "y":
        q_num = 1
        score = 0
        for question,answer in questions.items():
            while True:
                try:
                    user_input = input(f"{q_num}_{question}: ")
                    print('-' * 20)
                    if user_input.isdigit():
                        raise ValueError
                    q_num += 1
                    if user_input.title() == answer:
                        score += 1
                    break
                except ValueError:
                    print("Your input must not be a number.")

        return score

    else:
        return
    
playing = user_playing()
score = start_quiz(dict_questions, playing)
print(f"Your score is {score}")
print(f"{(score / 8) * 100} % of questions.")
