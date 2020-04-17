import user_receipt

economy_seating_data = []
economy_seat_list = []
economy_seat_list_float = []
row_in_depo = 2
seat_number = 0
economy_seat_full = False
last_seat_in_list = 39
seat_position = 0


def load_economy_seating_data():
    global economy_seating_data
    with open('economy_seating_depo.txt', 'r') as economy_seating:
        line = economy_seating.readlines()
        for row in line:
            economy_seating_data.append(row)


def extract_economy_seating_data():
    global economy_seating_data, economy_seat_list, row_in_depo
    for row in range(0, 8):
        for seat_availability in economy_seating_data[row_in_depo]:
            if seat_availability == '0':
                economy_seat_list.append(0)
            elif seat_availability == '1':
                economy_seat_list.append(1)
        row_in_depo += 1
    row_in_depo -= 8


def check_seat_availability():
    global economy_seat_list, economy_seat_full, last_seat_in_list
    if economy_seat_list[last_seat_in_list] == 1:
        economy_seat_full = True


def assign_economy_seat():
    global economy_seat_list, seat_number, seat_position
    seat_position = 0
    for seat_availability in economy_seat_list:
        if seat_availability == 0:
            economy_seat_list[seat_position] = 1
            seat_number += 1
            break
        else:
            seat_position += 1
            seat_number += 1
    user_receipt.user_seat_number.append(seat_number)


# hard coded, need to be improvised, too wet
def overwrite_economy_seating_data():
    global economy_seat_list, economy_seating_data, row_in_depo, economy_seat_list_float
    for row in range(0, 8):
        economy_seat_list_float.append([])
    economy_seat_list_float[0] = f'{economy_seat_list[0]}\t{economy_seat_list[1]}\t{economy_seat_list[2]}\t' \
                                 f'{economy_seat_list[3]}\t{economy_seat_list[4]}\n'
    economy_seat_list_float[1] = f'{economy_seat_list[5]}\t{economy_seat_list[6]}\t{economy_seat_list[7]}\t' \
                                 f'{economy_seat_list[8]}\t{economy_seat_list[9]}\n'
    economy_seat_list_float[2] = f'{economy_seat_list[10]}\t{economy_seat_list[11]}\t{economy_seat_list[12]}\t' \
                                 f'{economy_seat_list[13]}\t{economy_seat_list[14]}\n'
    economy_seat_list_float[3] = f'{economy_seat_list[15]}\t{economy_seat_list[16]}\t{economy_seat_list[17]}\t' \
                                 f'{economy_seat_list[18]}\t{economy_seat_list[19]}\n'
    economy_seat_list_float[4] = f'{economy_seat_list[20]}\t{economy_seat_list[21]}\t{economy_seat_list[22]}\t' \
                                 f'{economy_seat_list[23]}\t{economy_seat_list[25]}\n'
    economy_seat_list_float[5] = f'{economy_seat_list[25]}\t{economy_seat_list[26]}\t{economy_seat_list[27]}\t' \
                                 f'{economy_seat_list[28]}\t{economy_seat_list[29]}\n'
    economy_seat_list_float[6] = f'{economy_seat_list[30]}\t{economy_seat_list[31]}\t{economy_seat_list[32]}\t' \
                                 f'{economy_seat_list[33]}\t{economy_seat_list[34]}\n'
    economy_seat_list_float[7] = f'{economy_seat_list[35]}\t{economy_seat_list[36]}\t{economy_seat_list[37]}\t' \
                                 f'{economy_seat_list[38]}\t{economy_seat_list[39]}\n'
    for row in range(0, 8):
        economy_seating_data[row_in_depo] = economy_seat_list_float[row]
        row_in_depo += 1
    row_in_depo -= 8


# critical stage, if power trips... well the data will be corrupted
def write_economy_seating_data():
    with open('economy_seating_depo.txt', 'w') as economy_seating:
        for data in economy_seating_data:
            economy_seating.writelines(data)


# to prevent the next booking to be conflicted from the first one (as loading it twice will occur for second purchase)
def unload_economy_seating_data():
    global economy_seating_data, economy_seat_list, economy_seat_list_float, economy_seat_full, seat_number
    economy_seating_data = []
    economy_seat_list = []
    economy_seat_list_float = []
    economy_seat_full = False
    seat_number = 0
