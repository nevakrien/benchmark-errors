# clock-speed weirdness
on most CPUs there is a small peice of hardware called the **frequency governor**
which can slowdown or speedup the CPU depending on how much work it needs to do.

this matters a lot to us because if the CPU is cold for 1 benchmark and then fast for the other we will see a fake speedup. This is part of the reason why I am doing an ABBABAAB pattern for our benchmarks. So that code runs at generally the same time on probably the same CPU.

however as this benchmark shows this is not enough and backround calculations DO effect the CPUs clock speeds which has a consistent measurble effect on performance!!! on my machine when the AC is on its measuring at around 20% speedup (yes the heat in the room can effect this).

there is really no good way around this... you could potentially try and heat up the CPU by runing a very long busy loop before u start measuring. But this has the effect of potentially requiring a slowdown so the CPU can cool off.

# what we do

So there is genuinly no good option to remove the effects of the frequency governor.
The best we can do is to try and give both benchmarks similar CPU state or alternativly try to limit the damage to the final measurment.
Null hypothesis tests are actually really good at this because unlike a regrssion test we are not asking for an exact figure.

Its also a good idea to prefer end to end benchmarks rather than small secssions. Because the startup code has a meaningful performance effect and thus should absolutly be measured. For languges with a JIT its usually a good idea to use the `time` command in order to get a full measurment.

So as an example if we are comparing a luajit program to a C excutble we SHOULD include the JIT runtime in our tests. Since thats time the CPU gets to heat up. If that makes it hard to get a good final figure we may chose to spin up the CPU for the C program an apropriate amount of time.

However simply ignoring the problem can mess up our result to the point of showing an oposite effect to reality. Once you see this you can not unsee it. Soooo many benchmarks forget to acount for this effect while using the builin "`get_time`" command in their various runtimes.

[Versel](https://programming-language-benchmarks.vercel.app/lua-vs-c) usually gets it right in their benchmarks, by simply including a full end-to-end measurment. Unsuprisingly the measurments show C is faster than luajit across the board.

# OS considerations
This effect is destinct from the OS sceduler messing with our work. I have purposfully used long IO calls as the main drive of heat for the CPU because that keeps the CPU sceduler close to its initial state on most operating systems.