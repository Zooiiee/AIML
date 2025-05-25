/* Entry point: Start node and get path to goal */
search_bf(Start, Goal) :-
    bfs([[Start]], Goal).

/* Base case: Goal found, path is printed */
bfs([[Goal|RestPath] | _], Goal) :-
    reverse([Goal|RestPath], Path),
    write('Goal Found: '), nl,
    write('Path: '), write(Path), nl.

/* Recursive case: expand front node's children and continue */
bfs([[Current|RestPath] | OtherPaths], Goal) :-
    findall([Child,Current|RestPath],
            (children(Current, Children),
             member(Child, Children),
             \+ member(Child, [Current|RestPath])  % Avoid cycles
            ),
            NewPaths),
    append(OtherPaths, NewPaths, UpdatedQueue),
    bfs(UpdatedQueue, Goal).

/* Define Graph */
children(a,[b,c]).
children(b,[d,e]).
children(c,[]).
children(d,[]).
children(e,[]).

/* Define goal(s) */
goal(e).
goal(f).
