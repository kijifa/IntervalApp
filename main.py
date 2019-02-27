import common_methods as cm
import test_data as td


def main():
    #variables = td.test_input_speed()
    variables = user_input()

    print(variables)
    return


def user_input():
    print('Pro zacatek budu potrebovat par informaci \n\n')
    print('Probehlo nejake rozhybani pred intervaly?')

    warm_up_time = input('Jak dlouho trvalo? (ve formatu min:sec (napr 4:22), pokud neprobehlo zadej 0)\n')
    warm_up_time  = check_input_time(warm_up_time)

    if warm_up_time != None:
        warm_up_speed = input('A jakou rychlosti (v km/h na 2 desetinna mista pr. 5.50)\n')
        warm_up_speed = check_input_speed(warm_up_speed)
    else:
        warm_up_speed = None

    hiit_time = input('Jak dlouho trvala zatezova cast intervalu? (format min:sec)\n')
    hiit_time = check_input_time(hiit_time)

    hiit_speed = input('A jak rychle (v km/h)\n')
    hiit_speed = check_input_speed(hiit_speed)

    rest_time = input('Jak dlouho trvala odpocinkovejsi cast intervalu? (format min:sec)\n')
    rest_time = check_input_time(rest_time)

    rest_speed = input('Jakou rychlosti? (v km/h) \n')
    rest_speed = check_input_speed(rest_speed)

    cool_down_time = input('Probehlo i nejake vydychani? (ve formatu min:sec (napr 4:22), pokud neprobehlo zadej 0)\n')
    cool_down_time = check_input_time(cool_down_time)

    if cool_down_time != None:
        cool_down_speed = input('A to v rychlosti? (v km/h)\n')
        cool_down_speed = check_input_speed(cool_down_speed)
    else:
        cool_down_speed = None

    print('Ufff spousta informaci, ja vim. Tak ted snad to posledni')
    total_time = input('Jak dlouho aktivita trvala celkove? (format min:sec)\n')
    total_time = check_input_time(total_time)

    variables = {
        'warm_up_time' : warm_up_time,
        'warm_up_speed' : warm_up_speed,
        'hiit_time' : hiit_time,
        'hiit_speed' : hiit_speed,
        'rest_time' : rest_time,
        'rest_speed' : rest_speed,
        'cool_down_time' : cool_down_time,
        'cool_down_speed' : cool_down_speed,
        'total_time' : total_time
    }

    return variables


def check_input_time(time):
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


def check_input_speed(speed):
    while True:
        if speed == '':
            speed = None

        speed = cm.set_zero(speed)

        if speed != None:
            if cm.check_speed_format(speed) == False:
                print('Zda se, ze "' + speed + '" neni ve spravnem formatu "napr 8.00 km/h"')
                speed = input('Zkus to znovu: \n')
            else:
                break
        else:
            break
    return speed


if __name__ == "__main__":
    main()