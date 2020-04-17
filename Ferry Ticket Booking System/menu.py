# seat will be read from file
import time
import os
import reset_seating
import business_seating
import economy_seating
import view_seating
import user_receipt
confirmation_proceed = False
reset_attempt_exceed = False
ferry_id = 0
destination = ''
departure_time = ''


def main_menu():
    global reset_attempt_exceed
    print('-'*21 + ' Ticketing System ' + '-'*21)
    print('\t\t  P - to Purchase Ticket')
    print('\t\t  V - to View Seating Arrangement')
    print('\t\t  R - to reset seating (for admin)')
    print('\t\t  Q - to Quit the system')
    print('-' * 60)
    while True:
        select = input('>>> ').lower()
        if select == 'p':
            os.system('clear')
            sub_menu_purchase()
            break
        elif select == 'v':
            os.system('clear')
            sub_menu_view_seating()
            break
        elif select == 'r':
            os.system('clear')
            if reset_attempt_exceed:
                print('Exceed reset attempt!')
                print('Restart to try again...')
            else:
                sub_menu_reset_seating()
            main_menu()
            break
        elif select == 'q':
            os.system('clear')
            print('System exit in 30 seconds, thanks for using!')
            time.sleep(30)
            exit()
        else:
            print('Invalid keyword!')


def sub_menu_purchase():
    global confirmation_proceed, ferry_id, destination
    print('-' * 22 + ' Purchase Menu ' + '-' * 23)
    print('\tB - to purchase ticket for Business class')
    print('\tE - to purchase ticket for Economy class')
    print('\tM - to return to Main Menu')
    print('-' * 60)
    while True:
        select = input('>>> ').lower()
        if select == 'b':
            sub_menu_destination_selection()
            sub_menu_departure_time_selection()
            check_seating_business()
            sub_menu_seating_full()
            if not business_seating.business_seat_full:
                sub_menu_confirmation()
                if confirmation_proceed:
                    sub_menu_name()
                    print('Processing...please wait...')
                    assign_business_seating()
                    user_receipt.user_info_cache()
                    user_receipt.print_receipt()
                    print('Purchase successful!\n\n')
                else:
                    print('Purchase fail!')
                    sub_menu_purchase()
            break
        elif select == 'e':
            sub_menu_destination_selection()
            sub_menu_departure_time_selection()
            check_seating_economy()
            sub_menu_seating_full()
            if not economy_seating.economy_seat_full:
                sub_menu_confirmation()
                if confirmation_proceed:
                    sub_menu_name()
                    print('Processing...please wait...')
                    assign_economy_seating()
                    user_receipt.user_info_cache()
                    user_receipt.print_receipt()
                    print('Purchase successful!\n\n')
                else:
                    print('Purchase fail!')
                    sub_menu_purchase()
            break
        elif select == 'm':
            os.system('clear')
            main_menu()
            break
        else:
            print('Invalid Keyword!')
    business_seating.unload_business_seating_data()
    economy_seating.unload_economy_seating_data()
    ferry_id = 0
    destination = ''
    sub_menu_purchase()


def sub_menu_destination_selection():
    global ferry_id, destination
    print('-' * 23 + ' Destination ' + '-' * 24)
    print('\t\t 1 - Penang to Lankawi')
    print('\t\t 2 - Langkawi to Penang')
    print('-' * 60)
    while True:
        select = input('>>> ').lower()
        if select == '1':
            business_seating.row_in_depo = 2
            economy_seating.row_in_depo = 2
            ferry_id = 1
            destination = 'Penang to Langkawi'
            break
        elif select == '2':
            business_seating.row_in_depo = 35
            economy_seating.row_in_depo = 83
            ferry_id = 9
            destination = 'Langkawi to Penang'
            break
        else:
            print('Invalid Keyword!')


def sub_menu_departure_time_selection():
    global ferry_id, departure_time
    num = 0
    print('-' * 21 + ' Departure Times ' + '-' * 22)
    for val in range(0, 8):
        print(f'\t\t\t{val + 1} - 1{val}:00')
    print('-' * 60)
    while True:
        try:
            select = int(input('>>> '))
        except ValueError:
            pass
        if select in range(1, 9):
            break
        else:
            print('Invalid Keyword!')
    departure_time = f'1{num}:00'
    while select > 1:
        departure_time = f'1{num + 1}:00'
        business_seating.row_in_depo += 4
        economy_seating.row_in_depo += 10
        ferry_id += 1
        num += 1
        select -= 1


def sub_menu_seating_full():
    global confirmation_proceed
    if business_seating.business_seat_full:
        check_seating_economy()
        keyword_1, keyword_2 = 'Business', 'Economy'
    elif economy_seating.economy_seat_full:
        check_seating_business()
        keyword_1, keyword_2 = 'Economy', 'Business'
    if business_seating.business_seat_full and economy_seating.economy_seat_full:
        print('All seating for selected trip time is sold out!')
        print('Check back again tomorrow, sorry for the inconvenience.')
        print('Returning to purchase menu...')
    if business_seating.business_seat_full and not economy_seating.economy_seat_full or\
            economy_seating.economy_seat_full and not business_seating.business_seat_full:
        print(f'{keyword_1} class seat is full for current time!')
        print(f'Would you like to purchase {keyword_2} class ticket instead?')
        sub_menu_confirmation()
        if confirmation_proceed:
            sub_menu_name()
            if business_seating.business_seat_full:
                print('Processing...please wait...')
                assign_economy_seating()
                user_receipt.user_info_cache()
                user_receipt.print_receipt()
                print('Purchase successful!\n\n')
            elif economy_seating.economy_seat_full:
                print('Processing...please wait...')
                assign_business_seating()
                user_receipt.user_info_cache()
                user_receipt.print_receipt()
                print('Purchase successful!\n\n')
        else:
            print('Purchase fail!')


def check_seating_business():
    business_seating.load_business_seating_data()
    business_seating.extract_business_seating_data()
    business_seating.check_seat_availability()


def check_seating_economy():
    economy_seating.load_economy_seating_data()
    economy_seating.extract_economy_seating_data()
    economy_seating.check_seat_availability()


def assign_business_seating():
    business_seating.assign_business_seat()
    business_seating.overwrite_business_seating_data()
    business_seating.write_business_seating_data()
    user_receipt.user_ticket_class.append('Business')


def assign_economy_seating():
    economy_seating.assign_economy_seat()
    economy_seating.overwrite_economy_seating_data()
    economy_seating.write_economy_seating_data()
    user_receipt.user_ticket_class.append('Economy')


def sub_menu_view_seating():
    print('-' * 20 + ' View Seating Menu ' + '-' * 21)
    print('\t\t  F - to select Ferry ID')
    print('\t\t  T - to select Trip Time')
    print('\t\t  M - to return to Main Menu')
    print('-' * 60)
    while True:
        select = input('>>> ').lower()
        if select == 'f':
            print('Ferry ID ex. 001')
            while True:
                ferry_if_allowed = ['001', '002', '003', '004', '005', '006', '007', '008', '009', '010', '011', '012',\
                                    '013', '014', '015', '016']
                view_seating.ferry_id = input('Ferry ID: ')
                if view_seating.ferry_id in ferry_if_allowed:
                    view_seating.ferry_id_choice = True
                    view_seating.seat_view()
                    break
                else:
                    print('Invalid Ferry ID!')
                    print('Try again?')
                    sub_menu_confirmation()
                    if not confirmation_proceed:
                        break
            break
        elif select == 't':
            print('Time ex. 10:00')
            while True:
                time_allowed = ['10:00', '11:00', '12:00', '13:00', '14:00', '15:00', '16:00', '17:00']
                view_seating.time = input('Time: ')
                if view_seating.time in time_allowed:
                    view_seating.destination_selection()
                    view_seating.seat_view()
                    break
                else:
                    print('Invalid Time!')
                    print('Try again?')
                    sub_menu_confirmation()
                    if not confirmation_proceed:
                        break
            break
        elif select == 'm':
            os.system('clear')
            main_menu()
            break
        else:
            print('Invalid Keyword!')
    sub_menu_view_seating()


def sub_menu_confirmation():
    global confirmation_proceed
    print('-' * 25 + ' Proceed? ' + '-' * 25)
    print('\t\t\t  Y - Yes')
    print('\t\t\t  N - No')
    print('-' * 60)
    while True:
        select = input('>>> ').lower()
        if select == 'y':
            confirmation_proceed = True
            break
        elif select == 'n':
            confirmation_proceed = False
            break
        else:
            print('Invalid keyword!')


def sub_menu_name():
    characters_allow = 'abcdefghijklmnopqrstuvwxyz_'
    while True:
        name_error = False
        name_input = input('Name: ')
        for characters in name_input.lower():
            if characters not in characters_allow:
                print('Please input only alphabetical name!')
                name_error = True
                break
        if name_error:
            pass
        elif len(name_input) < 3:
            print('Name cannot be less than 3 characters!')
        elif len(name_input) > 15:
            print('Name cannot exceed 15 characters!')
        else:
            break
    user_receipt.user_name.append(name_input)


def sub_menu_reset_seating():
    global reset_attempt_exceed, confirmation_proceed
    while True:
        password = input('Password (1 attempt): ')
        if password == 'RESET_SEAT':
            sub_menu_confirmation()
            if confirmation_proceed:
                reset_seating.reset_business_seating()
                reset_seating.reset_economy_seating()
                print('All seat successfully reset...')
            else:
                print('Reset fail!')
        else:
            print('Invalid Password... returning to main menu...')
            reset_attempt_exceed = True
        break
