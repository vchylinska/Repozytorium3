add_library('pdf')

def setup():
    size (400, 400, PDF, "nowy_id_zdjecie.pdf")
    global id_foto
    id_foto = loadImage("foto.jpg")
    print(type(id_foto))
    image(id_foto, 0, 0, height, width)
    id_okulary = loadImage("okulary.png")
    print(type(id_okulary))
    image(id_okulary, 85, 165, height/2+30, width/4)
    id_diadem = loadImage("diadem.png")
    print(type(id_diadem))
    image(id_diadem, 50, -160, 300, 300)


def draw():
    rectMode(CENTER)
    fill(150,210,155)
    rect(30, 30, 30, 30)
    
def draw():
    global img
    image(id_foto, 400, 400)
    rectMode(CENTER)
    fill(150,210,155)
    rect(30, 30, 30, 30)
    exit()
