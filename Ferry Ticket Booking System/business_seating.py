import user_receipt

business_seating_data = []
business_seat_list = []
business_seat_list_float = []
row_in_depo = 2
seat_number = 0
business_seat_full = False
last_seat_in_list = 9
seat_position = 0


def load_business_seating_data():
    global business_seating_data
    with open('business_seating_depo.txt', 'r') as business_seating:
        line = business_seating.readlines()
        for row in line:
            business_seating_data.append(row)


def extract_business_seating_data():
    global business_seating_data, business_seat_list, row_in_depo
    for row in range(0, 2):
        for seat_availability in business_seating_data[row_in_depo]:
            if seat_availability == '0':
                business_seat_list.append(0)
            elif seat_availability == '1':
                business_seat_list.append(1)
        row_in_depo += 1
    row_in_depo -= 2


def check_seat_availability():
    global business_seat_list, business_seat_full, last_seat_in_list
    if business_seat_list[last_seat_in_list] == 1:
        business_seat_full = True


def assign_business_seat():
    global business_seat_list, seat_position, seat_number
    seat_position = 0
    for seat_availability in business_seat_list:
        if seat_availability == 0:
            business_seat_list[seat_position] = 1
            seat_number += 1
            break
        else:
            seat_position += 1
            seat_number += 1
    user_receipt.user_seat_number.append(seat_number)


def overwrite_business_seating_data():
    global business_seat_list, business_seating_data, row_in_depo, business_seat_list_float
    for row in range(0, 2):
        business_seat_list_float.append([])
    business_seat_list_float[0] = f'{business_seat_list[0]}\t{business_seat_list[1]}\t{business_seat_list[2]}\t' \
                                  f'{business_seat_list[3]}\t{business_seat_list[4]}\n'
    business_seat_list_float[1] = f'{business_seat_list[5]}\t{business_seat_list[6]}\t{business_seat_list[7]}\t' \
                                  f'{business_seat_list[8]}\t{business_seat_list[9]}\n'
    for row in range(0, 2):
        business_seating_data[row_in_depo] = business_seat_list_float[row]
        row_in_depo += 1
    row_in_depo -= 1


# critical stage, if power trips... well the data will be corrupted
def write_business_seating_data():
    with open('business_seating_depo.txt', 'w') as business_seating:
        for data in business_seating_data:
            business_seating.writelines(data)


# to prevent the next booking to be conflicted from the first one (as loading it twice will occur for second purchase)
def unload_business_seating_data():
    global business_seating_data, business_seat_list, business_seat_list_float, business_seat_full, seat_number
    business_seating_data = []
    business_seat_list = []
    business_seat_list_float = []
    business_seat_full = False
    seat_number = 0
