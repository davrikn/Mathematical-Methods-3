def bezier(x, y):
    bx = 3*(x[1]-x[0])
    cx = 3*(x[2]-x[1]) - bx
    dx = x[3] - x[0] - bx - cx
    by = 3*(y[1]-y[0])
    cy = 3*(y[2]-y[1]) - by
    dy = y[3] - y[0] - by - cy

    print("x(t) = " + str(x[0]) +"+"+ str(bx) + "t" +"+"+ str(cx) + "t^2" +"+"+ str(dx) + "t^3")
    print("y(t) = " + str(y[0]) +"+"+ str(by) + "t" +"+"+ str(cy) + "t^2" +"+"+ str(dy) + "t^3")

if __name__ == "__main__":
    x = [-1,0,3,2]
    y = [0,3,2,-1]
    bezier(x,y)