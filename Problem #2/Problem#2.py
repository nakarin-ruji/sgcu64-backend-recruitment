def print_command(x,command):
    print('Welcome to Chula Chana!!!\nAvailable command:')
    for i in range(x):
        print('        '+str(i+1)+'.', command[i])

place_info = {'1': ['Mahamakut Building', 300],
         '2': ['Sara Phra Keaw', 50],
         '3': ['CU Sport Complex', 120],
         '4': ['Sanam Juub', 240],
         '5': ['Samyam Mitr Town', 900]}
admin_command = ['Check in user', 'Check out user', 'Print people count', 'Add place', 'Add Admin', 'Print admin', 'End program']
user_command = ['Check in user', 'Check out user', 'Print people count', 'End program']
admin_id = ['prayut', 'pareena']
checkin_info = {}

mode = int(input('Choose Mode:\n        1.Admin\n        2.User\nEnter mode: '))
print('\n------------------------------------------\n')
if mode in [1,2]: #Additional idea: เลือกโหมดว่า Admin หรือ User
    if mode == 1: #Additional idea: โหมด Admin จะมีทั้งหมด 6หลักฟังก์ชัน มีส่วนของเพิ่มสถานที่ เพิ่มแอดมิน ดูจำนวนและชื่อแอดมิน
        name = input('Enter admin id: ')
        password = input('Enter password: ')
        if (name in admin_id) and password == '84000cells':
            y = 7
            command = admin_command
            print('\n------------------------------------------\n')
            print_command(y, command)
        else:
            print('\n------------------------------------------\n')
            print('You are not in list or Incorrect Input!')
            exit()
    else:
        y = 4 #Additional idea: โหมด User มีฟังก์ชันให้เลือก 4ฟังก์ชันหลัก
        command = user_command
        print_command(y, command)
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
                print_command(y,command)
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
                    print_command(y,command)                
                    input_command = int(input('Please input any number: '))
                    print('\n------------------------------------------\n')
                    continue
                else:
                    print('You have already check in.')
                    print('\n------------------------------------------\n')
                    print_command(y,command)
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
                print_command(y,command)
                input_command = int(input('Please input any number: '))
                print('\n------------------------------------------\n')
                continue
            else:
                print('You never check in this place')
                ('\n------------------------------------------\n')
                print_command(y,command)
                input_command = int(input('Please input any number: '))
                print('\n------------------------------------------\n')
                continue
        elif input_command == 3:
            print('Current Population')
            for i in range(len(place_info)):
                print('        '+str(i+1)+'.', place_info[str(i+1)][0], ':', place_info[str(i+1)][1])
            print('\n------------------------------------------\n')
            print_command(y,command)
            input_command = int(input('Please input any number: '))
            print('\n------------------------------------------\n')
            continue
        elif mode == 1 and input_command == 4: #Additional idea: เพิ่มจำนวนสถานที่ ซึ่งถ้ามีอยู่แล้วจะไม่เพิ่มและแจ้งเตือนให้รับรู้ว่ามีอยู่แล้ว
            place, no_people = input('Add place\nEnter new place:no_people : ').split(':')
            new_place = [place, int(no_people)]
            list_place = []
            for i in place_info:
                list_place.append(place_info[i][0])
            if place not in list_place:
                place_info[str(len(place_info)+1)] = new_place
                print('\nAdd',place,'complete!')
                print('\n------------------------------------------\n')
                print_command(y,command)
                input_command = int(input('Please input any number: '))
                print('\n------------------------------------------\n')
                continue
            else:
                print('This place already have.')
                print('\n------------------------------------------\n')
                print_command(y,command)
                input_command = int(input('Please input any number: '))
                print('\n------------------------------------------\n')
                continue
        elif mode == 1 and input_command == 5: #Additional idea: เพิ่มแอดมินโดยใช้ไอดี ถ้ามีอยู่แล้วจะแจ้งเตือนว่ามีอยู่แล้วและทำงานส่วนอื่นต่อไป
            admin_input = input('Enter admin id: ')
            if admin_input not in admin_id:
                admin_id.append(admin_input)
                print('Add', admin_input, 'complete!')
                print('\n------------------------------------------\n')
                print_command(y,command)
                input_command = int(input('Please input any number: '))
                print('\n------------------------------------------\n')
                continue
            else:
                print(admin_input, 'in list')
                print('\n------------------------------------------\n')
                print_command(y,command)
                input_command = int(input('Please input any number: '))
                print('\n------------------------------------------\n')
                continue
        elif mode == 1 and input_command ==6: #Additional idea: ดูจำนวน Admin ที่มีอยู่ในตอนนี้
            print('Admin: ')
            for i in range(len(admin_id)):
                print('    '+str(i+1)+'.', admin_id[i])
            print('\n------------------------------------------\n')
            print_command(y,command)
            input_command = int(input('Please input any number: '))
            print('\n------------------------------------------\n')
            continue
        else: 
            print('This program has not this command and End of Program')
            break
else:
    print('Choose again')
