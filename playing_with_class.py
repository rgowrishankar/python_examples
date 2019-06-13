# can you guess the values printed in each line?


class Animal:
    count = 0

    def __init__(self):
        print("self.count %d Animal.count %d id_self_count %s id_self %s id_Animal %s id_Animal_Count %s" %
               (self.count, Animal.count, hex(id(self.count)), hex(id(self)),hex(id(Animal)), hex(id(Animal.count))))
        Animal.count = Animal.count + 1
        self.count = self.count + 1
        print("self.count %d Animal.count %d id_self_count %s id_self %s id_Animal %s id_Animal_Count %s" %
              (self.count, Animal.count, hex(id(self.count)), hex(id(self)),hex(id(Animal)), hex(id(Animal.count))))

    @classmethod
    def print_count_cls(cls):
        print("Animal.count in class method ", Animal.count)

    def print_count(self):
        print("self.count in print_count %d %s" % (self.count, hex(id(self.count))))
        print("Animal.count in print_count %d %s " % (Animal.count, hex(id(Animal.count))))
        print("self.count %d Animal.count %d id_self_count %s id_self %s id_Animal %s id_Animal_Count %s" %
              (self.count, Animal.count, hex(id(self.count)), hex(id(self)),hex(id(Animal)), hex(id(Animal.count))))


class Animal2:
    count = 0

    def __init__(self):
        print("Animal.count %d id_self %s id_Animal %s id_Animal_Count %s" %
              (Animal2.count, hex(id(self)), hex(id(Animal2)), hex(id(Animal2.count))))
        Animal2.count = Animal2.count + 1
        print("Animal.count %d id_self %s id_Animal %s id_Animal_Count %s" %
              (Animal2.count, hex(id(self)), hex(id(Animal2)), hex(id(Animal2.count))))

    @classmethod
    def print_count_cls(cls):
        print("Animal.count in class method ", Animal2.count)


def main():
    cow = Animal()
    dog = Animal()
    horse = Animal()
    dinosaur = Animal()
    Animal.print_count_cls()
    cow.print_count()
    dog.print_count()
    horse.print_count()
    dinosaur.print_count()

    man = Animal2()
    chimp = Animal2()
    orangutan = Animal2()

if __name__ == '__main__':
    main()
