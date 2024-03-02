inp = [[0,30],[5,10],[15,20]]

inp.sort(key=lambda x: x[1])

def can_attend_meeting(inp):
    prev_end_time = 0
    for item in inp:
        if item[0] > prev_end_time:
            continue
        else:
            return False
    
    return True

print(can_attend_meeting(inp))
    
        