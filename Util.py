import math

def get_distance(p1, p2):
	return math.sqrt(math.pow((p1[0] - p2[0]), 2) + math.pow((p1[1] - p2[1]), 2))

def get_angle(p1, p2):
	return (math.degrees(math.atan2(p1[1] - p2[1], p1[0] - p2[0])) + 360) % 360

def check_collision(p1, p2):
    if get_distance(p1.position, p2.position) <= p1.size + p2.size:
        return True
    return False

def normalize_angle(angle):
    if angle < 0:
        angle += 360
    return angle / 360.0
    #return math.atan2(math.sin(angle), math.cos(angle))