# compiler optimizations

removing the volatile from the example in chapter 1 causes any decent compiler to completly optimize away the loop.
in fact the assembly for the fast and slow version is exacly the same.

you can verify this with

```bash
make asm
```

and then

```bash
diff fast.s slow.s
1c1
< 	.file	"fast.c"
---
> 	.file	"slow.c"
```
which shows the only diffrence in the assembly is in the name of the source file.
so basically the machine code itself is identical.

# why?
This happens because the compiler is smart enough to see that 
```c
x+=1;
x+=1;
```
is equivelent to
```c
x+=2;
```

In fact it is even smart enough to already work out all of these additions and avoid the loop entirly.
We can see this in the assembly

on gcc-13 on x86-64 we get

```as
movl	$100000, %edx
```

which translates to "store 100000 to edx".

# what do we do about it?
When making benchmarks we need to make sure the compiler is actually doing the work we want it to do.
Depending on the languge the compiler can remove pretty much ANY code that is not directly OBSERVBLE to the user.

In chapter 1 we used the `volatile` keyword to tell the compiler "hey every time you change X treat it as if someone may see that change"
this stops the compiler from optimizing away our code. We could also use things like printing the result to achive a similar effect, the reason chapter 1 uses `volatile` is that the overhead from printing the result between each addition would simply be way too large, and at that point we are benchmarking the printing function.

Now what we have ALSO shown is that when coding C it really does not matter if you write 
```c
x+=1;
x+=1;
```
or 

```c
x+=2;
```

it gets optimized out and you really dont need to think about it.

I have seen so many people make these tiny "optimizations" which either do absolutly nothing or in some cases make the code SLOWER because they missunderstand what the compiler is actually doing.

this concept applies to many other languge runtimes: javascript under the V8 engine has the same behivior, as well as Go Rust C++ or any languge with an LLVM backend.
I have even seen it in gforth.

However some runtimes have such terible optimizers that they do not do this. 
The only example that comes to mind is cpython, but you may see this in other badly optimized runtimes.

# avoid abusing volatile
It might be tempting to put volatile everywhere when you benchmark, however unless you are directly benchmarking the processor itself thats a mistake.

in general `volatile` variables should only be written to via FUNCTIONS that you are benchmarking. their entire purpose is simply to verify the function has actually excuted. 

In many cases we are actually intested in testing how well can the compiler optimize our function inside a hot loop, if we are then `volatile` should generally be avoided in order to allow the compiler to properly optimize. This is typically the case for inline functions in C.
