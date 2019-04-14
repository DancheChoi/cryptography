alphabet = "abcdefghijklmnopqrstuvwxyz"
engima = "qwertyuiopasdfghjklzxcvbnm"

def encrypt(message):
    a = 0
    for i in range(0, len(message)):
      result = message.split('')
      if result[i] == alphabet[a]:
          result[i].replace(engima[a])

      else:
          while result[i] != alphabet[a]:
              a = a + 1
          result[i].replace(engima[a])
      y = ""
      return result.join[y]

def decrypt(message):
        a = 0
    for i in range(0, len(message)):
      result = message.split('')
      if result[i] == alphabet[a]:
          result[i].replace(engima[a])

      else:
          while result[i] != engima[a]:
              a = a + 1
          result[i].replace(alphabet[a])
      y = ""
      return result.join[y]

    
