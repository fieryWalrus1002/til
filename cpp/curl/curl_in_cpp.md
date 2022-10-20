# include curl in c++ projects using cmake

In the CMakeLists.txt file, you can add curl to the target_link_libraries line, like so:

```
target_link_libraries(${PROJECT_NAME} PUBLIC Boost::boost curl)
```

I got the correct lib name by running 'curl-config --libs' in terminal, which gave the response '-lcurl'. The '-l' part is automatically added as a prefix by cmake, so we just need to provide the curl part. The path for curl is already added to path in my installation, but if you're compiling yourself you might need to add it.

To include the curl library in your cpp file, just do:

```
#include <curl/curl.h>
```

Everything compiles from there.
