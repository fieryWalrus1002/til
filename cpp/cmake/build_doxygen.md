# Building doxygen documentation

If I'm running a copy of the cpp template, it already has what I need to run doxygen.

```{linux}
cmake -S documentation -B build/doc
cmake --build build/doc --target GenerateDocs

# view the docs
open build/doc/doxygen/html/index.html
```
