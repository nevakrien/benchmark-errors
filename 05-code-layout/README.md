# code layout

The location of code inside of the binary has a direct measurble effect on performance.
In C this can be controlled by the order in which we pass files to the linker/compiler... 
Because of course we want the order of name to have a meaningful effect on performance.

This happens because of 2 seprate reasons:
1. code needs to be loaded from memory, its cached exacly like data.
2. on some arches jumps/calls are more effishent if the destination is aligned

I am not telling you to hyperfixate on how functions are orgenized, as long as things are orgenized into files based on some sort of coherent ordering the effect should be minimal.

What I am telling you is that you have this semi "random" effect in the code that changes across versions.
This is the absolute worse because it can effect benchmarks even though its bound to change in future versions of the code.

So a speedup/slowdown could happen because a rewrite just happens to get better alignment and thus less padding leading to shorter code. But as soon as another if statment is needed that alignment would break and we would see a slowdown again.

The worse part about this effect is that it is persistent, there is no good way to sample out the noise, you are stuck with it for the entire current version. clang has a flag named `-frandomize-layout-seed` which randomizes where functions are linked and adds random padding. This can help mitigate this effect.