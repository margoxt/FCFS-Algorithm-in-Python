#FCFS
#PROCESSES: [arrival_time, burst_time, person_id]
#Video Reference: https://youtu.be/TH_vRsr5Dy8?si=54iRfrYPgtMrGGn4

def fcfs(process_list):
    t = 0
    ganttChart = []
    completed = {}
    process_list.sort()
    #Keep running until all processes are finished
    while process_list != []:
        #Checking for CPU idle time
        if process_list[0][0] >= t:
            t += 1
            ganttChart.append("Idle")
            continue
        #Execute a process
        else:
            #Take the first process in the queue
            process = process_list.pop(0)
            #Appends its ID to the ganttChart
            ganttChart.append(process[2])
            #Increase burst time
            t += process[1]
            person_id = process[2]
            #cc = completion time, tt = turnaround time, wt = waiting time
            cc = t
            tt = cc - process[0]
            wt = tt - process[1]
            completed[person_id] = [cc,tt,wt]
        print(ganttChart)
        print(completed)

if __name__ == "__main__":
    process_list = [[2,6,"p1"], [5,2,"p2"],[1,8,"p3"],[0,3,"p4"], [4,4,"p5"]]
    fcfs(process_list)

