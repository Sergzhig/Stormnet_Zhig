from  colorama import init
from colorama import Fore,Back, Style
# use colorama to make Termcolor worc on Windows too
init()

ZERO = [
    [" ", "*", "*", "*", " "],
    ["*", " ", " ", " ", "*"],
    ["*", " ", " ", " ", "*"],
    ["*", " ", " ", " ", "*"],
    ["*", " ", " ", " ", "*"],
    ["*", " ", " ", " ", "*"],
    ["*", " ", " ", " ", "*"],
    ["*", " ", " ", " ", "*"],
    ["*", " ", " ", " ", "*"],
    [" ", "*", "*", "*", " "],
]

ONE = [
    [" ", " ", "*", " ", " "],
    [" ", "*", "*", " ", " "],
    ["*", " ", "*", " ", " "],
    [" ", " ", "*", " ", " "],
    [" ", " ", "*", " ", " "],
    [" ", " ", "*", " ", " "],
    [" ", " ", "*", " ", " "],
    [" ", " ", "*", " ", " "],
    [" ", " ", "*", " ", " "],
    ["*", "*", "*", "*", "*"],
]

TWO = [
    [" ", "*", "*", "*", " "],
    ["*", " ", " ", " ", "*"],
    [" ", " ", " ", " ", "*"],
    [" ", " ", " ", " ", "*"],
    [" ", " ", " ", " ", "*"],
    [" ", " ", " ", "*", " "],
    [" ", " ", "*", " ", " "],
    [" ", "*", " ", " ", " "],
    ["*", " ", " ", " ", "*"],
    ["*", "*", "*", "*", "*"],
]


class TwoDimensionalMadness:

    def __init__(self, width, height, background=" ", mark="*", space="",color="black"):
        self.width = width
        self.height = height
        self.background = background
        self.mark = mark
        self.space = space
        self.plane = self.generate_plane()
        self.map = {
            '0': ZERO,
            '1': ONE,
            '2': TWO,
            }
        self.color=color


    def generate_plane(self):
        # Берет из self размеры и генерирует и возвращает plane заданного размера
        #plane = []
        plane = [[self.background] * self.width for i in range(self.height)]
        return plane

    def reverse_plane(self, plane=None, reflection=False):
        # реверсирует двумерное поле, если поле не передано, то берет self.plane

        if plane is None:
            plane = self.plane
        for line in plane:
            i=0
            while i<len(line):
                if line[i]==self.mark:
                    line[i]=self.background
                else:
                    line[i]=self.mark
                i+=1
        reversed_plane=plane
        if reflection:
             reversed_plane = plane[::-1]
        return reversed_plane

    def print_plane(self, reversed=False, reflect=False):
        if reversed or reflect:
            self.print_something(self.reverse_plane(reflection=reflect))
        else:
            self.print_something(self.plane)


    def set_color(self):
        if self.color=="black":
            print(Fore.BLACK)
        elif self.color=="green":
            print(Fore.GREEN)
        elif self.color == "blue":
            print(Fore.CYAN)

    def print_something(self, something):
        # выводит на экран что-то, что лежит в двумерном списке
        # к примеру ZERO или ONE
        self.set_color()
        for line in something:
            joined_line = self.space.join(line)
            print(joined_line)

    def put_mark(self, width, height):
        # ставит отметку в координату
        self.plane[height][width] = self.mark

    def string_to_plane(self, some_string):
        # врендеривает строку в плейн.
        str_line=[]

        for i in range(len(ZERO)):
            a = []
            for l in some_string:
                a += self.map[l][i]
            str_line.append(a)

        if len(str_line[0]) <= len(self.plane[0]):
            iter_i = len(str_line[0])
        else:
            iter_i = len(self.plane[0])

        if len(str_line) <= len(self.plane):
            iter_j = len(str_line)
        else:
            iter_j = len(self.plane)

        for j in range(iter_j):
            for i in range(iter_i):
                if str_line[j][i]==self.mark or self.plane[j][i] ==self.mark:
                    self.plane[j][i] = self.mark
        return self.plane




plane_object = TwoDimensionalMadness(height=15, width=20, background=" ", mark="*", space=" ",color='blue')

plane_object.put_mark(height=5, width=10)
plane_object.put_mark(height=5, width=8)
plane_object.put_mark(height=8, width=12)
plane_object.put_mark(height=8, width=6)
plane_object.put_mark(height=9, width=7)
plane_object.put_mark(height=9, width=11)
plane_object.put_mark(height=10, width=8)
plane_object.put_mark(height=10, width=10)
plane_object.put_mark(height=10, width=9)

plane_object.string_to_plane(some_string='101')

plane_object.print_plane(reversed=False,reflect=False)

