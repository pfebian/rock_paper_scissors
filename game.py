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


print("가위 바위 보 <<하나 빼기>> 게임에 오신 것을 환영합니다!")
    
while True:
    print('--------------------')
    player_selection_list = []
    computer_selection_list = []
    for i in range(1, 2 + 1):
        print(i, "번째 수를 선택하세요.")
        print("1. 가위")
        print("2. 바위")
        print("3. 보")

        user_input = input("종료하려면 'exit' 입력)")
        
        if user_input == "exit":
            print("게임을 종료합니다.")
            break
        player_selection = get_selection_from_input(user_input)
        player_selection_list.append(player_selection)

    if user_input == "exit":
        break
    
    while len(computer_selection_list) < 2:
        computer_selection = get_random_selection()
        if computer_selection not in computer_selection_list:
            computer_selection_list.append(computer_selection)
    
    print(f"당신의 선택: {player_selection_list}")
    print(f"컴퓨터의 선택: {computer_selection_list}")
    print("최종 수를 선택하세요.")
    user_input = input()
    player_selection = player_selection_list[int(user_input) - 1]

    cnt_same = 0
    for i in range(2):
        for j in range(2):
            if player_selection_list[i] == computer_selection_list[j]:
                cnt_same += 1
                break
    # print(f'cnt_same: {cnt_same}')  # test
    if cnt_same == 2:
        if "가위" in computer_selection_list and "바위" in computer_selection_list:
            computer_selection = "바위"
        elif "바위" in computer_selection_list and "보" in computer_selection_list:
            computer_selection = "보"
        elif "보" in computer_selection_list and "가위" in computer_selection_list:
            computer_selection = "가위"
        else:
            print("에러")
    else:
        computer_selection = random.randint(0, 1)
        computer_selection = computer_selection_list[computer_selection]

    print("당신의 선택:", player_selection)
    print("컴퓨터의 선택:", computer_selection)

    result = determine_winner(player_selection, computer_selection)
    if result == -1:
        result_message = "비겼습니다."
    else:
        winner = result
        result_message = winner + "가 이겼습니다."

    print(result_message)
