from game_of_life import update_cells # type: ignore


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
        print ("Expected:")
        print ("FAILED 1!")
        print (expected_next_state1)
        print ("Actual:")
        print (actual_next_state1)
