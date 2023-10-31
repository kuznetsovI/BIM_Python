list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
kolvo=len(list_players)//2
left=list_players[:kolvo]
right=list_players[kolvo:]
print(left)
print(right)
