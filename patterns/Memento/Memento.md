This pattern is used for implementing undo mechanisms

- We create a new class called EditorState for managing the state of variables that we want to track their values
- we introduce a new list called `prevStates`
- having `prevStates` inside the Editor class breaks the SRP, so we introduce a new class called History to track the state
- The History class has two methods called push(state) and pop(), and states[] (states can be a stack too), and also have a composition relationship with the EditorState
- We then add two new methods to the Editor which are createState() (returns EditorState object) and restore(state)

Original class names as written in the book:

- Editor => Originator
- EditorState => Memento
- History => Caretaker
