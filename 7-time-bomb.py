from collections import deque

meta = input().split()
player_count, times, k = int(meta[0]), int(meta[1]), int(meta[2])

players = deque(range(1, player_count + 1))

while k > 0:
    for _ in range(times - 1):  # Pass the bomb to the next person for * times
        players.append(players.popleft())  # Move the player from left to right

    players.popleft()  # Remove the player that has the bomb
    k -= 1

print(players[0])
