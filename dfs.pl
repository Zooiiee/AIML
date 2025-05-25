/* Graph Representation */
children(a, [b, c]).
children(b, [d, e]).
children(c, []).
children(d, []).
children(e, []).

/* Define goal node(s) */
goal(e).

/* Entry point for DFS */
search_df(Start) :-
    dfs([Start], Path),
    write('Goal Found: '), nl,
    reverse(Path, CorrectOrder),
    write('Path: '), write(CorrectOrder), nl.

/* Base case: if current node is goal */
dfs([Node | Rest], [Node | Rest]) :-
    goal(Node).

/* Recursive DFS exploration */
dfs([Node | RestPath], FinalPath) :-
    children(Node, Children),
    member(Child, Children),
    \+ member(Child, [Node | RestPath]),  % Prevent cycles
    dfs([Child, Node | RestPath], FinalPath).
