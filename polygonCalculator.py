class Rectangle:
  def __init__(self, height, width):
    self.height = height
    self.width = width
    
  def set_height(self, height):
    self.height = height
    
  def set_width(self, height):
    self.width = height
  
  def get_area(self):
    return self.height * self.width
  
  def get_perimeter(self):
    return 2 * (self.height + self.width)
  
  def get_diagonal(self):
    return (self.height ** 2 + self.width ** 2) ** 0.5

  def get_picture(self):
    if self.height > 50 or self.width > 50:
      return "Too big for picture."
    else:
      picture = ""
      for i in range(self.height):
        picture += "*" * self.width + "\n"
      return picture
  def get_amount_inside(self, sape):
    return self.get_area() // sape.get_area()
    
  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"
    
class Square(Rectangle):
  def __init__(self, length):
    self.set_side(length)

  def set_side(self, length):
    self.height = length
    self.width = length
  
  def set_height(self, length):
    self.set_side(length)
    
  def set_width(self, length):
    self.set_side(length)

  def height(self):
    return self.width
    
  def __str__(self):
    return f"Square(side={self.width})"
