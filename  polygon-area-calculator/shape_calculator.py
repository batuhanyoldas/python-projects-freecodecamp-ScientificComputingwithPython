class Rectangle:
  #Initialize 
  def __init__(self, width, height):
    self.width = width
    self.height = height
  # Text representation
  def __str__(self):
    return 'Rectangle(width='+ str(self.width)+', height='+ str(self.height) +')'
  # Methods
  def set_width(self, width):
    self.width = width
  def set_height(self, height):
    self.height = height
  def get_area(self):
    return self.height * self.width
  def get_perimeter(self):
    return 2*self.height + 2*self.width
  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5
  def get_picture(self):
    picture = ""
    if self.width > 50 or self.height > 50:
      picture = "Too big for picture."
    else:
      for x in range(self.height):
        picture += "*"*self.width + "\n"
    return picture
  def get_amount_inside(self,shape):
    div_width = self.width // shape.width
    div_height = self.height // shape.height
    return div_width * div_height

class Square(Rectangle):
  #Override init and text representation
  def __init__(self, length):
    self.width = self.height = length
  def __str__(self):
    return "Square(side="+ str(self.width) +")"
  #Overwritten methods
  def set_height(self, length):
    self.width = self.height = length
  def set_width(self, length):
    self.width = self.height = length
  #Unique method
  def set_side(self, length):
    self.width = self.height = length