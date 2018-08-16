def distinct(items):
  distobj = {}
  isDistict = True
  for number in items:
    if distobj.has_key(number):
      print('duplicate number', number)
      isDistict = False
      break
    else:
      distobj[number] = 1
    print(number)
  
  print(isDistict)

distinct([1,2,4,4,5])