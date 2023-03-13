from random import *

Ascore = 0
Bscore = 0 

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
                    print('Player B Dice : ', DiceB)
                    print()
                    
                    wait = input()

                elif DiceA < DiceB :
                    print('Player A Dice : ', DiceA)
                    print('Player B Dice : ', DiceB)
                    Bscore += 1
                    print()
                    
                    wait = input()

                elif DiceA == DiceB :
                    print('Player A Dice : ', DiceA)
                    print('Player B Dice : ', DiceB)
                    Ascore += 1
                    Bscore += 1
                    
                    print()
                    
                    wait = input()


                else :
                    print('Player A Score : ', Ascore)
                    print('Player B Score : ', Bscore)
                    print()
                    
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

