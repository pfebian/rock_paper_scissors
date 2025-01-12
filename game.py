import random

def get_selection_from_input(user_input):
    num = int(user_input)
    if num == 1:
        selection = "가위"
    elif num == 2:
        selection = "바위"
    elif num == 3:
        selection = "보"
    return selection

def get_random_selection():
    num = random.randint(0, 2)
    if num == 0:
        selection = "가위"
    elif num == 1:
        selection = "바위"
    elif num == 2:
        selection = "보"
    return selection

def determine_winner(player_selection, computer_selection):
    if player_selection == computer_selection:
        return -1
    elif (player_selection == "가위" and computer_selection == "보") or \
         (player_selection == "바위" and computer_selection == "가위") or \
         (player_selection == "보" and computer_selection == "바위"):
        return "player"
    else:
        return "computer"


print("가위 바위 보 게임에 오신 것을 환영합니다!")
    
while True:
    print('--------------------')
    print("선택하세요.")
    print("1. 가위")
    print("2. 바위")
    print("3. 보")

    user_input = input("종료하려면 'exit' 입력)")

    if user_input == "exit":
        print("게임을 종료합니다.")
        break

    player_selection = get_selection_from_input(user_input)

    
    computer_selection = get_random_selection()

    print(f"당신의 선택: {player_selection}")
    print(f"컴퓨터의 선택: {computer_selection}")

    result = determine_winner(player_selection, computer_selection)
    if result == -1:
        result_message = "비겼습니다."
    else:
        winner = result
        result_message = winner + "가 이겼습니다."

    print(result_message)