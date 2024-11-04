class Horse: # класс описывающий лошадь
    x_distance = 0 # пройденный путь
    sound = 'Frrr' # звук, который издаёт лошадь

    def run(self, dx):
        Horse.x_distance += dx

class Eagle: # класс описывающий орла
    y_distance = 0 # высота полёта
    sound = 'I train, eat, sleep, and repeat' # звук, который издаёт орёл

    def fly(self, dy):
        Eagle.y_distance += dy

class Pegasus(Horse, Eagle): #класс описывающий пегаса. Наследуется от Horse и Eagle
    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self): # возвращает текущее положение пегаса в виде кортежа
        return (self.x_distance, self.y_distance)

    def voice(self):
        print(Eagle.sound)
p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()