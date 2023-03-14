# 뒤에서부터 처리하는 것이 이득입니다.
def solution(cap, n, deliveries, pickups):
    result = 0

    while deliveries or pickups:
        while deliveries:
            if deliveries[-1] == 0:
                deliveries.pop()

            else:
                break

        while pickups:
            if pickups[-1] == 0:
                pickups.pop()
            else:
                break

        d = len(deliveries)
        p = len(pickups)
        now = cap

        while deliveries:
            if deliveries[-1] == 0:
                deliveries.pop()

            elif deliveries[-1] <= now:
                now -= deliveries[-1]
                deliveries.pop()

            elif deliveries[-1] > now:
                deliveries[-1] -= now
                now = 0

            if now == 0:
                break

        now = cap
        while pickups:
            if pickups[-1] == 0:
                pickups.pop()

            elif pickups[-1] <= now:
                now -= pickups[-1]
                pickups.pop()

            elif pickups[-1] > now:
                pickups[-1] -= now
                now = 0

            if now == 0:
                break

        result += max(d, p) * 2

    return result
