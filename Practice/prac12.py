class doughFactory:

    def get_dough(self):
        print('Getting infested dough')


class Dominos(doughFactory):

    def make_pizza(self):
        super().get_dough()
        print('Making pizza ')

class organic_Dough(doughFactory):

    def get_dough(self):
        print('getting organic dough')

class DominosOrganic(Dominos,organic_Dough):

    def make_pizza(self):
        super().get_dough()
        print('making organic pizza')


obj1 = DominosOrganic()
obj1.make_pizza()
print(help(obj1))