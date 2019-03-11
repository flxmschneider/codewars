def bouncingBall(h, bounce, window):
    if (h <= 0) or (bounce <=0) or (bounce >=1) or (window >=h):
        return -1
    counter = 0
    while h > window:
        counter += 1
        h = h*bounce
        if h > window:
            counter +=1
    return counter 
