def print_command(x):
    print('Welcome to Chula Chana!!!\nAvailable command:')
    for i in range(x):
        print('        '+str(i+1)+'.', command[i])

place_info = {'1': ['Mahamakut Building', 300],
         '2': ['Sara Phra Keaw', 50],
         '3': ['CU Sport Complex', 120],
         '4': ['Sanam Juub', 240],
         '5': ['Samyam Mitr Town', 900]}
command = ['Check in user', 'Check out user', 'Print people count', 'Add place']
checkin_info = {}

mode = int(input('Choose Mode:\n        1.Admin\n        2.User\nEnter mode: ')) #Additional Idea : มีการเลือกโหมดเพื่อที่จะเป็นแอดมินหรือผู้ใช้ 
print('\n------------------------------------------\n')
if mode in [1,2]:  
    if mode == 1: #Additional Idea: Admin mode จะมีในส่วนของการเพิ่มสถานที่ลงไป
        y = 4
        print_command(y)
    else:
        y = 3
        print_command(y)
    input_command = int(input('Please input any number: '))
    print('\n------------------------------------------\n')
    for n in range(99999):
        if input_command == 1:
            phonenumber = input('Check In\nEnter phone number: ')
            for i in place_info:
                print('        ', i+'.',place_info[i][0])
            select_place = input('Select the place: ')
            if phonenumber not in checkin_info:
                checkin_info[phonenumber] = select_place
                place_info[select_place][1] = place_info[select_place][1] - 1
                print('Checking in', phonenumber, 'into', place_info[select_place][0])
                print('\n------------------------------------------\n')
                print_command(y)
                input_command = int(input('Please input any number: '))
                print('\n------------------------------------------\n')
                continue
            else:
                if checkin_info[phonenumber] != select_place:
                    old_place = checkin_info[phonenumber]
                    place_info[old_place][1] = place_info[old_place][1] + 1
                    checkin_info[phonenumber] = select_place
                    place_info[select_place][1] = place_info[select_place][1] - 1
                    print('Checking in', phonenumber, 'into', place_info[select_place][0])
                    print('\n------------------------------------------\n')
                    print_command(y)                
                    input_command = int(input('Please input any number: '))
                    print('\n------------------------------------------\n')
                    continue
                else:
                    print('You have already check in.')
                    print('\n------------------------------------------\n')
                    print_command(y)
                    input_command = int(input('Please input any number: '))
                    print('\n------------------------------------------\n')
                    continue
        elif input_command == 2:
            phonenumber = input('Check Out\nEnter phone number: ')
            if phonenumber in checkin_info:
                place_info[checkin_info[phonenumber]][1] = place_info[checkin_info[phonenumber]][1] + 1
                print('Checking out', phonenumber)
                print('\n------------------------------------------\n')
                del checkin_info[phonenumber]
                print_command(y)
                input_command = int(input('Please input any number: '))
                print('\n------------------------------------------\n')
                continue
            else:
                print('You never check in this place')
                ('\n------------------------------------------\n')
                print_command(y)
                input_command = int(input('Please input any number: '))
                print('\n------------------------------------------\n')
                continue
        elif input_command == 3:
            print('Current Population')
            for i in range(len(place_info)):
                print('        '+str(i+1)+'.', place_info[str(i+1)][0], ':', place_info[str(i+1)][1])
            print('\n------------------------------------------\n')
            print_command(y)
            input_command = int(input('Please input any number: '))
            print('\n------------------------------------------\n')
            continue
        elif mode == 1 and input_command == 4: #Addtional Idea : ส่วนของการเพิ่มสถานที่ ซึ่งสามารถเช็คได้ว่ามีหรือยังไม่มี ถ้าไม่มีก็เพิ่ม ถ้ามีก็ไม่เปลี่ยนแปลงอะไร(มีแจ้งเตือน)
            place, no_people = input('Add place\nEnter new place:no_people : ').split(':')
            new_place = [place, int(no_people)]
            list_place = []
            for i in place_info:
                list_place.append(place_info[i][0])
            if place not in list_place:
                place_info[str(len(place_info)+1)] = new_place
                print('\nAdd',place,'complete!')
                print('\n------------------------------------------\n')
                print_command(y)
                input_command = int(input('Please input any number: '))
                print('\n------------------------------------------\n')
                continue
            else:
                print('This place already have.')
                print('\n------------------------------------------\n')
                print_command(y)
                input_command = int(input('Please input any number: '))
                print('\n------------------------------------------\n')
                continue
        elif mode == 2 and input_command == 4:
            print('This program has not this command and End of Program')
            break
        else:
            print('This program has not this command and End of Program')
            break
else:
    print('Choose again')
