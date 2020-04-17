def reset_business_seating():
    time = 10
    departure, arrival = 'Penang', 'Langkawi'
    with open('business_seating_depo.txt', 'w+') as business_seating:
        for destination in range(0, 2):
            business_seating.write(f'Destination: {departure} to {arrival}\n')
            departure, arrival = 'Langkawi', 'Penang'
            for departure_time in range(0, 8):
                business_seating.write(f'Time: {time}:00\n')
                for number_of_seat_row in range(0, 2):
                    for number_of_seat_position in range(0, 5):
                        business_seating.write('0\t')
                    business_seating.write('\n')
                business_seating.write('\n')
                time += 1
            time = 10


def reset_economy_seating():
    time = 10
    departure, arrival = 'Penang', 'Langkawi'
    with open('economy_seating_depo.txt', 'w+') as economy_seating:
        for destination in range(0, 2):
            economy_seating.write(f'Destination: {departure} to {arrival}\n')
            departure, arrival = 'Langkawi', 'Penang'
            for departure_time in range(0, 8):
                economy_seating.write(f'Time: {time}:00\n')
                for number_of_seat_row in range(0, 8):
                    for number_of_seat_position in range(0, 5):
                        economy_seating.write('0\t')
                    economy_seating.write('\n')
                economy_seating.write('\n')
                time += 1
            time = 10


if __name__ == '__main__':
    reset_business_seating()
    reset_economy_seating()