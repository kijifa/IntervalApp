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


def test_input_time():
    time = {
        'warm_up': '0',
        'hiit': '1:00',
        'rest': '2:00',
        'cool_down': '10:00',
        'total': '45:00'
    }
    return time


def test_input_speed():
    speed = {
        'warm_up': '0',
        'hiit': '14.00',
        'rest': '12.00',
        'cool_down': '6.00'
    }
    return speed
