class Activity: #Class for storing activity information
    #here "this" is used to reresent the current instance of the class
    #this is similar to "self" in python
    #this is used to access variables that belongs to the class
    #here "None" means this method doesn't return anything
    def __init__(this, name, duration) -> None: #Constructor for Activity class
        this.name = name    #name of the activity
        this.duration = duration    #duration of the activity
        this.predecessors = []  #list of predecessors of the activity
        this.successors = []    #list of successors of the activity
        this.es = 0     #earliest start time
        this.ef = 0     #earliest finish time
        this.ls = 0     #latest start time
        this.lf = 0     #latest finish time
        this.st = 0     #slack time

file_name = "CPM_input.txt"     #input file name
activities = {}     #dictionary to store activities

with open(file_name, 'r') as file:      #opening file in read mode
    for line in file:    #reading file line by line
        name, *rest = line.strip().split()  #splitting line into name and rest
        duration = int(rest[0]) #duration is the first element in rest
        
        if len(rest)==1:    #if there are no predecessors then predecessors is empty
            predecessors = []   
        else:   #else predecessors is the second element in rest
            predecessors = rest[1].split(",")   #splitting the second element by comma

        activities[name] = Activity(name, duration) #creating an instance of Activity class and storing it in activities dictionary
        activities[name].predecessors = predecessors    #setting predecessors of the activity

        for predecessor in predecessors:    #adding the activity as a successor to its predecessors
            activities[predecessor].successors.append(name) #appending the activity to the successors list of its predecessors

#Forward pass
max_earliest_finish = 0
for name, activity in activities.items():   #iterating through activities
    if not activity.predecessors:   #if there are no predecessors then es = 0 and ef = duration
        activity.ef = activity.duration
    else:                           #else es = max(ef of predecessors) and ef = es + duration
        max_earliest_start = float('-inf')
        for i in activity.predecessors: 
            predecessor_ef = activities[i].ef
            max_earliest_start = max(max_earliest_start, predecessor_ef)

        activity.es = max_earliest_start    #
        activity.ef = max_earliest_start + activity.duration    

    max_earliest_finish = max(max_earliest_finish, activity.ef) 

   #Backward pass
    for name in reversed(activities):   
        activity = activities[name]
        if not activity.successors: #if there are no successors then lf = max_earliest_finish and ls = lf - duration
            activity.lf = max_earliest_finish
            activity.ls = max_earliest_finish - activity.duration
        else:   #else lf = min(ls of successors) and ls = lf - duration
            min_latest_start = float('inf')
            for i in activity.successors:
                successor_ls = activities[i].ls
                min_latest_start = min(min_latest_start, successor_ls)
            
            activity.lf = min_latest_start
            activity.ls = min_latest_start - activity.duration

        activity.st = activity.lf - activity.ef

#Printing results
critical_path = ""
print(f"{'Activity':^8} {'ES':^4} {'EF':^4} {'LS':^4} {'LF':^4} {'ST':^4}")        
for name,activity in activities.items():
    print(f"{name:^8} {activity.es:^4} {activity.ef:^4} {activity.ls:^4} {activity.lf:^4} {activity.st:^4}")

    if activity.st == 0:
        critical_path += name + ", "

print(f"\nCritical path = {{{critical_path[:-2]}}}")