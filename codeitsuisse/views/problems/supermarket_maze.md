# Supermarket Maze

### Instructions
While shopping for groceries you find that the supermarket is like a maze filled with blocked walkways that hinder your shopping sprees. 

Given the floor plan of the supermarket, find the number of steps made within the shortest path from the entrance to the checkout counter.

To make things interesting some mazes are unsolvable, in that case return -1 as number of steps to solve the maze! 

Expose a `POST` endpoint `/supermarket` for us to verify!

#### Input
```json5
{
    "tests": {
        "0":{
            "maze": [[1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
                     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                     [1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
                     [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1],
                     [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
                     [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
                     [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
                     [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
                     [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1],
                     [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
                     [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]],
            "start": [3, 0],
            "end": [1, 10]
        },
        "1": {
            "maze": [[1, 1, 1, 0, 1, 1, 1, 1, 1],
                     [1, 1, 1, 0, 0, 0, 0, 0, 1],
                     [1, 1, 1, 0, 1, 1, 1, 0, 1],
                     [1, 1, 1, 0, 0, 0, 1, 0, 1],
                     [1, 1, 1, 1, 1, 0, 1, 0, 1],
                     [1, 0, 0, 0, 1, 0, 1, 0, 1],
                     [1, 0, 1, 1, 1, 0, 1, 0, 1],
                     [1, 0, 0, 0, 0, 0, 1, 0, 1],
                     [1, 1, 1, 1, 1, 1, 1, 0, 1]],
            "start": [3, 0],
            "end": [7, 8]
        },
        "2": {
          "maze": [[1, 1, 1, 0, 1, 1, 1, 1, 1],
                   [1, 1, 1, 0, 0, 0, 0, 0, 1],
                   [1, 1, 1, 0, 1, 1, 1, 0, 1],
                   [1, 1, 1, 0, 0, 0, 1, 0, 1],
                   [1, 1, 1, 1, 1, 0, 1, 1, 1],
                   [1, 0, 0, 0, 1, 0, 1, 0, 1],
                   [1, 0, 1, 1, 1, 0, 1, 0, 1],
                   [1, 0, 0, 0, 0, 0, 1, 0, 1],
                   [1, 1, 1, 1, 1, 1, 1, 0, 1]],
          "start": [3, 0],
          "end": [7, 8]
        },
        ...
    }
}
```

#### Output Expected
```json5
{
    "answers": {
            "0": 29,
            "1": 13,
            "2": -1,
            ...
    }
}
```

### Limitations
1. Assume that the start point is `(X,0)` where `X can be the x-coordinate within the length of the maze`
2. No diagonal movement
3. The floor plan
    - A wall is represented by `1`
    - A walkable space is represented by `0`
    
### Example

#### Example Input
```
[1, 1, 1, 0, 1, 1, 1]
[1, 0, 1, 0, 0, 0, 1]
[1, 0, 0, 0, 1, 0, 1]
[1, 1, 0, 1, 1, 1, 1]
[1, 0, 0, 0, 0, 1, 1]
[1, 1, 1, 1, 0, 1, 1]

Coordinates will be given in as [x-axis, y-axis]

start: [3, 0]
end: [4, 5]
```
 
#### Example Output
```
answer: 9
```
##### Visualization
[1, 1, 1, <b style="color:red">0</b>, 1, 1, 1]<br>
[1, 0, 1, <b style="color:red">0</b>, 0, 0, 1]<br>
[1, 0, <b style="color:red">0</b>, <b style="color:red">0</b>, 1, 0, 1]<br>
[1, 1, <b style="color:red">0</b>, 1, 1, 1, 1]<br>
[1, 0, <b style="color:red">0</b>, <b style="color:red">0</b>, <b style="color:red">0</b>, 1, 1]<br>
[1, 1, 1, 1, <b style="color:red">0</b>, 1, 1]

Actual number of test cases given may change.
