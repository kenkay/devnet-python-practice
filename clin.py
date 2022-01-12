class colorPicker:
    def __init__(self, color, texture):
        self.color = color
        self.texture = texture

    def colorPrint(self): 
        # print (self.texture, '\n')
        out = f'You have picked : {self.color}'
        return out

pick = colorPicker('blue', 'matte')

# pick.colorPrint()
print (pick.colorPrint())