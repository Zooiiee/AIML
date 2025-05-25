% --- 8-Puzzle Hill Climbing ---

% Goal state definition
goal_state([1,2,3,4,5,6,7,8,0]).

% Heuristic: number of misplaced tiles (excluding blank)
heuristic(State, H) :-
    goal_state(Goal),
    misplaced_tiles(State, Goal, H).

misplaced_tiles([], [], 0).
misplaced_tiles([0|T1], [_|T2], H) :- % ignore blank
    misplaced_tiles(T1, T2, H).
misplaced_tiles([X|T1], [X|T2], H) :- % correct tile
    misplaced_tiles(T1, T2, H).
misplaced_tiles([X|T1], [Y|T2], H) :-
    X \= 0,
    X \= Y,
    misplaced_tiles(T1, T2, H1),
    H is H1 + 1.

% Moves: up, down, left, right - slide blank tile

% Index positions are 0-based: positions 0..8 in the list

move(State, NextState) :-
    nth0(BlankPos, State, 0),
    swap(BlankPos, SwapPos),
    valid_swap(BlankPos, SwapPos),
    swap_elements(State, BlankPos, SwapPos, NextState).

% Swap rules based on positions:

% Moves: Up (pos - 3), Down (pos +3), Left (pos -1), Right (pos +1)
swap(BlankPos, SwapPos) :-
    SwapPos is BlankPos - 3;  % Up
    SwapPos is BlankPos + 3;  % Down
    SwapPos is BlankPos - 1;  % Left
    SwapPos is BlankPos + 1.  % Right

% Validate moves (to prevent wraparound)
valid_swap(BlankPos, SwapPos) :-
    SwapPos >= 0,
    SwapPos < 9,
    % Prevent illegal left/right moves across rows
    RowBlank is BlankPos // 3,
    RowSwap is SwapPos // 3,
    (RowBlank =:= RowSwap ; abs(BlankPos - SwapPos) =:= 3).

% Swap elements in list at two positions
swap_elements(List, I, J, Result) :-
    nth0(I, List, ElemI),
    nth0(J, List, ElemJ),
    set_nth0(List, I, ElemJ, Temp),
    set_nth0(Temp, J, ElemI, Result).

% Replace Nth element of list
set_nth0([_|T], 0, X, [X|T]).
set_nth0([H|T], N, X, [H|R]) :-
    N > 0,
    N1 is N - 1,
    set_nth0(T, N1, X, R).

% Hill Climbing search
hill_climb(State, Path) :-
    heuristic(State, H),
    hill_climb(State, H, [State], Path).

hill_climb(State, 0, Path, Path) :- % reached goal
    !.

hill_climb(State, H, Visited, Path) :-
    findall(NextState,
            (move(State, NextState),
             \+ member(NextState, Visited)),
            NextStates),
    evaluate_and_choose(NextStates, H, BestNext, BestH),
    (BestH < H ->
        hill_climb(BestNext, BestH, [BestNext|Visited], Path)
    ;
        % No better neighbor: stuck at local maxima
        reverse(Visited, Path)
    ).

% Evaluate all next states, select the one with minimum heuristic
evaluate_and_choose([S], _, S, H) :-
    heuristic(S, H).
evaluate_and_choose([S|Ss], CurrentH, BestState, BestH) :-
    heuristic(S, H1),
    evaluate_and_choose(Ss, CurrentH, S2, H2),
    (H1 < H2 -> (BestState = S, BestH = H1) ; (BestState = S2, BestH = H2)).

evaluate_and_choose([], H, _, H) :- fail.

% Utility to print states nicely (optional)
print_state(State) :-
    print_rows(State, 0).

print_rows(_, 9).
print_rows(State, N) :-
    N < 9,
    nth0(N, State, Val),
    (Val =:= 0 -> write('  ') ; write(Val), write(' ')),
    N1 is N + 1,
    (N1 mod 3 =:= 0 -> nl ; true),
    print_rows(State, N1).

% Sample run example
solve(Start) :-
    hill_climb(Start, Path),
    print_solution(Path).

print_solution([]).
print_solution([H|T]) :-
    print_state(H), nl,
    print_solution(T).

%to solve - ['hillclimb.pl']. ; solve([1,2,3,4,0,6,7,5,8]).
