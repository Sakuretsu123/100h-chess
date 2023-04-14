#!python3

def knight(square):
  """
  input:
  str square: the coordinate of the square that the knight is currently located in
  examples: 'f3' or 'g6'
  
  return:
  list of possible squares that the knight can move to:
  """
  #a b c d e f g h 
  # 8
  # 7
  # 6 
  # 5 
  # 4 
  # 3 
  # 2 
  # 1 

  verticalb = vertical = square[1]
  horizontalb = horizontal = square[0]
  myList = []

  #move1 up up left
  

  horizontal  = chr(ord(horizontal )-1)
  vertical = int(vertical) + 2
  myList.append(str(horizontal)+str(vertical))

  if horizontalb == "a" or verticalb == "7" or verticalb == "8": 
    myList.pop()
  horizontal = horizontalb
  vertical = verticalb

  #move2 up up right
  

  horizontal  = chr(ord(horizontal )+1)
  vertical = int(vertical) + 2
  myList.append(str(horizontal)+str(vertical))

  if horizontalb == "h" or verticalb == "7" or verticalb == "8": 
    myList.pop()
    
  horizontal = horizontalb
  vertical = verticalb

  #move3 right right up

  horizontal  = chr(ord(horizontal )+2)
  vertical = int(vertical) + 1
  myList.append(str(horizontal)+str(vertical))

  if verticalb == "8" or horizontalb == "g" or horizontalb == "h": 
    myList.pop()

  horizontal = horizontalb
  vertical = verticalb

  #move4 right right down
  

  horizontal  = chr(ord(horizontal )+2)
  vertical = int(vertical) -1
  myList.append(str(horizontal)+str(vertical))

  if verticalb == "1" or horizontalb == "g" or horizontalb == "h": 
    myList.pop()

  horizontal = horizontalb
  vertical = verticalb

  #move5 down down right 

 

  horizontal  = chr(ord(horizontal )+1)
  vertical = int(vertical) -2
  myList.append(str(horizontal)+str(vertical))

  if horizontalb == "h" or verticalb == "1" or verticalb == "2": 
    myList.pop()
    
  horizontal = horizontalb
  vertical = verticalb 

  #move6 down down left
  

  horizontal  = chr(ord(horizontal )-1 )
  vertical = int(vertical) -2
  myList.append(str(horizontal)+str(vertical))

  if horizontalb == "a" or verticalb == "1" or verticalb == "2": 
    myList.pop()
    
  horizontal = horizontalb
  vertical = verticalb

  #move7 left left down


  horizontal  = chr(ord(horizontal )-2)
  vertical = int(vertical) -1
  myList.append(str(horizontal)+str(vertical))

  if verticalb == "1" or horizontalb == "a" or horizontalb == "b": 
    myList.pop()
    
  horizontal = horizontalb
  vertical = verticalb
  #move8 left left up
  

  horizontal  = chr(ord(horizontal )-2 )
  vertical = int(vertical) +1

  
  if vertical <= 8: 
    myList.append(str(horizontal)+str(vertical))
  if verticalb == "8" or horizontalb == "a" or horizontalb == "b": 
    myList.remove[-1]
    
  horizontal = horizontalb
  vertical = verticalb


  return myList


def main():
  myList = knight('g7')
  myList.sort()
  assert myList == ['e6', 'e8', 'f5', 'h5']
  myList = knight('d4')
  myList.sort()
  assert myList == ['b3', 'b5', 'c2', 'c6', 'e2', 'e6', 'f3', 'f5']

if __name__ == "__main__":
  main()
