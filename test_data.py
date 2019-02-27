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

def test_input_speed():
    variables = {
        'warm_up_time': '5:00',
        'warm_up_speed': '8.00',
        'hiit_time': '1:00',
        'hiit_speed': '14.00',
        'rest_time': '2:00',
        'rest_speed': '10.00',
        'cool_down_time': '10:00',
        'cool_down_speed': '6.00',
        'total_time': '45:00'
    }

    return variables