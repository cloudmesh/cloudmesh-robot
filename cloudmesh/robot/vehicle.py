from __future__ import print_function


class Vehicle(object):
    def __init__(self, name, history):
        """
        createa vehicle, history is a file to which we save the position
        :param name: 
        :param history: 
        """
        self.name = name
        self.x = self.x0 = 0
        self.y = self.y0 = 0
        self.z = self.z0 = 0
        self.t = 0
        self.x0

    def set_speed(self, speed):
        """
        sets the speed
        :param speed: 
        :return: 
        """
        pass

    def get_speed(self):
        """
        returns the speed
        :return: 
        """
        pass

    def turn(self, angle):
        """
        :param angle: angle to turn
        :return: 
        """
        pass

    def move_turn(self, direction, dt):
        """
        turn for dt seconds
        :param direction: "left", "right"
        :param dt: time to turn
        :return: 
        """
        pass

    def move(self, dt):
        """
        moves forward for the given time
        :param dt: time in seconds 
        :return: 
        """
        pass

    def drive_to(self, x, y, z, dt=0.1):
        """
        drives to the position x,y,z
        :param x: 
        :param y: 
        :param z: ignore for now 
        :param dt: time for next check point
        :return: 
        """
        pass

    def set_origin(self):
        """
        sets the origen to the current position
        :return: 
        """
        pass

    def set_marker(self):
        """
        saves the current position into a marker x0
        :return: 
        """

    def save_position(self):
        """
        saves the position into an file
        :return: 
        """
        pass

    def clear_position(self):
        """
        saves the position
        :return: 
        """
        pass

    def get_position(self, i):
        """
        get the ith position
        :param i: 
        :return: 
        """
        return self.name, 0.0, 0.0, 0.0, 0.0
