#resize plane object to dimensions of material image
#looks at material color chanel

import c4d,os 
from c4d import gui, bitmaps 

def getImageSize(): 
    mat = [i for i in op.GetTags() if i.GetType() == 5616][0][c4d.TEXTURETAG_MATERIAL]
    pathToFile = mat[c4d.MATERIAL_COLOR_SHADER][c4d.BITMAPSHADER_FILENAME]
    
    bmp = bitmaps.BaseBitmap(pathToFile) 
    bmp.InitWith(pathToFile) 
        
    x, y = bmp.GetSize() #Gets the X and Y dimensions of the image 
    return [x, y]

def resizeCard():
    op[c4d.PRIM_PLANE_WIDTH] = getImageSize()[0]
    op[c4d.PRIM_PLANE_HEIGHT] = getImageSize()[1]
    

resizeCard()
c4d.EventAdd()
