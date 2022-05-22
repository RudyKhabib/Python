class TaskManager:
    def __init__(self):
        self.dict_task = dict()

    def new_task(self, task, priority):
        if self.dict_task.get(priority) is None:
            self.dict_task[priority] = [task]
        else:
            self.dict_task[priority].append(task)

    def print(self):
        for key, value in sorted(self.dict_task.items()):
            print(key, end=' ')
            [print(';', value[i], end='') if i != 0 else print(value[i], end='') for i in range(len(value))]
            print()

    def delete(self,task, priority):
        if self.dict_task.get(priority) is None:
            print('Нельзя удалить несуществуещий элемент')
        else:
            if len(self.dict_task[priority]) > 1:
                self.dict_task[priority].pop(self.dict_task[priority].index(task))
            else:
                self.dict_task.pop(priority)
                