class parent:
    def __init__(self) -> None:
        pass

    def vf(self):
        print ("vague function")


class child(parent):
    def vf2(self):
        print ("other vague function")

x = child()
x.vf()