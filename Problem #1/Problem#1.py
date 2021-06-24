def check_num(list_index,list_appd):
    for i in list_time:
        list_appd.append(i[list_index])
    print(*list_appd,sep='')
number ={'0': [' __ ', '|  |', '|__|'],
        '1' : ['    ', '   |', '   |'], 
        '2' : [' __ ', ' __|', '|__ '],
        '3' : [' __ ', ' __|', ' __|'],
        '4' : ['    ', '|__|', '   |'],
        '5' : [' __ ', '|__ ', ' __|'],
        '6' : [' __ ', '|__ ', '|__|'],
        '7' : [' __ ', '   |', '   |'],
        '8' : [' __ ', '|__|', '|__|'],
        '9' : [' __ ', '|__|', ' __|'],
        '.' : ['   ', ' · ', ' · ']}
time_0 = []
time_1 = []
time_2 = []
hr, min, sec = input('Input: ').split(':')
if 0 <= int(min) <= 60 and 0 <= int(sec) <= 60 and 0<= int(hr) <=99:
    list_time = [number[hr[:1]], number[hr[1:]],number['.'], number[min[:1]], number[min[1:]], number['.'], number[sec[:1]], number[sec[1:]]]
    check_num(0, time_0)
    check_num(1, time_1)
    check_num(2, time_2)
else:
    print('        ·          ·\n__  __  ·  __  __  ·  __  __')
