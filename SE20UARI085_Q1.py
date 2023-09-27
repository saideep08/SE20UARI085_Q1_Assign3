# Given Data
process_ids = ["P1", "P2", "P3", "P4"]
arrival_times = [0, 4, 5, 6]
burst_times = [24, 3, 3, 12]
priorities = [3, 1, 4, 2]
num_processes = len(process_ids)

# Define functions to compute waiting time and turnaround time
def calculate_waiting_turnaround_time(burst_time, waiting_time, turnaround_time):
    waiting_time[0] = 0
    for i in range(1, num_processes):
        waiting_time[i] = turnaround_time[i-1] - burst_time[i-1]

def calculate_turnaround(burst_time, waiting_time, turnaround_time):
    for i in range(num_processes):
        turnaround_time[i] = burst_time[i] + waiting_time[i]

# 1. First Come First Serve (FCFS)
def fcfs_algorithm():
    waiting_time, turnaround_time = [0] * num_processes, [0] * num_processes
    total_waiting_time, total_turnaround_time = 0, 0

    # Calculate waiting time using FCFS
    for i in range(1, num_processes):
        waiting_time[i] = burst_times[i-1] + waiting_time[i-1]

    # Calculate turnaround time
    calculate_turnaround(burst_times, waiting_time, turnaround_time)

    return waiting_time, turnaround_time

# 2. Shortest Job First (SJF)
def sjf_algorithm():
    waiting_time, turnaround_time = [0] * num_processes, [0] * num_processes
    total_waiting_time, total_turnaround_time = 0, 0

    # Calculate waiting time using SJF
    for i in range(num_processes):
        waiting_time[i] = 0
        for j in range(i):
            waiting_time[i] += burst_times[j]

    # Calculate turnaround time
    calculate_turnaround(burst_times, waiting_time, turnaround_time)

    return waiting_time, turnaround_time

# 3. Priority Scheduling
def priority_algorithm():
    waiting_time, turnaround_time = [0] * num_processes, [0] * num_processes
    total_waiting_time, total_turnaround_time = 0, 0

    # Calculate waiting time using Priority Scheduling
    for i in range(1, num_processes):
        waiting_time[i] = burst_times[i-1] + waiting_time[i-1]

    # Calculate turnaround time
    calculate_turnaround(burst_times, waiting_time, turnaround_time)

    return waiting_time, turnaround_time

# 4. Round Robin Scheduling
def round_robin_algorithm(time_quantum):
    waiting_time, turnaround_time = [0] * num_processes, [0] * num_processes
    total_waiting_time, total_turnaround_time = 0, 0
    remaining_burst_time = [0] * num_processes

    for i in range(num_processes):
        remaining_burst_time[i] = burst_times[i]

    current_time = 0
    while True:
        done = True
        for i in range(num_processes):
            if remaining_burst_time[i] > 0:
                done = False

                if remaining_burst_time[i] > time_quantum:
                    current_time += time_quantum
                    remaining_burst_time[i] -= time_quantum
                else:
                    current_time += remaining_burst_time[i]
                    waiting_time[i] = current_time - burst_times[i]
                    remaining_burst_time[i] = 0

        if done:
            break

    # Calculate turnaround time
    calculate_turnaround(burst_times, waiting_time, turnaround_time)

    return waiting_time, turnaround_time

# Perform scheduling and calculate waiting times and turnaround times
fcfs_waiting_time, fcfs_turnaround_time = fcfs_algorithm()
sjf_waiting_time, sjf_turnaround_time = sjf_algorithm()
ps_waiting_time, ps_turnaround_time = priority_algorithm()
rr_waiting_time, rr_turnaround_time = round_robin_algorithm(4)

# Calculate and display average waiting time and average turnaround time for each scheduling algorithm
def compute_average(values):
    return sum(values) / num_processes

average_waiting_time_fcfs = compute_average(fcfs_waiting_time)
average_turnaround_time_fcfs = compute_average(fcfs_turnaround_time)

average_waiting_time_sjf = compute_average(sjf_waiting_time)
average_turnaround_time_sjf = compute_average(sjf_turnaround_time)

average_waiting_time_ps = compute_average(ps_waiting_time)
average_turnaround_time_ps = compute_average(ps_turnaround_time)

average_waiting_time_rr = compute_average(rr_waiting_time)
average_turnaround_time_rr = compute_average(rr_turnaround_time)

print("FCFS Algorithm:")
print("Process\t\tWT\t\tTAT")
for i in range(num_processes):
    print(f"{process_ids[i]}\t\t{fcfs_waiting_time[i]}\t\t{fcfs_turnaround_time[i]}")
print(f"Average WT: {average_waiting_time_fcfs}")
print(f"Average TAT: {average_turnaround_time_fcfs}")

print("\nSJF Algorithm:")
print("Process\t\tWT\t\tTAT")
for i in range(num_processes):
    print(f"{process_ids[i]}\t\t{sjf_waiting_time[i]}\t\t{sjf_turnaround_time[i]}")
print(f"Average WT: {average_waiting_time_sjf}")
print(f"Average TAT: {average_turnaround_time_sjf}")

print("\nPriority Algorithm:")
print("Process\t\tWT\t\tTAT")
for i in range(num_processes):
    print(f"{process_ids[i]}\t\t{ps_waiting_time[i]}\t\t{ps_turnaround_time[i]}")
print(f"Average WT: {average_waiting_time_ps}")
print(f"Average TAT: {average_turnaround_time_ps}")

print("\nRound Robin Algorithm:")
print("Process\t\tWT\t\tTAT")
for i in range(num_processes):
    print(f"{process_ids[i]}\t\t{rr_waiting_time[i]}\t\t{rr_turnaround_time[i]}")
print(f"Average WT: {average_waiting_time_rr}")
print(f"Average TAT: {average_turnaround_time_rr}")

# Determine the most suitable scheduling algorithm based on average waiting time
average_waiting_times = {
    "FCFS": average_waiting_time_fcfs,
    "SJF": average_waiting_time_sjf,
    "PS": average_waiting_time_ps,
    "RR": average_waiting_time_rr
}

most_suitable_algorithm = min(average_waiting_times, key=average_waiting_times.get)
print(f"\nMost suitable scheduling algorithm is {most_suitable_algorithm} with average waiting time of {average_waiting_times[most_suitable_algorithm]}")
