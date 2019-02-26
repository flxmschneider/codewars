def race(v1, v2, g):
    ''' Tortoise A with speed v1 and lead of g, B with speed v2.
    When will Tortoise B reach Tortoise A?

    args: v1(int): speed tortoise A
          v2(int): speed tortoise B
          g(int): lead of tortoise A
    return (array): hours, minutes, seconds 
    '''

    v_diff = v2 - v1
    if v_diff <= 0:
        return None
    v_diff_per_second = v_diff/(60*60) 
    seconds_to_reach_A = g/v_diff_per_second
    
    minutes = int(seconds_to_reach_A/60)
    hours = int(minutes/60)
    minutes = int(minutes - 60* hours)

    seconds = int(seconds_to_reach_A - 60*minutes - 60*60*hours)

    return [hours, minutes, seconds]
