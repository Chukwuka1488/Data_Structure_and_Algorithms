"""
Eight houses, represented as cells, are arranged in a straight line. Each day every cell competes with its adjacent
cells (neighbors). An integer value 1 represents an active cell and a value of 0 represents an inactive cell.
If the neighbors on both the sides of a cell are either active or inactive, the cell becomes inactive on the next day;
otherwise the cell becomes active. The two cells on each end have a single adjacent cell, so assume that the unoccupied
space on the opposite side is an inactive cell. Even after updating the cell state, consider its previous state when
updating the state of other cells. The state information of all cells should be updated simultaneously.

Write an algorithm to output the state of the cells after the given number of days.
"""
import running_time


def cellCompete(states, days):
    new = states[:]  # get a copy of the array
    n = len(states)

    if n == 1:
        print[0]  # when only 1 node, return [0]

    for _ in range(days):
        new[0] = states[1]  # determine the edge nodes first
        new[n - 1] = states[n - 2]

        for i in range(1, n - 1):
            new[i] = 1 - (states[i - 1] == states[i + 1])  # logic for the rest nodes
        states = new[:]  # update the list for the next day
    # print(new)
    return " ".join(str(item) for item in new)


if __name__ == '__main__':
    state = [1, 1, 1, 0, 1, 1, 1, 1]
    day = 2
    print(cellCompete(state, day))
    running_time.time_to_run()
