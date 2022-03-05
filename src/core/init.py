
class Effects : 

    def __init__(self) -> None:
        self.effects = ["anime"]
        self.effects_methods = [self._anime]

    def Make (self,img,effects):
        functional = self.effects_methods[self.effects.index(effects)]
        for x in range(0,img.shape[0]):
            for y in range(0,img.shape[1]):
                for z in range(0,img.shape[2]):
                    color = img[x][y][z] 
                    img[x][y][z] = functional(color)

        return img

    def _anime(self,pixel):
        min_pixel = 100
        max_pixel = 200
        coef_pixel = 10
        error_pixel = 10
        reponse = 0
        if pixel < min_pixel:
            reponse = 0
        elif pixel < max_pixel:
            for i in range(0,(max_pixel-min_pixel)//coef_pixel):
                if (pixel-error_pixel) <= min_pixel + coef_pixel*i:
                    reponse = min_pixel + coef_pixel*i
                    break
        else:
            reponse = 255

        return reponse