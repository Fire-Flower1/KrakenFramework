## Instructions
Create a main.py file containing a `main()` function where you execute your code.

feel free to use other files and libraries in your function

i.e. you might have a file called `printSomething.py`:
```
class printSomething:
  def __init__(self):
    print("Something")

  def printOtherThings(self):
    print("more something")
```

and this works fine **as long as** you have a `main.py` that calls this class
i.e.
```
from printSomething.py import printSomething

def main():
  printing = printSomething()
  printing.printOtherThings()
```

and this should work fine.
