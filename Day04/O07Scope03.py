
# nested function
glbx = 100

def outerFun(gst):                  # local variable for outer
    info = f"Mr. {gst}"
    global glbx
    glbx = 500

    def innerFun():
        nonlocal  info
        info = f'Mr. Dravid'


        print(f"hello {gst}")
        print(info)

    innerFun()
    print(info)

outerFun("Rahul")
print(f"glbx :{glbx}")
