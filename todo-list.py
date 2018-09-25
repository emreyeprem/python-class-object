#---------------------- First Try------------------------
# priority_list = []
# task_list = []
# task_and_priority_list = []
#
# while 1==1:
#     task_title = input("Enter the task: ").lower()
#     task_priority = int(input("Type a number from 0 to 5(0: least important -> 5: highly important): "))
#     quit_program = input('Press q to quit or enter to add another task: ').lower()
#     task_list.append(task_title)
#     priority_list.append(task_priority)
#     task_and_priority_list.append("{0} : {1}".format(task_priority,task_title))
#     #print(task_and_priority_list)
#     #print(task_list)
#     final_list = sorted(task_and_priority_list, reverse = True)
#     print(final_list)
#     if quit_program == 'q':
#         break

# -----------------Second try-------------------------------

task_list = {}
priority_list = []

class Task:


    def __init__(self,name, priority):
        self.name = name
        self.priority = priority
        task_list[self.name] = self.priority
        print(task_list)


    def remove(self):

        for key in task_list:
            i = input('Enter the task to remove: ')
            if i in task_list:
                removed = task_list.pop(i)
                return removed


    def sort(self):
        sorted_list = sorted(task_list.items(), key=lambda kv: kv[1], reverse = True)

        print(sorted_list)


while 1==1:
    task = Task(input('Enter task name:'), int(input('Type a number from 0 to 5(0: least important -> 5: highly important): ')))
    if input('Press q to quit or enter to add more task: ') == 'q':
        break
# task.remove()

task.remove()
print(task_list)
task.sort()




#-------------------------------------------------
