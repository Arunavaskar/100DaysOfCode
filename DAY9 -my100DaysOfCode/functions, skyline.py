def myfunc(string):
     new_s= '' #empty string to hold further values
     for i,l in enumerate(string): # enumerate returns both, index numbers and objects
                                   # so i = index number and l = letter
         if i%2==0: # if index number % 2 == 0 (even number)
              new_s += l.upper() # add an upper cased letter to the new_s
          else: # if index number is an odd number
              new_s += l.lower() # add a lower cased letter to new_s
      return new_s # returns the string new_s