% --- Water Jug DFS solver ---

% Example capacities (you can change)
capacity(jug1, 4).
capacity(jug2, 3).

% Target amount to measure
target(2).

% Initial state: both jugs empty
initial_state(state(0,0)).

% Goal: either jug has the target amount
goal(state(X,_)) :- target(X).
goal(state(_,Y)) :- target(Y).

% Allowed moves

% Fill jug1
move(state(X,Y), state(C1,Y)) :-
    capacity(jug1, C1),
    X < C1.

% Fill jug2
move(state(X,Y), state(X,C2)) :-
    capacity(jug2, C2),
    Y < C2.

% Empty jug1
move(state(X,Y), state(0,Y)) :-
    X > 0.

% Empty jug2
move(state(X,Y), state(X,0)) :-
    Y > 0.

% Pour jug1 -> jug2
move(state(X,Y), state(X2,Y2)) :-
    X > 0,
    capacity(jug2, C2),
    Space is C2 - Y,
    Transfer is min(X, Space),
    X2 is X - Transfer,
    Y2 is Y + Transfer.

% Pour jug2 -> jug1
move(state(X,Y), state(X2,Y2)) :-
    Y > 0,
    capacity(jug1, C1),
    Space is C1 - X,
    Transfer is min(Y, Space),
    X2 is X + Transfer,
    Y2 is Y - Transfer.

% DFS search: dfs(CurrentState, VisitedStates, Path)
dfs(State, Visited, [State]) :-
    goal(State).

dfs(State, Visited, [State|Path]) :-
    move(State, NextState),
    \+ member(NextState, Visited),
    dfs(NextState, [NextState|Visited], Path).

% Helper predicate to solve and print the path
solve :-
    initial_state(Start),
    dfs(Start, [Start], Path),
    print_path(Path).

print_path([]).
print_path([state(X,Y)|T]) :-
    format('Jug1: ~w liters, Jug2: ~w liters~n', [X,Y]),
    print_path(T).
    
%solve.
