

def convert_real_to_scale(input_real, mm_to_feet):
    output = input_real * 3.28084 * mm_to_feet
    return output


def get_scale():
    global int_scale
    int_scale = 0
    while int_scale == 0:
        scale = input('How many mm to the foot: ')
        try:
            int_scale = int(scale)
        except ValueError:
            print('ERROR: Please enter a number')

    return int_scale


if __name__ == '__main__':

    scale = get_scale()

    while True:

        meters = input('Real Meters: ')

        if meters.lower() in ['q', 'quit']:
            print('Quitting')
            break

        try:
            mm = round(convert_real_to_scale(float(meters), scale), 1)
            print(f'-> {mm}mm')
        except ValueError:
            print("ERROR: Please enter a number")
