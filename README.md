# benchmark-errors
This repo is a collection of common benchmarking errors. We go into all of the hardware weirdness as well as some of the statistics needed to make a good benchmark.

The languge chosen is C since a lot of the concepts are easier to SHOW in C,
however this is fundemental to how modern computers work and all of these are present in any languge,
in fact the driving force behind making this repo was a bad article about luajit speedups in relation to C.

# build/run
to get the code on your computer run
```bash
git clone https://github.com/nevakrien/benchmark-errors.git
```

every leason is made as a seprate folder but they all use the same analyzer which is in this main folder.
to make sure that works properly please run
```bash
pip install -r requirments.txt
```

for every leason u can run the main benchmark with
```
make bench
```

regardless of how that benchmark is setup.

# play/contribute
You are encouraged to modify the code and try adding examples of your own.
The analyzer is made to check the output of your code to avoid mistakes in implementation.

You can also add folders with new examples in any languge you prefer. I am not picky.