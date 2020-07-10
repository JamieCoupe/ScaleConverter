

def convert_meter_to_scale(input_meter, mm_to_foot):
    output = input_meter * 3.28084 * mm_to_foot
    return output


def convert_feet_to_scale(input_feet, mm_to_foot):

    if ' ' in str(input_feet):
        input_split = input_feet.split(' ')
        if len(input_split) < 3:
            feet_and_inches = float(parse_fraction(input_split[0])) + (float(parse_fraction(input_split[1])) / 12)
        else:
            if '/' in input_split[2]:
                feet_and_inches = float(parse_fraction(input_split[0])) + ((float(parse_fraction(input_split[1])) +
                                                                            (float(parse_fraction(input_split[2]))))
                                                                           / 12)
            else:
                print('WARNING: Last column not a fraction')
                feet_and_inches = float(parse_fraction(input_split[0])) + (float(parse_fraction(input_split[1])) / 12)

    elif ' ' not in str(input_feet):
        feet_and_inches = float(parse_fraction(input_feet))
    else:
        print('ERROR: Enter vaild options in each column')

    output = feet_and_inches * mm_to_foot

    return output


def parse_fraction(input_fraction):
    if '/' in str(input_fraction):
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

    print('Scale Converter - V0.1')

    scale = get_scale()
    input_type = input('Enter "m" for meters, "f" for foot and inches: ')

    while True:

        real_input = input('Real Distance: ')

        if real_input.lower() in ['q', 'quit']:
            print('Quitting')
            break

        try:

            if input_type in ['m', 'meters']:
                mm = round(convert_meter_to_scale(float(real_input), scale), 2)
            elif input_type in ['f', 'feet']:
                mm = round(convert_feet_to_scale(real_input, scale), 2)
            print(f'-> {mm}mm')
        except ValueError:
            print("ERROR: Please enter a number")
