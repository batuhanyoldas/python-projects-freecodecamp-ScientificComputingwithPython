import copy
import random
# Consider using the modules imported above.

class Hat:
  #Initalize
  def __init__(self, **kwargs):
    self.contents = []
    for item in kwargs.items():
      for x in range(item[1]):
        self.contents.append(item[0])
  def draw(self, amount_balls):
    removed_balls =[]
    if len(self.contents) <= amount_balls:
      removed_balls = self.contents
    else:
      for x in range(amount_balls):
        removed_balls.append(self.contents.pop(random.randint(0,len(self.contents)-1)))
    return removed_balls
    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  success = 0
  for i in range(num_experiments):
    experiment_hat = copy.deepcopy(hat)
    drawn_balls = experiment_hat.draw(num_balls_drawn)
    is_color_matched = 1 
    for color in expected_balls.items():  
      if int(color[1]) > drawn_balls.count(color[0]):
        is_color_matched = 0
        break
    if is_color_matched == 1:
      success += 1
  probability = success / num_experiments
  return probability