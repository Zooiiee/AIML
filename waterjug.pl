/* Water Jug Problem using DFS */

/* Define jug capacities */
capacity(jugA, 4).
capacity(jugB, 3).

/* Define the goal state: Jug A should have 2 liters */
goal(state(2, _)).

/* Define possible moves */
move(state(A, B), state(4, B)) :- A < 4.        % Fill Jug A
move(state(A, B), state(A, 3)) :- B < 3.        % Fill Jug B
move(state(A, B), state(0, B)) :- A > 0.        % Empty Jug A
move(state(A, B), state(A, 0)) :- B > 0.        % Empty Jug B

% Pour A to B
move(state(A, B), state(NewA, NewB)) :-
    A > 0, B < 3,
    Transfer is min(A, 3 - B),
    NewA is A - Transfer,
    NewB is B + Transfer.

% Pour B to A
move(state(A, B), state(NewA, NewB)) :-
    B > 0, A < 4,
    Transfer is min(B, 4 - A),
    NewB is B - Transfer,
    NewA is A + Transfer.

/* DFS: Path search */
dfs(State, Path, [State | Path]) :-
    goal(State).

dfs(State, Visited, FinalPath) :-
    move(State, NextState),
    \+ member(NextState, Visited),  % Avoid cycles
    dfs(NextState, [State | Visited], FinalPath).

/* Solve and print the result */
solve :-
    dfs(state(0, 0), [], Path),
    reverse(Path, SolutionPath),
    write('Solution Path:'), nl,
    print_path(SolutionPath),
    last(SolutionPath, Goal),
    write('Goal State: '), write(Goal), nl.

print_path([]).
print_path([H | T]) :-
    write(H), nl,
    print_path(T).
