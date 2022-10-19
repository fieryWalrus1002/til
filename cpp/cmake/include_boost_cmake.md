# How to include the boost library in CMakeLists.txt

```{cmake}
# ---- Include BOOST ----
SET (BOOST_ROOT "/usr/local/boost_1_80_0")
find_package(Boost)
target_link_libraries(${PROJECT_NAME} PUBLIC Boost::boost)
```
