import random 
options =('rock','paper','scissor')
running=True 
while running:
    player=None
    computer=random.choice(options)
    while player not in options:
        player=input("enter choide(rock,scissor,paper):")
    print(f"player.{player}")
    print(f"computer.{computer}")
    if player==computer:
        print('its a tie!')
    elif player=='rock' and computer =='paper':
        print("paper wins")
    elif player =='rock' and computer=='scissor':
        print('Rock wins')
    elif player =='paper' and computer=='scissor':
        print('scissor wins')
    else:
        print('you loose!')
    if not input("play again? (y/n):").lower()=='y':
        running= False
    print('thanks for playing')
    