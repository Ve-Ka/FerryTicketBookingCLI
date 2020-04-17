import menu
import time

user_name = []
user_ferry_id = []
user_destination = []
user_departure_time = []
user_ticket_class = []
user_seat_number = []
user_date_purchase = []
user_clock_purchase = []


def user_info_cache():
    global user_name, user_ferry_id, user_destination, user_departure_time, user_ticket_class, user_seat_number, \
        user_date_purchase, user_clock_purchase
    if menu.ferry_id < 10:
        user_ferry_id.append(f'00{menu.ferry_id}')
    else:
        user_ferry_id.append(f'0{menu.ferry_id}')
    user_destination.append(menu.destination)
    user_departure_time.append(menu.departure_time)
    local_time = time.localtime()
    date = time.strftime("%d %b %Y", local_time)
    clock = time.strftime("%H:%M:%S", local_time)
    user_date_purchase.append(date)
    user_clock_purchase.append(clock)


def print_receipt():
    global user_name, user_ferry_id, user_destination, user_departure_time, user_ticket_class, user_seat_number, \
        user_date_purchase, user_clock_purchase
    for name, ferry_id, destination, departure_time, ticket_class, seat_number, date_purchase, time_purchase in \
            zip(user_name, user_ferry_id, user_destination, user_departure_time, user_ticket_class, user_seat_number,\
                user_date_purchase, user_clock_purchase):
        print('*' * 60)
        print(f'Name:\t\t\t\t\t{name}')
        print(f'Ferry ID:\t\t\t\t{ferry_id}')
        print(f'Destination:\t\t\t{destination}')
        print(f'Departure time:\t\t\t{departure_time}')
        print(f'Ticket class:\t\t\t{ticket_class}')
        print(f'Seat Number:\t\t\t{seat_number}')
        print(f'Date purchase:\t\t\t{date_purchase}')
        print(f'Time purchase:\t\t\t{time_purchase}')
        print('*' * 60)
    write_ticket_to_txt()
    unload_user_info_cache()


def unload_user_info_cache():
    global user_name, user_ferry_id, user_destination, user_departure_time, user_ticket_class, user_seat_number, \
        user_date_purchase, user_clock_purchase
    user_name = []
    user_ferry_id = []
    user_destination = []
    user_departure_time = []
    user_ticket_class = []
    user_seat_number = []
    user_date_purchase = []
    user_clock_purchase = []


def write_ticket_to_txt():
    global user_name, user_ferry_id, user_destination, user_departure_time, user_ticket_class, user_seat_number, \
        user_date_purchase, user_clock_purchase
    with open('ticket.txt', 'a+') as ticket:
        for name, ferry_id, destination, departure_time, ticket_class, seat_number, date_purchase, time_purchase in \
                zip(user_name, user_ferry_id, user_destination, user_departure_time, user_ticket_class,\
                    user_seat_number, user_date_purchase, user_clock_purchase):
            ticket.writelines('*' * 60 + '\n')
            ticket.writelines(f'Name:\t\t\t\t\t{name}\n')
            ticket.writelines(f'Ferry ID:\t\t\t\t{ferry_id}\n')
            ticket.writelines(f'Destination:\t\t\t{destination}\n')
            ticket.writelines(f'Departure time:\t\t\t{departure_time}\n')
            ticket.writelines(f'Ticket class:\t\t\t{ticket_class}\n')
            ticket.writelines(f'Seat Number:\t\t\t{seat_number}\n')
            ticket.writelines(f'Date purchase:\t\t\t{date_purchase}\n')
            ticket.writelines(f'Time purchase:\t\t\t{time_purchase}\n')
            ticket.writelines('*' * 60 + '\n\n')
