#!python3

def bishop(square):
  """
  input:
  str square: the coordinate of the square that the bishop is currently located in
  examples: 'f3' or 'g6'
  
  return:
  list of possible squares that the bishop can move to:
  """
  verticalb = vertical = square[1]
  horizontalb = horizontal = square[0]
  myList = []

  #topleft = square + 1 number - 1 letter 
  #topright = square + 1 number + 1 letter
  #bottomleft = square - 1 number - 1 letter 
  #bottomright = square - 1 number + 1 letter

  while vertical != 8 and horizontal != "a":
    horizontal  = chr(ord(horizontal )-1)
    vertical = int(vertical )+1
    myList.append(str(horizontal)+str(vertical))
  vertical = verticalb
  horizontal = horizontalb

  while vertical != 8 and horizontal != "h":
    horizontal  = chr(ord(horizontal )+1)
    vertical = int(vertical )+1
    myList.append(str(horizontal)+str(vertical))
  vertical = verticalb
  horizontal = horizontalb

  while vertical != 1 and horizontal != "a":
    horizontal  = chr(ord(horizontal )-1)
    vertical = int(vertical )-1
    myList.append(str(horizontal)+str(vertical))
  vertical = verticalb
  horizontal = horizontalb

  while vertical != 1 and horizontal != "h":
    horizontal  = chr(ord(horizontal )+1)
    vertical = int(vertical )-1
    myList.append(str(horizontal)+str(vertical))
  vertical = verticalb
  horizontal = horizontalb

  return myList








def main():
  myList = bishop('f3')
  myList.sort()
  assert myList == ['a8', 'b7', 'c6', 'd1', 'd5', 'e2', 'e4', 'g2', 'g4', 'h1', 'h5']
  myList = bishop('g7')
  myList.sort()
  assert myList == ['a1', 'b2', 'c3', 'd4', 'e5', 'f6', 'f8', 'h6', 'h8']

if __name__ == "__main__":
  main()
