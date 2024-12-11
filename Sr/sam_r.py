import math

# task1

class Circle:   
    def __init__(self, radius):
        self.radius = radius 
    def dlina_o(self):
        return 2*math.pi*self.radius
    def s_o(self):
        return math.pi*self.radius**2
    

class Square:
    def __init__(self, side):
        self.side = side
    def perimetr(self):
        return self.side*4
    def s_s(self):
        return self.side**2

class SquaredCircle(Circle, Square):
    def __init__(self, radius):
        Circle.__init__(self, radius)
        Square.__init__(self, radius*2)

squeredcircle = SquaredCircle(10)
print(squeredcircle.perimetr())    
# krug = Circle(6)
# print(krug.dlina_o())
# print(krug.s_o())


# task2

class Engine:
    def __init__(self, power, quality):
        self.__power = power 
        self.__quality = quality
    
    def get_power(self):
        return self.__power 
    def get_quality(self):
        return self.__quality
    
    def set_power(self, new_power):
        self.__power = new_power
    
class Doors:
    def __init__(self, type, quality):
        self.__type = type 
        self.__quality = quality
    
    def get_type(self):
        return self.__type 
    def get_quality(self):
        return self.__quality
    
    def set_type(self, new_type):
        self.__type = new_type
    

class Wheels:
    def __init__(self, size, quality):
        self.__size = size 
        self.__quality = quality
    
    def get_size(self):
        return self.__size 
    def get_quality(self):
        return self.__quality
    
    def set_size(self, new_size):
        self.__size = new_size
    
class Auto:
    def __init__(self,enqine_power,engine_quality,wheels_size,wheels_quality,doors_quality,doors_type):
        self.engine = Engine(enqine_power, engine_quality)
        self.doors = Doors(doors_quality, doors_type)
        self.wheels = Wheels(wheels_quality, wheels_size)

new_auto = Auto('1000', 'премиум', 'большие', 'отличные', 'идеальные', 'открываются вверх')
print(new_auto.doors.get_quality())
new_auto.doors.set_type('открываются в сторону')
print(new_auto.doors.get_type()) 



# task3

class Animal :
    def __init__(self, sound, type, name):
        self.__sound = sound
        self.__type = type
        self.__name = name
    
    def get_sound(self):
        print(f'Это животное говорит {self.__sound}!')
    def get_name(self):
        print(f'Это животное зовут {self.__name}!')
    def get_type(self):
        print(f'Это животное типа {self.__type}!')
    
class Parrot(Animal) :
    def __init__(self, name):
        super().__init__('Чирик-чирик', 'попугай', name)
class Dog(Animal) :
    def __init__(self, name):
        super().__init__('Гав-гав', 'собака', name)
class Cat(Animal) :
    def __init__(self, name):
        super().__init__('Мяу-мяу', 'кошка', name)
class Hamster(Animal) :
    def __init__(self, name):
        super().__init__('Пи-пи', 'хомяк', name)

new_cat = Cat('Ноэль')
new_cat.get_sound()
new_dog = Dog('Хати')
new_dog.get_type()


# task4

class Employee :
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def Print(self):
        print(f'Этого сотрудника зовут {self.name} и его/ee возраст составляет {self.age}') 
    def __str__(self):
        return f'Имя этого сотрудника {self.name}, а его/ее возраст {self.age}'
    def __int__(self):
        return self.age  
    
class Manager(Employee):
    def Print(self):
        print(f'Этого менеджера зовут {self.name} и его/ee возраст составляет {self.age}')
    
class President(Employee):
    def Print(self):
        print(f'Этого директора зовут {self.name} и его/ee возраст составляет {self.age}')

class Worker(Employee):
    def Print(self):
        print(f'Этого работника зовут {self.name} и его/ee возраст составляет {self.age}')

new_worker = Worker('Наташа', 26)
new_worker.Print()
print(new_worker)
print(int(new_worker))