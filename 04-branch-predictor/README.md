# branch predictor

CPUs don't actually execute code sequentially, that's just a convenient lie we tell ourselves. The public API pretends to be sequential for the most part but there are measurable out of order effects we can observe.

Most CPUs execute instructions significantly faster than they can read memory. Because of this it would be incredibly helpful if the CPU did not have to wait idle between every tiny read.

To solve this a modern CPU tries to guess what the result of a memory read would be. It can then execute the code optimistically and get a lot of work done while waiting for the result of a read.

This guessing process is usually extremely accurate, on most benchmarks accuracy is at least 95% usually much higher. You can see for yourself in [this paper](https://arxiv.org/pdf/1906.08170) or just on [Wikipedia](https://en.wikipedia.org/wiki/Branch_predictor).

Predictable inputs generally make for much easier predictions and this can be observed in the benchmark code here. Important to note that the effect varies across CPUs so you might need to fiddle around with the code to get this to work on your particular machine. On my machine I have managed to use these effects to completely reverse the outcome of a benchmark.

# so what do we do?
Generally speaking this does not require any immediate action by us. It does have some major implications when we want to measure a CPU directly. Specifically when measuring the performance of a loop its important to note that the CPU would generally assume the loop keeps going. So loop overhead is actually significantly cheaper than may seem based on the raw assembly.

Its also important to keep in mind that irregular code is significantly more expensive. and that function calls done before the start of a benchmark DO effect the branch predictor and thus can change the result.

# example case

There are 3 separate benchmarks in this folder

1. bench-main: where we directly compare regular to irregular inputs
2. bench-fair: which just a control case between a slow and a fast program.
3. bench     : here we use regular inputs to make the slow program BEAT the fast program.

Getting the code into a state where `bench-fair` passes but `bench` fails took a lot of fiddling around. It will likely act different on your machine so I encourage you to try and make it work by playing with slow.c