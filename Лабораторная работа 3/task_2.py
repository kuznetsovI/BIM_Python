def find_common_participants(group_1, group_2, gg=','):
    p_1 = group_1.split(gg)
    p_2 = group_2.split(gg)
    spisok= list(set(p_1).intersection(p_2))
    spisok.sort()
    return spisok
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
itog= find_common_participants(participants_first_group, participants_second_group, gg=' ')
print(itog)
# TODO Провеьте работу функции с разделителем отличным от запятой
