questions = ("What is the capital of Germany?",
             "What is the capital of India?",
             "what is the capital of USA?")

options = ( ("A:Berlin" , "B:Hamburg" , "C:Munich", "D:Cologne"), 
            ("A:Mumbai", "B:Delhi", "C:Rajesthan", "D.Gujrat"), 
            ("A:New York", "B:Chicago", "C:Washington", "D:Texas"))

answers = ( "A" , "B", "C" )

guesses = []

score = 0

question_num = 0

for question in questions:
    print("------------------------")
    print(question)
    for option in options[question_num]:
        print (option)

    guess = input("Enter (A, B, C, D): ").upper()
    
    question_num += 1
print("------------------------")




