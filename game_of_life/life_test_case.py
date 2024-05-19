from game_of_life import update_cells # type: ignore

# test cases imported from tutorial

if __name__ == "__main__":
    # TEST 1: dead cells with no live neighbors
    # should stay dead.
    init_state1 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    expected_next_state1 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    actual_next_state1 = update_cells(init_state1)

    if expected_next_state1 == actual_next_state1:
        print ("PASSED 1")
    else:
        print ("FAILED 1!")
        print ("Expected:")
        print (expected_next_state1)
        print ("Actual:")
        print (actual_next_state1)

    # TEST 2: dead cells with exactly 3 neighbors
    # should come alive.
    init_state2 = [
        [0,0,1],
        [0,1,1],
        [0,0,0]
    ]
    expected_next_state2 = [
        [0,1,1],
        [0,1,1],
        [0,0,0]
    ]
    actual_next_state2 = update_cells(init_state2)

    if expected_next_state2 == actual_next_state2:
        print ("PASSED 2")
    else:
        print ("FAILED 2!")
        print ("Expected:")
        print (expected_next_state2)
        print ("Actual:")
        print (actual_next_state2)
