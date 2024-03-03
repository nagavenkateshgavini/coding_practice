inp = [(2,7)]

import heapq

def meeting_rooms(inp):
    inp.sort(key=lambda x: x[1])
    meeting_rooms = []
    heapq.heappush(meeting_rooms, inp[0][1])
    for item in inp[1:]:
        if item[0]  > meeting_rooms[0]:
            heapq.heappop(meeting_rooms)
        
        heapq.heappush(meeting_rooms, item[1])
        
    return len(meeting_rooms)

print(meeting_rooms(inp))