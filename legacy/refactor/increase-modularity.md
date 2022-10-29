# increasing modularity in legacy code

These are some thoughts on how to increase modularity in legacy code. I have a lot of learnign to do here.
<todo> <learninggoal>
* When trying to increase modularity in the code, used the problem domain and bounded-context as a guide. What components of the code are tied together, and have a common view of the world. Those are your boundaries of the scope. Try to zero in on the smallest set.
* Establish 'seams' in the code. These are places you can break the code down into smaller, independent parts.
* Use refactoring techniques to improve abstraction. This also increases maintainability, testability, and reusability!
* Separation-of-conerns is something you should always be looking to improve.
* Boy scout, leave the code in a better state every commit. Little piece by little piece.
* Make progress tactically, change what you must to solve the problem in front of you.
* Solutions will be specific to system and tech. 
* Work in a series of experiments to improve performance. Measure and test!
