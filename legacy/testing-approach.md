# Apporach to testing legacy code: Strangler Pattern

Don't try to refactor to unit tests for the whole of the legacy code. That often results in more bugs. 

Instead, evaluate the system only in the area you want to be making changes. Create test cases that target only that functionality, and create an anti-corruption layer. 

An anti-corruption layer is created by utilizing an abstracted inferface between your changes and the rest of the legacy code. The surrounding legacy code will interact with the abstract interface as it did to the pre-existing code, and the interface will interpret those requests and carry them out with our new, unit-tested code. 

The piece of code we extracted can be thrown away, rewritten, thoroughly covered by unit tests. 

## The Strangler Pattern
Named after the strangler vine in australia. It wraps a tree, and kills it, leaving the dead tree as a structure for the vines to grow on. In a similar way, we are encapsulating and re-writing a part of the legacy code, killing and replacing it with our own code.
