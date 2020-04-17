import economy_seating
import business_seating
ferry_id = ''
time = ''
departure, arrival = '', ''
business_seat_start, business_seat_end = 0, 0
economy_seat_start, economy_seat_end = 0, 0
ferry_id_choice = False


def destination_selection():
    global departure, arrival
    while True:
        print('1 - Penang to Langkawi')
        print('2 - Langakawi to Penang')
        select = input('>>> ')
        if select == '1':
            departure, arrival = 'Penang', 'Langkawi'
            break
        elif select == '2':
            departure, arrival = 'Langkawi', 'Penang'
            break
        else:
            print('Invalid Keyword!')


def seat_view():
    global ferry_id, time, business_seat_start, business_seat_end, economy_seat_start, economy_seat_end, departure,\
        ferry_id_choice, departure, arrival
    if departure == 'Penang' or ferry_id_choice:
        if ferry_id == '001' or time == '10:00':
            business_seat_start, business_seat_end = 1, 4
            economy_seat_start, economy_seat_end = 1, 10
            departure, arrival = 'Penang', 'Langkawi'
        elif ferry_id == '002' or time == '11:00':
            business_seat_start, business_seat_end = 5, 8
            economy_seat_start, economy_seat_end = 11, 20
            departure, arrival = 'Penang', 'Langkawi'
        elif ferry_id == '003' or time == '12:00':
            business_seat_start, business_seat_end = 9, 12
            economy_seat_start, economy_seat_end = 21, 30
            departure, arrival = 'Penang', 'Langkawi'
        elif ferry_id == '004' or time == '13:00':
            business_seat_start, business_seat_end = 13, 16
            economy_seat_start, economy_seat_end = 31, 40
            departure, arrival = 'Penang', 'Langkawi'
        elif ferry_id == '005' or time == '14:00':
            business_seat_start, business_seat_end = 17, 20
            economy_seat_start, economy_seat_end = 41, 50
            departure, arrival = 'Penang', 'Langkawi'
        elif ferry_id == '006' or time == '15:00':
            business_seat_start, business_seat_end = 21, 24
            economy_seat_start, economy_seat_end = 51, 60
            departure, arrival = 'Penang', 'Langkawi'
        elif ferry_id == '007' or time == '16:00':
            business_seat_start, business_seat_end = 25, 28
            economy_seat_start, economy_seat_end = 61, 70
            departure, arrival = 'Penang', 'Langkawi'
        elif ferry_id == '008' or time == '17:00':
            business_seat_start, business_seat_end = 29, 32
            economy_seat_start, economy_seat_end = 71, 80
            departure, arrival = 'Penang', 'Langkawi'

    if departure == 'Langkawi' or ferry_id_choice:
        if ferry_id == '009' or time == '10:00':
            business_seat_start, business_seat_end = 34, 37
            economy_seat_start, economy_seat_end = 82, 91
            departure, arrival = 'Langkawi', 'Penang'
        elif ferry_id == '010' or time == '11:00':
            business_seat_start, business_seat_end = 38, 41
            economy_seat_start, economy_seat_end = 92, 101
            departure, arrival = 'Langkawi', 'Penang'
        elif ferry_id == '011' or time == '12:00':
            business_seat_start, business_seat_end = 42, 45
            economy_seat_start, economy_seat_end = 102, 111
            departure, arrival = 'Langkawi', 'Penang'
        elif ferry_id == '012' or time == '13:00':
            business_seat_start, business_seat_end = 46, 49
            economy_seat_start, economy_seat_end = 112, 121
            departure, arrival = 'Langkawi', 'Penang'
        elif ferry_id == '013' or time == '14:00':
            business_seat_start, business_seat_end = 50, 53
            economy_seat_start, economy_seat_end = 122, 131
            departure, arrival = 'Langkawi', 'Penang'
        elif ferry_id == '014' or time == '15:00':
            business_seat_start, business_seat_end = 54, 57
            economy_seat_start, economy_seat_end = 132, 141
            departure, arrival = 'Langkawi', 'Penang'
        elif ferry_id == '015' or time == '16:00':
            business_seat_start, business_seat_end = 58, 61
            economy_seat_start, economy_seat_end = 142, 151
            departure, arrival = 'Langkawi', 'Penang'
        elif ferry_id == '016' or time == '17:00':
            business_seat_start, business_seat_end = 62, 65
            economy_seat_start, economy_seat_end = 152, 161
            departure, arrival = 'Langkawi', 'Penang'

    print('*' * 38)
    print(f'Destination: {departure} to {arrival}')
    print('*** Business Class ***')
    business_seating.load_business_seating_data()
    for lines in business_seating.business_seating_data[business_seat_start:business_seat_end]:
        print('|\t' + lines.rstrip())
    business_seating.unload_business_seating_data()
    print('-' * 38)
    print('*** Economy Class ***')
    economy_seating.load_economy_seating_data()
    for lines in economy_seating.economy_seating_data[economy_seat_start:economy_seat_end]:
        print('|\t' + lines.rstrip())
    economy_seating.unload_economy_seating_data()
    print('*' * 38)
    ferry_id_choice = False
    departure, arrival = '', ''
    ferry_id = ''
    time = ''
