# Rust and C/C++ COMBINED! cbindgen, and Rust Embedded code snippets

This is a really interesting treatment on embedded programming with Rust, and includes a cool section on creating a C api for calling Rust binaries in C/C++, under the topic "A little C with your Rust."

Link [here.](https://docs.rust-embedded.org/book/interoperability/rust-with-c.html)

## Set up a rust cargo project as follows:

```{rust}
[lib]
name = "your_crate"
crate-type = ["cdylib"]      # Creates dynamic lib
# crate-type = ["staticlib"] # Creates static lib
```

## Don't let Rust mangle your functions!
```{rust}
#[no_mangle]
pub extern "C" fn rust_function() {
}

```

This instructs the rust compiler to not mangle the symbols or whatever that means! There is a way to automate the creation of c bindings for rust code, [cbindgen](https://github.com/eqrion/cbindgen). It creats C/C++11 headers for Rust libraries, and exposes a public C API.

