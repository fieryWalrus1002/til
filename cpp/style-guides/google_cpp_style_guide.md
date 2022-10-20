# Google C++ Style Guide Summary

This is my summary of the key ideas from the Google C++ style guide. Visit the complete style guide [here.](https://google.github.io/styleguide/cppguide.htmls)

## Header files

Every .cpp file should have an associated .h file. Unit tests don't need one.

1. Header files should be self-contained (compile on their own) and end in .h.
2. When a header declares inline functions or templates, the inline functions and templates must also have definitions in the header.
3. Use a header guard, such as:

```{cpp}
#ifndef FOO_BAR_BAZ_H_
#define FOO_BAR_BAZ_H_

...

#endif  // FOO_BAR_BAZ_H_

```

## Forward declarations

Avoid using forward declarations if possible. Instead, include the headers you need.

## Inline Functions

Define functions inline only when they are very small (<10 lines).

## Names and Order of Includes

Include headers in the following order, separated by blank lines for readability:

1. Related header (thisfile.h)
2. C system headers
3. C++ STL headers
4. other libraries' headers
5. Your project headers

All project headers should be listed as descendants of the project's source directory, without linux dir aliases ('./', '../')

But, wait! Theres more!

## Struct vs Class vs Tuple vs Pair

Classes are favored over structs, except when the object will only be a passive carrier of data. Then use a struct. All fields are public in a struct.

If you're using an object purely for data, prefer the struct over the pair and tuple. This is because you can give the variables a meaningful field name that will make reading the code later easier.

## Classes

### Declaration Order

Declare public, then protected, then private. Omit empty sections.

WIthin a section, group similar declarations together like so:

1. Type and type aliases
2. Static constants
3. Factory functions
4. Constructors and assignment operators
5. Destructor
6. All ofther functions
7. Data members (static and non-static)

Only define very short functions in-line.

## Functions

Prefer using return values over output parameters.
Prefer to return by value, then return by reference. Avoid returning pointers unless it can be null.

### input parameters to functions

Non-optional parameters should usually be values or const references, while non-optional output and input/output parameters shoudl usually be references(which cannot be null). Generally, use std::optionalto represent optional byvalue inputs.
