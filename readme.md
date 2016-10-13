# Sort Demo

Compare the sort algorithms.

Heap sort, Merge sort, Bubble sort, Insert Sort, Select Sort

Script outputs the executing time for different algo and number of input.


__Command Line__:

```bash
for a in 10 30 100 300 500; do python sortDemo.py $a; done
```  

output:
> insert sort : 0.01  bubble sort : 0.00  select sort : 0.01  merge sort : 0.00  heap sort : 0.00  
insert sort : 0.06  bubble sort : 0.03  select sort : 0.06  merge sort : 0.00  heap sort : 0.00  
insert sort : 0.61  bubble sort : 0.28  select sort : 0.64  merge sort : 0.01  heap sort : 0.01  
insert sort : 5.51  bubble sort : 2.71  select sort : 5.79  merge sort : 0.04  heap sort : 0.05  
insert sort : 15.30  bubble sort : 7.23  select sort : 16.08  merge sort : 0.07  heap sort : 0.09   