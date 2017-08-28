
"""
# assume start at 0 0
move 0 1
move 1 1
move 5 5
"""


def move(robot, x, y, epsilon=0.0001):
    """
    Param:
    =====

    robot: instance of marvelmind.MarvelmindHedge"
    x: float: x-coordinate of target
    y: float: y-coordinate of target
    epsilon: float: threshold for distance to target
    """

    while True:
        cx, cy = robot.position()
        dx, dy = x - cx, y - cy

        # assume motion is horizontal or vertical only
        if abs(dx) >= epsilon
            # move left/right
            pass
        elif abs(dy) >= epsilon:
            # move up/down
            pass
        else:
            assert abs(dx) < epsilon and abs(dy) < epsilon
            robot.stop()
            break
