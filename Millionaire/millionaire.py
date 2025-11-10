questions = [
    ["What is the capital of France?", "A) Berlin", "B) Madrid", "C) Paris", "D) Rome", "C"],
    ["Which planet is known as the Red Planet?", "A) Earth", "B) Mars", "C) Jupiter", "D) Venus", "B"],
    ["Who wrote 'Hamlet'?", "A) Charles Dickens", "B) William Shakespeare", "C) Mark Twain", "D) Jane Austen", "B"],
    ["What is the largest mammal?", "A) Elephant", "B) Blue Whale", "C) Giraffe", "D) Hippopotamus", "B"],
    ["Which element has the chemical symbol 'O'?", "A) Gold", "B) Oxygen", "C) Silver", "D) Iron", "B"],
    ["What is the tallest mountain in the world?", "A) K2", "B) Kangchenjunga", "C) Everest", "D) Lhotse", "C"],
    ["Who painted the Mona Lisa?", "A) Vincent Van Gogh", "B) Pablo Picasso", "C) Leonardo da Vinci", "D) Claude Monet", "C"],
    ["What is the smallest prime number?", "A) 0", "B) 1", "C) 2", "D) 3", "C"],
    ["Which ocean is the largest?", "A) Atlantic", "B) Indian", "C) Arctic", "D) Pacific", "D"],
    ["What is the chemical symbol for gold?", "A) Au", "B) Ag", "C) Fe", "D) Cu", "A"],
    ["Which country is known as the Land of the Rising Sun?", "A) China", "B) Korea", "C) Japan", "D) Vietnam", "C"],
    ["What is the largest organ in the human body?", "A) Heart", "B) Brain", "C) Liver", "D) Skin", "D"],
    ["Who invented the telephone?", "A) Thomas Edison", "B) Alexander Graham Bell", "C) Nikola Tesla", "D) George Eastman", "B"],
    ["What is the capital of Australia?", "A) Sydney", "B) Melbourne", "C) Canberra", "D) Perth", "C"]
]

prize = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000]

i = 0  
for question in questions:

    print(question[0])
    print(f" {question[1]}")
    print(f" {question[2]}")
    print(f" {question[3]}")
    print(f" {question[4]}")

    a = input("Enter your answer: ").upper()  # Convert input to uppercase
    if (question[5].upper() == a):  # Compare both in uppercase

        print("Correct answer")
        print("You have won: ", prize[i], "dollars")
        i+=1

    else : 
        print ("Incorrect")
        
    
    