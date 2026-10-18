def timeConversion(s):
  ofDay = s[-2:]
  preConvert = s[:-2]
  hour = int(s[:2])
  print(hour)
  
  if ofDay == "AM": 
      if hour == 12:
          newTime = preConvert[2:]
          print("00" + newTime)
  
  if ofDay == "PM":
      if hour == 12:
          return preConvert
      newHr = str(hour + 12)
      newTime = preConvert[2:]
      print(newHr + newTime)
  return

timeConversion("12:40:22AM")