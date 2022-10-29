# Steps of refactoring legacy code

1. Remove Clutter
2. Reduce cyclomatic complexity 
3. compose Methods

## Remove Clutter
Delete commented out code. You have git repositories you can reference for old versions of the functions. Don't keep these. It reduces readability and is often left over from previous versions, and uncommenting it out would lead to bugs.

## Reduce cyclomatic complexity
Take some of those branching if statements, and simplify them. Break the inner parts into different functions, to isolate when and why from the what and how. 

## Compose methods
