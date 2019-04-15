import math

def main():
    X = []
    Y = []
    for i in range(1000):
        X.append(40 + (340/1000)*(i))
        Y.append(80+(340/2)*(math.sin(math.pi*2/1000*i)+1))
    print(list(zip(X,Y)))

if __name__ == "__main__":
    main()
