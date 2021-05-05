## To use EOF (End of File)
  >> Here is the website https://blog.csdn.net/qq_35793358/article/details/77506726
  
  Code:
    ```pyhon
      import sys
      for line in sys.stdin:
        a=int(line) 
        if a!=0: 
          print(a)
    ```
    Another Way
    ```python
    try:
      while True:
        s = input()
    except EOFError:
      pass
    ```
