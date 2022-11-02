import time

start_time = time.time()


def time_to_run():
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    time_to_run()
