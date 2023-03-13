from random import *

Ascore = 0
Bscore = 0 
def imageA():
    if(DiceA == 1):
        print('***********')
        print('*         *')
        print('*    1    *')
        print('*         *')
        print('***********')
    elif(DiceA == 2):
        print('***********')
        print('*         *')
        print('*    2    *')
        print('*         *')
        print('***********')
    elif(DiceA == 3):
        print('***********')
        print('*         *')
        print('*    3    *')
        print('*         *')
        print('***********')
    elif(DiceA == 4):
        print('***********')
        print('*         *')
        print('*    4    *')
        print('*         *')
        print('***********')
    elif(DiceA == 5):
        print('***********')
        print('*         *')
        print('*    5    *')
        print('*         *')
        print('***********')
    elif(DiceA == 6):
        print('***********')
        print('*         *')
        print('*    6    *')
        print('*         *')
        print('***********')    
        
def imageB() :
    if (DiceB == 1):
        print('***********')
        print('*         *')
        print('*    1    *')
        print('*         *')
        print('***********') 
    if (DiceB == 2):
        print('***********')
        print('*         *')
        print('*    2    *')
        print('*         *')
        print('***********')
    if (DiceB == 3):
        print('***********')
        print('*         *')
        print('*    3    *')
        print('*         *')
        print('***********')
    if (DiceB == 4):
        print('***********')
        print('*         *')
        print('*    4    *')
        print('*         *')
        print('***********')
    if (DiceB == 5):
        print('***********')
        print('*         *')
        print('*    5    *')
        print('*         *')
        print('***********')
    if (DiceB == 6):
        print('***********')
        print('*         *')
        print('*    6    *')
        print('*         *')
        print('***********') 

while True :
    print('--------은우의 주사위 게임 시작--------')
    print('총 10번을 게임을 해 이긴 숫자가 많은 사람이 승리!')
    print('--------------게임시작(s)--------------')
    print('--------------게임종료(e)--------------')
    
    start = input('게임을 시작하고 싶으면(s) 게임 종료 하고 싶으면 (e)')
    
    if start == 's' or start == 'S':
        print('--------------게임을 시작합니다.--------------')

        for A in  range(1,11):
            DiceA = randrange(1,7)
            DiceB = randrange(1,7)
            print()
            
            if Ascore >=0 and Bscore >= 0 :
                if DiceA > DiceB :
                    Ascore += 1
                    print('Player A Dice : ', DiceA)
                    print('Player A Win')
                    imageA()
                    print('Player B Dice : ', DiceB)
                    imageB()
                    print()
                    print('Player A: ',Ascore,'Player B: ',Bscore)
                    
                    wait = input()

                elif DiceA < DiceB :
                    print('Player A Dice : ', DiceA)
                    imageA()
                    print('Player B Dice : ', DiceB)
                    print('Player B Win')
                    imageB()
                    Bscore += 1
                    print()
                    print('Player A:',Ascore,'Player B:',Bscore)
                    
                    wait = input()

                elif DiceA == DiceB :
                    print('Player A Dice : ', DiceA)
                    imageA()
                    print('Player B Dice : ', DiceB)
                    imageB()
                    Ascore += 1
                    Bscore += 1
                    
                    print()
                    print('Player A:',Ascore,'Player B:',Bscore)
                    
                    wait = input()


                else :
                    print('Player A Score : ', Ascore)
                    print('Player B Score : ', Bscore)
                    print()
                    print('Player A:',Ascore,'Player B:',Bscore)
                    
                    wait = input()

    if Ascore > 0 :
        if(Ascore > Bscore):
            print('A Player 가 승리하였습니다!')
            print('B Player 가 졌습니다 ㅠㅠ')
            print()
            
            break

        elif(Ascore < Bscore):
            print('B Player가 승리하였습니다!')
            print('A Player가 졌습니다 ㅠㅠ')
            print()
            
            break

        elif(Ascore == Bscore):
            print('비겼습니다!\n\n')
            print()
            
            break

    elif start == 'p' or start == 'P':
        print('종료되었습니다!\n\n')
        print()
    
        break
    else:
        print("잘못입력했습니다ㅠㅠ")
        print('게임이 다시 시작되었습니다!\n\n')

   
