# CodeJam 2020 Qualification Round
# Nitzan Haim April 4, 2020

def find_schedule(times_lst):
    sorted_times = sorted(times_lst)
    schedule_sorted = []
    c_occupation = 0
    j_occupation = 0
    for start, end, org_idx in sorted_times:
        if start >= c_occupation:
            c_occupation = end
            schedule_sorted.append(("C", org_idx))
        elif start >= j_occupation:
            j_occupation = end
            schedule_sorted.append(("J", org_idx))
        else:
            return "IMPOSSIBLE"

    schedule_lst = sorted(schedule_sorted, key=lambda x: x[1])
    return "".join([letter for letter, idx in schedule_lst])


output = ""
test_cases = int(input())
for t in range(test_cases):
    n = int(input())  # number of tasks
    times = []
    for i in range(n):
        line = input()
        times.append(list(map(int, line.split())) + [i])

    output += "Case #" + str(t+1) + ": " + find_schedule(times) + "\n"

print(output[:-1])
