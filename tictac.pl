% --- Tic-Tac-Toe BFS solver ---

% Starting from a given state, find a sequence of moves leading to a win for Player.

% Example initial empty board:
initial_state([e,e,e,e,e,e,e,e,e]).

% Check if a player has won
win(Player, Board) :-
    lines(Lines),
    member(Line, Lines),
    maplist(position_filled_by(Player, Board), Line).

position_filled_by(Player, Board, Pos) :-
    nth0(Pos, Board, Player).

% All winning line positions (rows, columns, diagonals)
lines([
    [0,1,2], [3,4,5], [6,7,8], % rows
    [0,3,6], [1,4,7], [2,5,8], % cols
    [0,4,8], [2,4,6]           % diagonals
]).

% Check if board is full (no empty squares)
full_board(Board) :-
    \+ member(e, Board).

% Get opponent
opponent(x, o).
opponent(o, x).

% Generate successors for Player by placing Player's mark on an empty spot
successor(Board, Player, NextBoard) :-
    nth0(Pos, Board, e),
    set_nth0(Board, Pos, Player, NextBoard).

% Helper to set Nth element in list
set_nth0([_|T], 0, X, [X|T]).
set_nth0([H|T], N, X, [H|R]) :-
    N > 0,
    N1 is N - 1,
    set_nth0(T, N1, X, R).

% BFS search for a winning path for Player
bfs(Player, Path) :-
    initial_state(Start),
    bfs_search([(Start, [Start])], [], Player, Path).

% bfs_search(Queue, Visited, Player, Path)
bfs_search([(State, Path)|_], _, Player, Path) :-
    win(Player, State), !.  % Goal found: Player wins

bfs_search([(State, Path)|RestQueue], Visited, Player, FinalPath) :-
    findall(
        (NextState, [NextState|Path]),
        (successor(State, Player, NextState),
         \+ member(NextState, Visited)),
        NextStates),
    append(RestQueue, NextStates, NewQueue),
    bfs_search(NewQueue, [State|Visited], Player, FinalPath).

bfs_search([], _, _, _) :-
    write('No winning path found.'), nl,
    fail.

% Print the board nicely
print_board(Board) :-
    print_rows(Board, 0).

print_rows(_, 9).
print_rows(Board, N) :-
    N < 9,
    nth0(N, Board, Val),
    (Val = e -> write('. ') ; write(Val), write(' ')),
    N1 is N + 1,
    (N1 mod 3 =:= 0 -> nl ; true),
    print_rows(Board, N1).

% Print path from initial to winning state
print_path([]).
print_path([H|T]) :-
    print_board(H), nl,
    print_path(T).

% Helper predicate to run BFS and print solution path
solve_tictactoe(Player) :-
    bfs(Player, RevPath),
    reverse(RevPath, Path),
    print_path(Path).


%solve - solve_tictactoe(x).
