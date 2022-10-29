# Steps of refactoring legacy code

Refactoring is making behavior-preserving changes. You want the end product of this piece of the code to behave exactly as it did before, but have it be more testable and easier to understand and maintain. If you change how it works at the same time, it may introduce some tricky bugs in other parts of the legacy code that you wouldn't even imagine to be coupled. This material is mostly my notes taken while watching [this video by Continuous Delivery on Youtube.](https://www.youtube.com/watch?v=Z2c3sGUE2GA)

## Before we begin, isolate your changes from the main branch:
Create a new branch dedicated to your refactoring. After each change, make a commit. With this style, you'll have a step-by-step process that can be revisited later, and revised if needed. It is very hard to break your code when you are doing this kind of isolation. 

After you have your new branch ready, follow these rough steps.

1. Remove Clutter
2. Reduce cyclomatic complexity 
3. compose Methods

## 1. Remove Clutter
Delete commented out code. You have git repositories you can reference for old versions of the functions. Don't keep these. It reduces readability and is often left over from previous versions, and uncommenting it out would lead to bugs.

## 2. Reduce cyclomatic complexity
Take some of those branching if statements, and simplify them. Break the inner parts into different functions, to isolate when and why from the what and how. This lets you test each part of the code blob, step by step.

## 3. Compose methods
Refactor by pulling bits of code out, naming it and refining it.

## 4. Remove Duplication
As the first three steps are happening, you will observe duplication in the code. 

## 5. Seperate concerns, reduce dependencies. 
A large bit of code is probably doing many things. Take those different things and break them out. It will make the individual components smaller and more testable.

## 6. Work in TINY steps
The smaller the step, the safer the step. Martin Fowler writes a few good books on refactoring.

## 7. Use a modern IDE with refactoring tools, and learn how to utilize them properly. 
More automated work, less human error from forgetting to rename variables or mistype function names, etc. 
