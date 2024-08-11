import random
print("Let's Play Hangman!!\n")
print("You Have Only 6 Lives.So Try To Guess The Word With In 6 Attempts.Good Luck!!\n")
list_animals=["lion","giraffe","panda","elephant","bear","leopard","tiger","buffalo","snake","hyena"]
random_animals=random.choice(list_animals)
length=len(random_animals)
list_1=[]
count=1
chances=10
k=0
i=0
for i in range(length):
    list_1.append('_')
print(list_1)
while chances!=0:
     if chances==0:
         break
     if k==length:
         break    
     letter=input("\nGuess a Letter: ")
     for j in range(length):
        if random_animals[j]==letter:
            if list_1[j]=='_':
                list_1[j]=letter
                i=1
                print(list_1)
                
                k=k+1
                if count==1:
                  print("""
                    _______
                    |       |
                    |
                    |
                    |
                    |
                    |____________
                    """)
                elif count == 2:
                  print("""
                    _______
                    |       |
                    |       O
                    |
                    |
                    |
                    |_____________""")
                    
                  chances=5  
                
                elif count == 3:
                  print("""_______
                           |       |
                           |       0
                           |       |
                           |
                           |
                           |_____________""")
                  chances=4
                elif count == 4:
                  print("""_______
                           |       |
                           |       0
                           |      /|
                           |
                           |
                           |_____________""")
                  chances=3           
                elif count == 5:
                  print("""_______
                           |       |
                           |       O
                           |      /|\\
                           |
                           |
                           |_____________""")
                  chances=2         
                elif count ==6:
                  print("""_______
                           |       |
                           |       O
                           |      /|\\
                           |      /
                           |
                           |_____________""")
                  chances=1    
                elif count == 7:
                   print("""_______
                          |       |
                          |       O
                          |      /|\\
                          |      / \\
                          |
                          |_____________""")
                   chances=0       
                   print("You Loose The Game Better Luck Next Time")  
            if i == 1:
                i=0
                break
            
                
                    
     if letter not in list_1:
            count=count+1
            print(f"You Guessed {letter} That Is Not Present In The Word.so you lose a life")
            if count == 2:
                print("""_______
                         |       |
                         |       O
                         |
                         |
                         |
                         |_____________""")
                
                chances=5 
            elif count == 3:
                print("""_______
                         |       |
                         |       O
                         |       |
                         |
                         |
                         |_____________""")
                
                chances=4          
            elif count == 4:
                  print("""_______
                           |       |
                           |       0
                           |      /|
                           |
                           |
                           |_____________""")
                  
                  chances=3              
            elif count == 5:
                print("""_______
                         |       |
                         |       O
                         |      /|\\
                         |
                         |
                         |_____________""")
                chances=2         
            elif count == 6:
                print("""_______a
                      
                         |       |
                         |       O
                         |      /|\\
                         |      /
                         |
                         |_____________""")
                chances=1      
            elif count == 7:
                print("""_______
                         |       |
                         |       O
                         |      /|\\
                         |      / \\
                         |
                         |_____________""")
                chances=0
                print("You Loose The Game Better Luck Next Time")
if k==length or chances!=0:
    print("You won the match")
else:
    print("By the way, The word was " + random_animals)
    print("byyyeeeeee")    