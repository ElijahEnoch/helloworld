import random


class person:

    def __init__(self, n):
        x = [i for i in range(n)]
        self.x = x

    def __del__(self):
        print("Thanos is death.")

    def FingerSnap(self):
        while len(self.x) > 5:
            self.x.remove(random.choice(self.x))
        return self.x

    def __str__(self):
        return "there are {},but {} will remain.".format(len(self.x), int(len(self.x)/2))



def main():
    thanos = person(10)

    print(thanos)
    print(thanos.FingerSnap())

if __name__ == '__main__':
    main()
