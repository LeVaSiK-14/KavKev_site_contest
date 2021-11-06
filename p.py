# Представьте робота, который умеет ходить только ВВЕРХ,ВПРАВО,ВЛЕВО,ВНИЗ
# Напишите функцию, которая принимает список из команд (e.g [up,down,left,right], 
# и вернет ответ True если после выполнения всех этих команд робот вернулся на место, False если нет

def step(arr):
    for i in arr:
        if i != 'left' and i != 'right' and i != 'down' and i != 'up':
            raise ValueError('Error: \tThe items of array is not valid!')
    str_ = ''.join(arr)
    left = str_.count('left')
    right = str_.count('right')
    down = str_.count('down')
    up = str_.count('up')
    if left == right and down == up:
        return True
    
    return False
print(step(['left', 'right', 'up', 'down', 'left', 'up', 'right', 'down']))


def step2(arr):
    left = []
    right = []
    down = []
    up = []
    for i in arr:
        if i == 'left':
            left.append(i)
        elif i == 'right':
            right.append(i)
        elif i == 'down':
            down.append(i)
        elif i == 'up':
            up.append(i)
        else:
            raise ValueError('Error: \tThe items of array is not valid!')
    if len(left) == len(right) and len(down) == len(up):
        return True
    return False
    

print(step2(['left', 'right', 'up', 'down', 'left', 'up', 'right', 'down']))

# абстракция, инкапсуляция, наследование, полиморфизм,