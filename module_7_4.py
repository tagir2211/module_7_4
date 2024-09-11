class Team:
  def __init__(self, team_name, team_num):
    self.name = team_name
    self.num = team_num
    self.task = None
    self.time = None
  
  def __str__(self):
    return 'В команде %s %s участников' % (self.name, self.num)
    
  def __add__(self, other):
    return 'Итого в командах %s и %s участвуют %s и %s участников'  %(self.name, other.name, self.num, other.num)
  
  def tasks(self):
    if self.task != None:
      return 'Команда {} решила {} задач!'.format(self.name, self.task)
    else:
      import random
      self.task = random.randint(0, 100)
      return 'Команда {} решила {} задач!'.format(self.name, self.task)
  
  def times(self):
    import random
    if self.task == None:
      self.tasks()
      self.time = random.randint(0, 100000)/10
      return 'Команда {} выполнила {} задач за {} секунд!'.format(self.name, self.task, self.time)
    else:
      
      self.time = random.randint(0, 100000)/10
      return 'Команда {} выполнила {} задач за {} секунд!'.format(self.name, self.task, self.time)
  
  def all_task(self, other):
    if other.task == None:
      other.tasks()
    if self.task == None:
      self.tasks()
    return f'Команды {self.name} и {other.name} выполнили {self.task} и {other.task} задач.'

  def result(self, other):
    if other.task == None:
      other.tasks()
    if self.task == None:
      self.tasks()
    if self.task == other.task:
      return f'Ничья'
    elif self.task > other.task:
      challenge_result = self.name
    else:
      challenge_result = other.name
    return f'Результат битвы: победа команды {challenge_result}'

  def time_avg(self, other):
    if self.time == None:
      self.times()
    if other.time == None:
      other.times()
    return f'Сегодня командами {self.name} и {other.name} было решено {self.task + other.task} задач, в среднем за {round((self.time + other.time)/2, 2)} секунд.'

r = Team('Россия', 12)
u = Team('Украина', 15)
print(u)
print(r + u)
print(r.tasks())
print(r.times())
print(u.tasks())
print(u.times())
print(u.all_task(r))
print(r.result(u))
print(u.time_avg(r))
