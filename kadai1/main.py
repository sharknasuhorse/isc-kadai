
class Airplane: 
    def __init__ (self, position_x, position_y, width, hight):
        self.position_x = position_x
        self.position_y = position_y
        self.position_center_x = position_x + width / 2
        self.position_center_y = position_y + hight / 2
        self.width = width
        self.hight = hight

if __name__ == "__main__":
    x, y, width, hight = map(int,input().split())
    my_airplane = Airplane(x, y, width, hight)
    n = int(input())
    enemy_list = []

    for _ in range(n):
        x, y, width, hight = map(int,input().split())
        enemy = Airplane(x, y, width, hight)
        enemy_list.append(enemy)

    for index, enemy in enumerate(enemy_list):
        if abs(my_airplane.position_center_x - enemy.position_center_x) < my_airplane.width / 2 + enemy.width / 2 and \
            abs(my_airplane.position_center_y - enemy.position_center_y) <  my_airplane.hight/2 + enemy.hight/2 :
            print("敵機" + str(index + 1) + "が当たり")
