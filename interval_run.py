import common_methods as cm
import test_data as td

def main():
    print('\nVitejte v jednoduche aplikaci, ktera vam spocita prumernou rychlost a vzdalenost dle zadanych hodnot.\n')

    #variables = user_input()
    variables = test_input()
    print(variables)
    variables_in_sec = {
        'warm_up_time': cm.convert_to_sec(variables.get('warm_up_time')),
        'warm_up_pace': cm.convert_to_meters_per_sec(variables.get('warm_up_time')),
        'hiit_time': cm.convert_to_sec(variables.get('hiit_time')),
        'hiit_pace': cm.convert_to_meters_per_sec(variables.get('hiit_pace')),
        'rest_time': cm.convert_to_sec(variables.get('rest_time')),
        'rest_pace': cm.convert_to_meters_per_sec(variables.get('rest_pace')),
        'cool_down_time': cm.convert_to_sec(variables.get('cool_down_time')),
        'cool_down_pace': cm.convert_to_meters_per_sec(variables.get('cool_down_pace')),
        'total_time': cm.convert_to_sec(variables.get('total_time'))
    }
    print(variables_in_sec)

    distances = cm.calculate_distances(variables_in_sec)
    speeds = cm.calculate_speeds(variables_in_sec)

    total_distance = variables_in_sec.get('total_distance')
    average_speed = variables_in_sec.get('total_average_speed')
    average_speed_km = round(average_speed * 3.6,2)
    #average_speed =
    #str_as = print(str(average_speed))

    print('Celkovy cas trvani aktivity ' + variables.get('total_time') + '\n'
          'Behem teto doby bylo urazeno ' + str(total_distance) + ' metru \n'
          'To znamena, ze pohyb probihal prumernou rychlosti ' + str(average_speed) + 'm/s \n'
          'Takze v prepoctu cca ' + str(average_speed_km) + 'km/h.'
          )

    return

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

def check_input(time):
    while True:
        if time == '':
            time = None

        time = cm.set_zero(time)

        if time != None:
            if cm.check_time_format(time) == False:
                print('Zda se, ze "' + time + '" neni ve formatu "minuty:ss"')
                time = input('Zkus to znovu: \n')
            else:
                break
        else:
            break
    return time

if __name__ == "__main__":
    main()