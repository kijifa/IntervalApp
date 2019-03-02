import prettytable


def summary_input(keys, time,speed_kph,paces,distances):

    table = prettytable.PrettyTable()

    table.title = 'Input Table'
    table.field_names = ['Faze cviceni', 'Doba trvani', 'Rychlost (km/h)', 'Vzdalenost (m)', 'Tempo (min:sec/km)']

    for key in keys:
        table.add_row([key,
                       time.get(key),
                       speed_kph.get(key),
                       distances.get(key),
                       paces.get(key)
                       ])

    input_summary = print(table)

    return input_summary

def summary_output(keys, time, speed_kph, paces, distances,intervals,summary):

    table = prettytable.PrettyTable()

    table.title = 'Output Summary'
    table.field_names = ['Faze cviceni',
                         'Doba trvani (min:sec)',
                         'Prumerna rychlost (km/h)',
                         'Vzdalenost (km)'
                         ]

    table.add_row([
        'warm up',
        time.get('warm_up'),
        speed_kph.get('warm_up'),
        round(distances.get('warm_up')/1000,2)
    ])
    table.add_row([
        'cool down',
        time.get('cool_down'),
        speed_kph.get('cool_down'),
        round(distances.get('cool_down') / 1000, 2)
    ])
    table.add_row([
        'intervals',
        intervals.get('sum_time_min'),
        intervals.get('average_speed_kph'),
        round(intervals.get('sum_distance')/1000, 2)
    ])
    table.add_row([
        'Summary',
        summary.get('total_time_min'),
        summary.get('average_speed_kph'),
        round(summary.get('total_distance') / 1000, 2)
    ])


    summary_output = print(table)

    return summary_output
