import random


def create_deck():
    # Задать локальные переменные.
    suits = ['пик','червей','крестей','бубей']
    special_values = {'туз':1, 'король':10, 'дама':10, 'валет':10}

    # Создать список всех достоинств карт.
    numbers = ['туз', 'король', 'дама', 'валет']
    for i in range(2,11):
        numbers.append(str(i))

    # Инициализировать колоду.
    deck = {}
    for suit in suits:
        for num in numbers:
            # Значения 2-10.
            if num.isnumeric():
                deck[num + ' ' + suit] = int(num)
            # Туз, король, дама или валет.
            else:
                deck[num + ' ' + suit] = special_values[num]
    return deck


def update_player_sum(player_sum, deck, card):
    if card.startswith("туз"):
        if player_sum + 11 <= 21:
            deck[card] = 11
    return player_sum + deck[card]


def main():
    deck = create_deck()
    while len(deck) != 0:
        player1_sum = 0
        player2_sum = 0
        while (player1_sum <= 21) and (player2_sum <= 21) and len(deck) != 0:
            card = random.choice(list(deck.keys()))
            player1_sum = update_player_sum(player1_sum, deck, card)
            msg = f"Игрок 1: карта - {card}, сумма очков - {player1_sum}"
            print(f"{msg:50}\t\t", end ="")
            del deck[card]

            card = random.choice(list(deck.keys()))
            player2_sum = update_player_sum(player2_sum, deck, card)
            print(f"Игрок 2: карта - {card}, сумма очков - {player2_sum}")
            del deck[card]

        if player1_sum > 21 and player2_sum > 21:
            winner = "Оба проиграли!\n"
        elif player1_sum > 21:
            winner = "Победил игрок 2!\n"
        elif player2_sum > 21:
            winner = "Победил игрок 1!\n"
        else:
            winner = "Победитель не определен, закончилась колода.\n"

        print(f"{'Розыгрыш закончен. '+winner:^100}")


if __name__ == '__main__':
    main()
