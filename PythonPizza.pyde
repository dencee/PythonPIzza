def setup():
    global mushroom, pepperoni, basil
    mushroom = loadImage("mushroom.png")
    mushroom.resize(80, 80)
    pepperoni = loadImage("pepperoni.png")
    pepperoni.resize(80, 80)
    basil = loadImage("basil.png")
    basil.resize(500, 500)
    imageMode(CENTER)
    
    # 1. Use the size(width, height) function to set the
    # width and height of your sketch
    
    # 2. Use the circle(x, y, diameter) function to create
    # the crust of your pizza
    
    # 3. Use the fill() function before drawing the circle
    # to set the color of your crust. 
    
    # 4. Use fill() and circle() to draw the sauce on top
    # of the crust

    # 5. Use fill() and circle() to draw the cheese on top
    # of the sauce
    
    
def draw():
    global mushroom, pepperoni, basil
    
    # 6. Use the image(topping, x, y) to add toppings to your
    # pizza! Pepperoni and basilare provided, but add at least 2 more!
    
    # 7. Use the mousePressed variable to place toppings on
    # the pizza when the mouse is pressed!
    
