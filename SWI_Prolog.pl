% SWI-Prolog Tasks 

% --- Task 1: Double Happiness ---
happy(alice).
happy(bob).
friends(alice, bob).
friends(charlie, alice).

doubleHappy(X) :-
    happy(X),
    (friends(X, Y); friends(Y, X)),
    happy(Y).

% --- Task 2: Sibling Finder ---
parent(john, mary).
parent(john, tom).
parent(susan, mary).
parent(susan, tom).

% --- Task 3: Chain of Command ---
manages(alice, bob).
manages(bob, charlie).
manages(charlie, david).

hasAuthority(X, Y) :- manages(X, Y).
hasAuthority(X, Y) :-
    manages(X, Z),
    hasAuthority(Z, Y).

% --- Task 4: Even Number Checker (Peano) ---
isEven(0).
isEven(succ(succ(X))) :- isEven(X).

% --- Task 5: Path Length ---
directTrain(nancy, metz).
directTrain(metz, fahlquemont).
directTrain(fahlquemont, stAvold).
directTrain(stAvold, freyming).
directTrain(freyming, forbach).
directTrain(forbach, saarbruecken).

pathLength(Start, End, succ(0)) :-
    directTrain(Start, End).
pathLength(Start, End, succ(N)) :-
    directTrain(Start, Mid),
    pathLength(Mid, End, N).

% --- Task 6: Food Preference Logic ---
vegetarian(alice).
eats(bob, meat).
eats(alice, vegetables).
eats(charlie, vegetables).

% --- Task 7: List Sum (Peano) ---
% NOTE: Unsolvable. The manual does not introduce list
% syntax like [] or [H|T].

% --- Task 8: Reverse Ancestry ---
child(bob, alice).
child(charlie, bob).

ancestor(X, Y) :- child(Y, X).
ancestor(X, Y) :-
    child(Z, X),
    ancestor(Z, Y).

generation(X, Y, succ(0)) :-
    child(Y, X).
generation(X, Y, succ(N)) :-
    child(Z, X),
    generation(Z, Y, N).

% --- Task 9: Tree Depth ---
% Peano addition 
add(0, Y, Y).
add(succ(X), Y, succ(Z)) :- add(X, Y, Z).
greater_than(succ(_), 0).
greater_than(succ(X), succ(Y)) :- greater_than(X, Y).

% --- Task 10: Safe Combination ---
validCombo(X, Y, Z) :-
    add(X, Y, Z),
    greater_than(X, 0),
    greater_than(Y, 0).