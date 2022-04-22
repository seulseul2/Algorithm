import heapq

card = [1, 5, 821, 2, 3209, 3]

heapq.heapify(card)
print(card)

max_card = []
for i in card:
    heapq.heappush(max_card, (-i, i))

print(max_card)
max_item = heapq.heappop(max_card)[1]
print(max_card)