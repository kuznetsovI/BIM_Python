users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
kolvo=len(users)
uniq=set(users)
uniq_2=len(uniq)
sayt={
    "Общее количество": 0,
    "Уникальные посещения": 0,
}
sayt["Общее количество"]+=kolvo
sayt["Уникальные посещения"]+=uniq_2
print(sayt)