#!/usr/bin/python3

v1 = (1, 2)
v2 = (4, 5)
v3 = (3, 15)

m = (8/3, 22/3)


def linear(x, y):
    denom = (v2[0] - v1[0]) * (v3[1] - v1[1]) - (v2[1] - v1[1]) * (
        v3[0] - v1[0])
    t2 = ((v2[0] - v1[0]) * (x - v1[0]) + (v1[0] - v3[0]) * (y - v1[1])) / denom
    t3 = ((v1[1] - v2[1]) * (x - v1[0]) + (v3[1] - v1[1]) * (y - v1[1])) / denom
    return 1 - t2 - t3

def barycentric(x, y):
    denom = ((v2[1]-v3[1])*(v1[0]-v3[0])+(v3[0]-v2[0])*(v1[1]-v3[1]))
    w = (v2[1]-v3[1])*(x-v3[0])+(v3[0]-v2[0])*(y-v3[1])
    return w / denom

def bc1(x, y):
    denom = ((v2[1]-v3[1])*(v1[0]-v3[0])+(v3[0]-v2[0])*(v1[1]-v3[1]))
    w = (v2[1]-v3[1])*(x-v3[0])+(v3[0]-v2[0])*(y-v3[1])
    return w / denom

def bc2(x, y):
    denom = ((v2[1]-v3[1])*(v1[0]-v3[0])+(v3[0]-v2[0])*(v1[1]-v3[1]))
    w = (v3[1]-v1[1])*(x-v3[0])+(v1[0]-v3[0])*(y-v3[1])
    return w / denom

def bc3(x, y):
    denom = ((v2[1]-v3[1])*(v1[0]-v3[0])+(v3[0]-v2[0])*(v1[1]-v3[1]))
    w1 = ((v2[1]-v3[1])*(x-v3[0])+(v3[0]-v2[0])*(y-v3[1])) / denom
    w2 = ((v3[1]-v1[1])*(x-v3[0])+(v1[0]-v3[0])*(y-v3[1])) / denom
    return 1-w1-w2

def test(pt):
    print("({:06.3f},{:06.3f})  {:+06.3f}  {:+06.3f} {:+06.3f} {:+06.3f}".format(pt[0], pt[1], linear(*pt), bc1(*pt), bc2(*pt), bc3(*pt)))

def main():
    test(v1)
    test(v2)
    test(v3)
    test(m)
    pass


if __name__ == "__main__":
    main()
