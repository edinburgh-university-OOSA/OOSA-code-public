

def perp_dist(x1, x2, x3, y1, y2, y3):
  '''
  This function returns the perpendicular distance from a point to a line segment.
    
  (x1,y1) and (x2,y2) define the start and end points of your line.
  (x3, y3) defines a point.
  '''
  if x2==x1:
    return abs(x3-x1)
  m = (y2-y1)/(x2-x1)
  c = y1-m*x1
  d = abs(m*x3 - y3 + c)/(m**2 + 1)**0.5
  return d

