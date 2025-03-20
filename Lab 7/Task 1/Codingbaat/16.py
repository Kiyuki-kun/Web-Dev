def make_bricks(small, big, goal):
    max_big_bricks = min(big, goal // 5)
    return (goal - max_big_bricks * 5) <= small