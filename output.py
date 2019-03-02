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
                         'Vzdalenost (km)',
                         'Tempo (min:sec/km)'
                         ]

    table.add_row([
        'Zahrati',
        time.get('warm_up'),
        speed_kph.get('warm_up'),
        round(distances.get('warm_up')/1000,2),
        paces.get('warm_up')
    ])
    table.add_row([
        'Zklidneni',
        time.get('cool_down'),
        speed_kph.get('cool_down'),
        round(distances.get('cool_down') / 1000, 2),
        paces.get('cool_down')
    ])
    table.add_row([
        'Intervalova cast',
        intervals.get('sum_time_min'),
        intervals.get('average_speed_kph'),
        round(intervals.get('sum_distance')/1000, 2),
        intervals.get('pace')
    ])
    table.add_row([
        'Souhrn',
        summary.get('total_time_min'),
        summary.get('average_speed_kph'),
        round(summary.get('total_distance') / 1000, 2),
        summary.get('average_pace')
    ])


    summary_output = print(table)

    return summary_output
