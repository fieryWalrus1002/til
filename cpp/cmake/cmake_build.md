# Building projects with cmake

## build and run standalone target

```{cpp}
cmake -S standalone -B build/standalone #ready the build environment
cmake --build build/standalone #build the app
./build/standalone/<app name> #run app
```

## Build and run test suite

```{cpp}
cmake -S test -B build/test
cmake --build build/test
CTEST_OUTPUT_ON_FAILURE=1 cmake --build build/test --target test

# or simply call the executable:
./build/test/<app name>Tests
```
