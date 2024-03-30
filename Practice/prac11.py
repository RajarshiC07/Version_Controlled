class Adam:
    def display(self):
        print('In Adam')


class Eve:
    def display(self):
        print('In Eve')


class L1F1(Adam, Eve):
    def display(self):
        print('in L1F1')
        super().display()


class L1M1(Adam, Eve):
    def display(self):
        print('in L1M1')
        super().display()


class L1F2(Adam, Eve):
    def display(self):
        print('in L1F2')
        super().display()


class L1M2(Adam, Eve):
    def display(self):
        print('in L1M2')
        super().display()


class L2F1(L1F1, L1M1):
    def display(self):
        print('in L2F1')
        super().display()


class L2M1(L1F1, L1M1):
    def display(self):
        print('in L2M1')
        super().display()


class L2F2(L1F1, L1M1):
    def display(self):
        print('in L2F2')
        super().display()


class L2M2(L1F1, L1M1):
    def display(self):
        print('in L2M2')
        super().display()


class L2F3(L1F2, L1M2):
    def display(self):
        print('in L2F3')
        super().display()


class L2M3(L1F2, L1M2):
    def display(self):
        print('in L2M3')
        super().display()


class L2F4(L1F2, L1M2):
    def display(self):
        print('in L2F4')
        super().display()


class L2M4(L1F2, L1M2):
    def display(self):
        print('in L2M4')
        super().display()


class L3F1(L2F1, L2M1):
    def display(self):
        print('in L3F1')
        super().display()


class L3M1(L2F2, L2M2):
    def display(self):
        print('in L3M1')
        super().display()


class L3F2(L2F3, L2M3):
    def display(self):
        print('in L3F2')
        super().display()


class L3M2(L2F4, L2M4):
    def display(self):
        print('in L3M2')
        super().display()


class Father(L3F1, L3M1):
    def display(self):
        print('in Father')
        super().display()


class Mother(L3F2, L3M2):
    def display(self):
        print('in Mother')
        super().display()


class Child(Father, Mother):
    def display(self):
        print('in Child')
        super().display()


if __name__ == '__main__':
    help(Child)
    Child().display()
