#dictionary, set, tuple

import collections
#deque, Counter, defaultdict
from heapq import heappop, heappush

dict = collections.defaultdict(int)
dict['one'] = 'one'
lst = []

heappush(lst, 10)
heappush(lst, 5)
heappush(lst, 6)
heappush(lst, 20)
print(lst)
print(dict)


heap = []

heappush(heap, 3)
heappush(heap, 4)
heappush(heap, 1)
heappush(heap, 5)
heappush(heap, 6)
heappush(heap, 9)
print(heap)

heappop(heap)
heappop(heap)

print(heap)



#다익스트라 알고리즘
