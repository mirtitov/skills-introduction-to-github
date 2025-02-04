soldats=int(input('Количество солдат в шеренге: '))
rules=int(input('Количество правил: '))
push=0
for soldar in range(soldats,0,-4):
    soldarrus=int(input('Назови сколько правил' ))
    if soldarrus!=rules:
        print('Ты не прав! ',10*soldar, 'отжиманий')
        push+=10*soldar
print('общее колв отжиманий', push)
