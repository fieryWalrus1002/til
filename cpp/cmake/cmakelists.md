# Creating cmakelist.txt files

This is a minimal CMakeLists.txt. There are much more robust versions in the cpptemplate project repo, but this will do the trick for a small project.

```{cmake}
cmake_minimum_required(VERSION 3.16)
project(cpp_restconf)
add_excecutable(src/main.cpp)
```
