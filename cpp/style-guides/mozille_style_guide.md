# Mozilla C++ Style Guide

The Mozilla C++ Style Guide is a nice clean style guide for organizing and formatting your c++ code and project structure.
[Check it out!](https://firefox-source-docs.mozilla.org/code-quality/coding-style/coding_style_cpp.html)

The short version:

## C++ Classes

```{c++}
namespace magnus {

class MyClass : public A
{
  ...
};

class MyClass
  : public X
  , public Y
{
public:
  MyClass(int aVar, int aVar2)
    : mVar(aVar)
    , mVar2(aVar2)
  {
     ...
  }

  // Special member functions, like constructors, that have default bodies
  // should use '= default' annotation instead.
  MyClass() = default;

  // Unless it's a copy or move constructor or you have a specific reason to allow
  // implicit conversions, mark all single-argument constructors explicit.
  explicit MyClass(OtherClass aArg)
  {
    ...
  }

  // This constructor can also take a single argument, so it also needs to be marked
  // explicit.
  explicit MyClass(OtherClass aArg, AnotherClass aArg2 = AnotherClass())
  {
    ...
  }

  int LargerFunction()
  {
    ...
    ...
  }

private:
  int mVar;
};

} // namespace magnus
```

## Methods and functions

Method names should use UpperCamelCase, such as GetTaco(), not getTaco() or get_taco() like you constantly do instead.

If a getter will never fail and never return Null, name the getter after the object that is being gotte, such as Foo(). All other getters should be GetFoo().

## Variable prefixes

    k = constant (e.g. kNC_child). Not all code uses this style, some uses ALL_CAPS for constants.

    g=global (e.g. gPrefService)

    a=argument (e.g. aCount)

    C++ Specific Prefixes

        s=static member (e.g. sPrefChecked)

        m=member (e.g. mLength)

        e=enum variants (e.g. enum Foo { eBar, eBaz }). Enum classes should use CamelCase instead (e.g. enum class Foo { Bar, Baz }).
