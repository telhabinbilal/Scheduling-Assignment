no_of_processes = input("Enter count of processes \n")
no_of_processes = int(no_of_processes)

PID = [0]*no_of_processes
Burst_times = [0]*no_of_processes
Arrival_times = [0]*no_of_processes
Total_time = 0


for i in range(0,no_of_processes):
	print("process No " + str(i+1))
	PID[i] = int(input("Enter Process ID \n"))
	Burst_times[i] = int(input("Enter Process's Burst time \n"))
	Arrival_times[i] = int(input("Enter Process's arrival time : \n"))

for j in range(0,no_of_processes):
	shortest_arrival_time_index = 0 

	for k in range(1,no_of_processes):
		if (Arrival_times[k] < Arrival_times[shortest_arrival_time_index]) and (Arrival_times[k] >= 0):
			shortest_arrival_time_index = int(k)
		elif Arrival_times[shortest_arrival_time_index] < 0 and Arrival_times[k] >= 0:
			shortest_arrival_time_index = int(k)
	wait_time = Total_time - Arrival_times[shortest_arrival_time_index]		
	Total_time = Total_time + Burst_times[shortest_arrival_time_index]
	Turnaround_time = Total_time - Arrival_times[shortest_burst_time_index]
	print("Process ID " + str(PID[shortest_burst_time_index]) + " Ended, Waiting Time " + str(wait_time) + " , Turnaround Time " + str(Turnaround_time))
	Arrival_times[shortest_arrival_time_index] = -1

