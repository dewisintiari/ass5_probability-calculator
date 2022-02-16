import copy
import random
# Consider using the modules imported above.

class Hat:
    # kwargs is used when a function requires an indefinite number of variables. The ** sign indicates a variable in dictionary form
    def __init__(self, **kwargs):
        self.contents = []
        self.number = 0
        for key in kwargs.keys():
            for i in range(0, kwargs.get(key)):
                self.contents.append("%s" %key)
        for value in kwargs.values():
            self.number += value

    def __str__(self):
        return str(self.contents)

    def draw(self, nbBall):
        if nbBall > self.number:
            return self.contents
        if nbBall <= self.number:
            self.taken = []
            for i in range(0, nbBall, 1):
                taken_id = random.randint(0, (len(self.contents)-1))
                self.taken.append(self.contents.pop(taken_id))
            return self.taken
        
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    exp = 0
    exp_todo = num_experiments
    success = 0
    while exp < exp_todo:
        # copy the class hat, so we do not modify the class directly
        hat2 = copy.deepcopy(hat)
        taken_list = hat2.draw(num_balls_drawn)
        # convert the list of results into dictionary of balls' colors
        taken = {i:taken_list.count(i) for i in taken_list}
        # flag is a boolean var for indicating that the balls drawn contain all the expected balls
        flag = False
        # check if all colors in expected_balls match with those of the outcome of the draw
        if (all (i in taken.keys() for i in expected_balls.keys())):
            for key, value in expected_balls.items():
                # check if the number of each color matches
                if value <= taken.get(key):
                    flag = True
                else:
                    flag = False
                    break
        # if expected_balls is a subset of taken, then the outcome satisfies the requirement
        if flag == True:
            success += 1           
        exp_todo -= 1
    probability = success / num_experiments
    return probability
    

