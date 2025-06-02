# Sceduling weirdness

Our code generally runs inside of an operating system.
This has a lot of implications one of which is sceduling, the OS decides when code runs and for how long.

So if we have the OS stop runing our code in the middle of a benchmark that can cause issues. For instance if we have something here

```c
clock_t start = clock();
...
//ops the OS decided its time to do something else
...
clock_t end = clock();
```

the OS will ruin our benchmark.