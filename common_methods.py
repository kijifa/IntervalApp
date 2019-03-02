import re


def calculate_intervals(time, speed, distance):
    intervals = {}

    intervals['distance'] = distance.get('hiit') + distance.get('rest')
    intervals['time'] = time.get('hiit') + time.get('rest')
    intervals['average_speed_mps'] = calculate_average_speed(intervals.get('distance'),intervals.get('time'))
    intervals['average_speed_kph'] = round(intervals.get('average_speed_mps')*3.6,2)
    intervals['count_intervals'] = (time.get('total') - time.get('warm_up') - time.get('cool_down'))/(intervals.get('time'))

    return intervals


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
        'total_time': '39:00'
    }

    return variables


def calculate_paces(speed):
    paces = {}
    for variable, value in speed.items():
        paces[variable] = calculate_pace(value)

    return paces


def calculate_pace(speed):
    if speed != '0':
        tmp_pace = (60/float(speed))
        pace = '{0:02.0f}:{1:02.0f}'.format(*divmod(tmp_pace * 60, 60))
    else:
        pace = '0:00'

    return pace


def calculate_average_speed(distance, time):

    average_speed = round(distance/time, 2)

    return average_speed


def calculate_distances(time, speed_mps, keys):
    distances = {}

    for key in keys:
        distance = calculate_distance(time.get(key),speed_mps.get(key))
        distances[key] = distance

    return distances


def calculate_distance(time, speed):
    distance = float(time) * float(speed)
    distance = round(distance, 2)
    return distance


def convert_to_sec(time):
    if time != '0' and time is not None:
        time_split = time.split(':')
        minutes = int(time_split[0])
        seconds = int(time_split[1])

        time_in_sec = (int(minutes)*60)+int(seconds)
    else:
        time_in_sec = 0

    return time_in_sec


def convert_kph_to_mps(kph_speed):
    if kph_speed is None:
        kph_speed = 0
    if kph_speed == '0':
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


def convert_time(time):
    time_sec = {
        'warm_up': convert_to_sec(time.get('warm_up')),
        'hiit': convert_to_sec(time.get('hiit')),
        'rest': convert_to_sec(time.get('rest')),
        'cool_down': convert_to_sec(time.get('cool_down')),
        'total': convert_to_sec(time.get('total'))
    }
    return time_sec


def convert_speed(speed):
    speed_mps = {
        'warm_up': convert_kph_to_mps(speed.get('warm_up')),
        'hiit': convert_kph_to_mps(speed.get('hiit')),
        'rest': convert_kph_to_mps(speed.get('rest')),
        'cool_down': convert_kph_to_mps(speed.get('cool_down'))
    }
    return speed_mps


def check_time_format(time):
    pattern = re.compile('[0-9]{1, }:[0-9][0-9]')

    if pattern.match(time):
        result = True
    else:
        result = False

    return result


def check_speed_format(speed):
    pattern = re.compile('[0-9]{1, }[.][0-9][0-9]')

    if pattern.match(speed):
        result = True
    else:
        result = False

    return result


def set_zero(variable):
    if variable == '0':
        variable = None
    return variable


def calculate_distances_deprecated(variables_sec):
    # Warm-Up
    warm_up_distance = calculate_distance(variables_sec.get('warm_up_time'), variables_sec.get('warm_up_pace'))
    variables_sec['warm_up_distance'] = warm_up_distance

    # Cool Down
    cool_down_distance = calculate_distance(variables_sec.get('cool_down_time'), variables_sec.get('cool_down_pace'))
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
