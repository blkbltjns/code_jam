import sys

def print_output(case_number, delimiter, *args):
    args_joined = delimiter.join(args)
    print("Case #" + str(case_number) + ": " + args_joined)

class Activity:
    def __init__(self, ordinal, start, finish):
        self.ordinal = ordinal
        self.start = start
        self.finish = finish
        self.assigned_parent_schedule = None

    def __repr__(self):
        return str(self.ordinal) + ": " + str(self.start) + "  " + str(self.finish)

class ParentSchedule:
    def __init__(self, parent_letter):
        self.parent_letter = parent_letter
        self.minutes_occupied = [False for i in range(0, 1440)]

    def is_available_for_activity(self, activity):
        for minute in range(activity.start, activity.finish):
            if self.minutes_occupied[minute]:
                return False
        return True

    def schedule_activity(self, activity):
        for minute in range(activity.start, activity.finish):
            self.minutes_occupied[minute] = True
        activity.assigned_parent_schedule = self

def find_available_schedule(activity, parent_schedules):
    for parent_schedule in parent_schedules:
        if parent_schedule.is_available_for_activity(activity):
            return parent_schedule
    return None

def custom_sort_by_start(activities):
    minute_to_activity = [list() for x in list(range(0, 1440))]
    for activity in activities:
        minute_to_activity[activity.start].append(activity)

    toReturn = list()
    for i in range(0, len(minute_to_activity)):
        for a in minute_to_activity[i]:
            toReturn.append(a)

    return toReturn

number_of_cases = int(sys.stdin.readline())

for case_number in range(1, number_of_cases + 1):
    parent_schedules = [ParentSchedule('C'), ParentSchedule('J')]
    impossible = False
    lines_in_case = int(sys.stdin.readline())
    activities = []
    for i in range(0, lines_in_case):
        case_line_split = sys.stdin.readline().split()
        activity = Activity(i, int(case_line_split[0]), int(case_line_split[1]))
        activities.append(activity)

    activities_sorted_by_start = custom_sort_by_start(activities)

    for activity in activities_sorted_by_start:
        available_parent_schedule = find_available_schedule(activity, parent_schedules)
        if available_parent_schedule == None:
            impossible = True
        else:
            available_parent_schedule.schedule_activity(activity)            
    
    if impossible:
        print_output(case_number, '', 'IMPOSSIBLE')
    else:
        print_output(case_number, '', *[a.assigned_parent_schedule.parent_letter for a in activities])