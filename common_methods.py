import re

def calculate_paces(variables_sec):
    #warm_up_pace =

    return variables_sec

def calculate_speeds(variables_sec):
    # Average Speed
    variables_sec['total_average_speed'] = round(variables_sec.get('total_distance')/variables_sec.get('total_time'),2)

    return variables_sec


def calculate_distances(variables_sec):
    # Warm-Up
    warm_up_distance = calculate_distance(variables_sec.get('warm_up_time'),variables_sec.get('warm_up_pace'))
    variables_sec['warm_up_distance'] = warm_up_distance

    # Cool Down
    cool_down_distance = calculate_distance(variables_sec.get('cool_down_time'),variables_sec.get('cool_down_pace'))
    variables_sec['cool_down_distance'] = cool_down_distance

    # Interval Part
    variables_sec['intervals_time'] = variables_sec.get('total_time') \
                                     - variables_sec.get('warm_up_time') \
                                     - variables_sec.get('cool_down_time')

    variables_sec['number_of_interval'] = round(variables_sec.get('intervals_time')/\
                        (variables_sec.get('hiit_time')+variables_sec.get('rest_time')),0)
    variables_sec['hiit_distance_one_int'] = calculate_distance(variables_sec.get('hiit_time'),
                                                                variables_sec.get('hiit_pace'))
    variables_sec['rest_distance_one_int'] = calculate_distance(variables_sec.get('rest_time'),
                                                                variables_sec.get('rest_pace'))
    variables_sec['intervals_distance'] = variables_sec['number_of_interval'] * (variables_sec.get('hiit_distance_one_int')
                                                                                + variables_sec.get('rest_distance_one_int'))
    variables_sec['total_distance'] = variables_sec.get('warm_up_distance') \
                                        + variables_sec.get('cool_down_distance') \
                                        + variables_sec.get('intervals_distance')
    print(variables_sec)
    return variables_sec


def calculate_distance(time,pace):
    distance = time * pace
    distance = round(distance,2)
    return distance


def convert_to_sec(time):
    time_split = time.split(':')
    minutes = int(time_split[0])
    seconds = int(time_split[1])

    time_in_sec = (int(minutes)*60)+int(seconds)

    return time_in_sec


def convert_kph_to_mps(kph_speed):
    if kph_speed == 0:
        kph_speed = 0
    kph_speed = float(kph_speed)
    mps_speed = round(kph_speed/3.6,2)

    return mps_speed


def convert_to_meters_per_sec(pace):
    pace_in_sec = convert_to_sec(pace)

    if pace_in_sec == 0:
        km_per_hour = 0
    else:
        km_per_hour = 3600/pace_in_sec

    meters_per_sec = round(km_per_hour/3.6,2)

    return meters_per_sec


def check_time_format(time):
    pattern = re.compile('[0-9]{1,}:[0-9][0-9]')

    if pattern.match(time):
        result = True
    else:
        result = False

    return result


def check_speed_format(speed):
    pattern = re.compile('[0-9]{1,}[.][0-9][0-9]')

    if pattern.match(speed):
        result = True
    else:
        result = False

    return result


def set_zero(variable):
    if variable == '0':
        variable = None
    return variable