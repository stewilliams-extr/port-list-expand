# port-list-expand
This is a simple python function that will expand a port list

#### Python file:
[port-list-expand.py](port-list-expand.py)


#### Example output:
```
Computer:~$ python port-list-expand.py
port in is 1, and the list is ['1']
port in is 1-2, and the list is [1, 2]
port in is 1-3, and the list is [1, 2, 3]
port in is 1:1, and the list is ['1:1']
port in is 1:1-3, and the list is ['1:1', '1:2', '1:3']
port in is 1:1,1:2, and the list is ['1:1', '1:2']
port in is 1:1,2:2,2:10-12, and the list is ['1:1', '2:2', '2:10', '2:11', '2:12']
port in is 1/1, and the list is ['1/1']
port in is 1/1-5, and the list is ['1/1', '1/2', '1/3', '1/4', '1/5']
port in is 1/10,1/13,2/10-13, and the list is ['1/10', '1/13', '2/10', '2/11', '2/12', '2/13']
```
