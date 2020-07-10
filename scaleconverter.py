

def convert_meter_to_scale(input_meter, mm_to_foot):
    output = input_meter / 3.28084 * mm_to_foot
    return output


def convert_feet_to_scale(input_feet, mm_to_foot):
    input_feet = str(input_feet)
    input_feet_split = input_feet.split(' ')
    if ' ' in input_feet and len(input_feet_split) > 1:
        parsed_feet = parse_fraction(input_feet_split[0])
        parsed_inches = parse_fraction(input_feet_split[1])

        try:
            fraction = input_feet_split[2]

            if '/' in str(fraction):
                parsed_fraction = int(fraction.split('/')[0]) / int(fraction.split('/')[1])
            else:
                parsed_fraction = 1 / int(fraction)

            feet_and_inches = int(parsed_feet) + ((int(parsed_inches) / 12) + (1 / int(parsed_fraction)))
        except IndexError:
            feet_and_inches = int(parsed_feet) + (int(parsed_inches) / 12)

    elif '/' in input_feet:
        feet_and_inches = parse_fraction(input_feet)
    else:
        feet_and_inches = int(input_feet)

    output = feet_and_inches * mm_to_foot
    return output


def parse_fraction(input_fraction):
    if '/' in input_fraction:
        decimal = int(input_fraction.split('/')[0]) / int(input_fraction.split('/')[1])
    else:
        decimal = input_fraction
    return decimal


def get_scale():
    global int_scale
    int_scale = 0
    while int_scale == 0:
        scale = input('Enter how many mm to the foot: ')
        try:
            int_scale = int(scale)
        except ValueError:
            print('ERROR: Please enter a number')

    return int_scale


if __name__ == '__main__':

    scale = get_scale()
    input_type = input('Enter "m" for meters, "f" for foot and inches: ')

    while True:

        real_input = input('Real Distance: ')

        if real_input.lower() in ['q', 'quit']:
            print('Quitting')
            break

        try:

            if input_type in ['m', 'meters']:
                mm = round(convert_meter_to_scale(float(real_input), scale), 1)
            elif input_type in ['f', 'feet']:
                mm = round(convert_feet_to_scale(real_input, scale), 1)
            print(f'-> {mm}mm')
        except ValueError:
            print("ERROR: Please enter a number")
