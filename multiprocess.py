from multiprocessing import Process

def f():
    while True:
        print("I pray for universal basic income")


if __name__ == '__main__':
    for item in range(0, 32):
        p = Process(target=f, args=())
        p.start()
        p.join()
