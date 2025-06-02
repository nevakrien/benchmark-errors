# "Basic" 2× Measurement

The code shown here tests a very basic assumption:  
**Is `x += 1; x += 1;` slower than `x += 2;`?**

However, as you can see from the code, this is anything but simple.  
In fact, it's not trivial to get a straightforward answer, and I’m not even sure I can confidently say how significant the speedup is.

I do know it's *around* 2× — but it might be 1.9, or 2.2. It may also depend on the processor.

There are multiple tricky aspects to measurement here.  
We’ll dive deeper into them in other chapters, but here’s a quick list of what we had to keep in mind:

---

1. **Compiler optimization**  
   We need `volatile` to make sure the compiler actually performs two separate additions.  
   Without it, a good compiler will reduce the loop to just one `+= 2` instruction.

2. **CPU resources**  
   We need to make sure the CPU frequency governor and the OS sceduler are fair — which is actually very hard, because the interference they introduces is *not* random.

3. **Process and timing overhead**  
   We need to account for the overhead of spawning processes and measuring time.  
   Here, we simply run enough iterations that the timing overhead becomes negligible by comparison.

4. **Loop overhead**  
   We also need to account for the loop overhead itself.  
   In this case, the loop is small enough that a modern CPU can effectively remove it.  
   _(More on that in the chapter about the branch predictor.)_

5. **Code alignment and caching**  
   We have to consider speedup/slowdown effects from code alignment and linking.  
   In this case, the code fits in the L1 instruction cache, so there is no interference from this type.

---

Even for this simplest possible benchmark, a lot of care is needed to get a meaningful measurement.  
This chapter demonstrates what a **correct** microbenchmark looks like — and sets the baseline for the bad examples that follow.

Note that if we just asked "is A faster than B" this becomes a lot simpler.
This kind of question is called a "Null hypothesis test" and it is sometimes preferred since we can be much more confident about the answer.