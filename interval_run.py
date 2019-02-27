import re

def main():
    print('\nVitejte v jednoduche aplikaci, ktera vam spocita prumernou rychlost a vzdalenost dle zadanych hodnot.\n')

    #variables = user_input()
    variables = test_input()

    variables_in_sec = {
        'warm_up_time': convert_to_sec(variables.get('warm_up_time')),
        'warm_up_pace': convert_to_meters_per_sec(variables.get('warm_up_time')),
        'hiit_time': convert_to_sec(variables.get('hiit_time')),
        'hiit_pace': convert_to_meters_per_sec(variables.get('hiit_pace')),
        'rest_time': convert_to_sec(variables.get('rest_time')),
        'rest_pace': convert_to_meters_per_sec(variables.get('rest_pace')),
        'cool_down_time': convert_to_sec(variables.get('cool_down_time')),
        'cool_down_pace': convert_to_meters_per_sec(variables.get('cool_down_pace')),
        'total_time': convert_to_sec(variables.get('total_time'))
    }
    print(variables_in_sec)

    pace = calculate(variables_in_sec)


    return

def test_input():
    variables = {
        'warm_up_time': '0:00',
        'warm_up_pace': '0:00',
        'hiit_time': '1:00',
        'hiit_pace': '4:00',
        'rest_time': '2:00',
        'rest_pace': '5:30',
        'cool_down_time': '0:00',
        'cool_down_pace': '0:00',
        'total_time': '40:00'
    }

    return variables

def user_input():
    print('Pro zacatek budu potrebovat par informaci \n\n')
    print('Probehlo nejake rozhybani pred intervaly?')

    warm_up_time = input('Jak dlouho trvalo? (ve formatu min:sec (napr 4:22), pokud neprobehlo zadej 0)\n')
    warm_up_time  = check_input(warm_up_time)

    if warm_up_time != None:
        warm_up_pace = input('A v jakem tempu? (format min:sec /km)\n')
        warm_up_pace = check_input(warm_up_pace)
    else:
        warm_up_pace = None

    hiit_time = input('Jak dlouho trvala zatezova cast intervalu? (format min:sec)\n')
    hiit_time = check_input(hiit_time)

    hiit_pace = input('A v jakem tempu? (format min:sec /km)\n')
    hiit_pace = check_input(hiit_pace)

    rest_time = input('Jak dlouho trvala odpocinkovejsi cast intervalu? (format min:sec)\n')
    rest_time = check_input(rest_time)

    rest_pace = input('V jakem tempu to bylo? (format min:sec /km) \n')
    rest_pace = check_input(rest_pace)

    cool_down_time = input('Probehlo i nejake vydychani? (ve formatu min:sec (napr 4:22), pokud neprobehlo zadej 0)')
    cool_down_time = check_input(cool_down_time)

    if cool_down_time != None:
        cool_down_pace = input('A v jakem tempu? (format min:sec /km)\n')
        cool_down_pace = check_input(cool_down_pace)
    else:
        cool_down_pace = None

    print('Ufff spousta informaci, ja vim. Tak ted snad to posledni')
    total_time = input('Jak dlouho aktivita trvala celkove? (format min:sec)\n')
    total_time = check_input(total_time)

    variables = {
        'warm_up_time' : warm_up_time,
        'warm_up_pace' : warm_up_pace,
        'hiit_time' : hiit_time,
        'hiit_pace' : hiit_pace,
        'rest_time' : rest_time,
        'rest_pace' : rest_pace,
        'cool_down_time' : cool_down_time,
        'cool_down_pace' : cool_down_pace,
        'total_time' : total_time
    }

    return variables

def calculate(variables_sec):
    # Warm-Up
    warm_up_distance = calculate_prepo(variables_sec.get('warm_up_time'),variables_sec.get('warm_up_pace'))
    variables_sec['warm_up_distance'] = warm_up_distance

    # Cool Down
    cool_down_distance = calculate_prepo(variables_sec.get('cool_down_time'),variables_sec.get('cool_down_pace'))
    variables_sec['cool_down_distance'] = cool_down_distance

    # Interval Part
    variables_sec['intervals_time'] = variables_sec.get('total_time') \
                                     - variables_sec.get('warm_up_time') \
                                     - variables_sec.get('cool_down_time')

    print(variables_sec)
    return

def calculate_prepo(time,pace):
    distance = time * pace
    return distance

def convert_to_sec(time):
    time_split = time.split(':')
    minutes = int(time_split[0])
    seconds = int(time_split[1])

    time_in_sec = (int(minutes)*60)+int(seconds)

    return time_in_sec

def convert_to_meters_per_sec(pace):
    pace_in_sec = convert_to_sec(pace)

    if pace_in_sec == 0:
        km_per_hour = 0
    else:
        km_per_hour = 3600/pace_in_sec

    meters_per_sec = round(km_per_hour/3.6,2)

    return meters_per_sec

def check_input(time):
    while True:
        if time == '':
            time = None

        time = set_zero(time)

        if time != None:
            if check_time_format(time) == False:
                print('Zda se, ze "' + time + '" neni ve formatu "minuty:ss"')
                time = input('Zkus to znovu: \n')
            else:
                break
        else:
            break
    return time

def check_time_format(time):
    pattern = re.compile('[0-9]{1,}:[0-9][0-9]')

    if pattern.match(time):
        result = True
    else:
        result = False

    return result

def set_zero(time):
    if time == '0':
        time = None
    return time

if __name__ == "__main__":
    main()