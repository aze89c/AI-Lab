 
% FAMILY TREE 
% CHECK GRANDFATHER RELATIONSHIP 
%CHECK UNCLE RELATIONSHIP 
%CHECK COUSIN RELATIONSHIP 
 
%facts(Father of) 
father(ahmed,wali). 
father(ahmed,moin). 
father(wali,raza). 
father(wali,saad). 
father(wali,sazzad). 
father(moin,salman). 
father(moin,sultan). 


%facts(Siblings of) 
sibling(wali,moin). 
sibling(moin,wali). 
sibling(raza,saad). 
sibling(saad,raza). 
sibling(raza,sazzad). 
sibling(sazzad,raza). 
sibling(saad,sazzad). 

sibling(sazzad,saad). 
sibling(salman,sultan). 
sibling(sultan,salman). 
 

%rules
 
grandfather(X,Y) :- 
father(X,Z) , father(Z,Y). 
 
uncle(B,A) :- 
father(X,A) ,sibling( X,B). /*father(B,Y) can be added as an unnecessary rule accoordung to the given facts but it implies that an uncle must be a father that might cause unexpected tracebacks when our data increases */
 
cousin(X,Y) :- 
father(M,X) , father(N,Y) , sibling(M,N).

/*

OUTPUT

GNU Prolog 1.5.0 (64 bits)
Compiled Jul  8 2021, 12:22:53 with gcc
Copyright (C) 1999-2021 Daniel Diaz

| ?- change_directory('C:/Users/azizb/OneDrive/Desktop/Prolog(AI_Lab)').

yes
| ?- [familytree].
compiling C:/Users/azizb/OneDrive/Desktop/Prolog(AI_Lab)/familytree.pl for byte code...
C:/Users/azizb/OneDrive/Desktop/Prolog(AI_Lab)/familytree.pl compiled, 46 lines read - 2888 bytes written, 5 ms

yes
| ?- grandfather(X,Y).

X = ahmed
Y = raza ? 

yes
| ?- grandfather(X,Y).

X = ahmed
Y = raza ? ;

X = ahmed
Y = saad ? ;

X = ahmed
Y = sazzad ? ;

X = ahmed
Y = salman ? ;

X = ahmed
Y = sultan ? ;

no
| ?- grandfather(X,Y), uncle(B,A),cousin(X,Y).

no
| ?- uncle(B,A).

A = raza
B = moin ? ;

A = saad
B = moin ? ;

A = sazzad
B = moin ? ;

A = salman
B = wali ? ;

A = sultan
B = wali

yes
| ?- cousin(X,Y).

X = raza
Y = salman ? ;

X = raza
Y = sultan ? ;

X = saad
Y = salman ? ;

X = saad
Y = sultan ? ;

X = sazzad
Y = salman ? ;

X = sazzad
Y = sultan ? ;

X = salman
Y = raza ? ;

X = salman
Y = saad ? ;

X = salman
Y = sazzad ? ;

X = sultan
Y = raza ? ;

X = sultan
Y = saad ? ;

X = sultan
Y = sazzad ? ;

no
| ?- uncle(B,A),cousin(X,Y).

A = raza
B = moin
X = raza
Y = salman ? ;

A = raza
B = moin
X = raza
Y = sultan ? ;

A = raza
B = moin
X = saad
Y = salman ? ;

A = raza
B = moin
X = saad
Y = sultan ? ;

A = raza
B = moin
X = sazzad
Y = salman ? ;

A = raza
B = moin
X = sazzad
Y = sultan ? ;

A = raza
B = moin
X = salman
Y = raza ? ;

A = raza
B = moin
X = salman
Y = saad ? ;

A = raza
B = moin
X = salman
Y = sazzad ? ;

A = raza
B = moin
X = sultan
Y = raza ? ;

A = raza
B = moin
X = sultan
Y = saad ? ;

A = raza
B = moin
X = sultan
Y = sazzad ? ;

A = saad
B = moin
X = raza
Y = salman ? ;

A = saad
B = moin
X = raza
Y = sultan ? ;

A = saad
B = moin
X = saad
Y = salman ? ;

A = saad
B = moin
X = saad
Y = sultan ? ;

A = saad
B = moin
X = sazzad
Y = salman ? ;

A = saad
B = moin
X = sazzad
Y = sultan ? ;

A = saad
B = moin
X = salman
Y = raza ? ;

A = saad
B = moin
X = salman
Y = saad ? ;

A = saad
B = moin
X = salman
Y = sazzad ? ;

A = saad
B = moin
X = sultan
Y = raza ? ;

A = saad
B = moin
X = sultan
Y = saad ? ;

A = saad
B = moin
X = sultan
Y = sazzad ? ;

A = sazzad
B = moin
X = raza
Y = salman ? ;

A = sazzad
B = moin
X = raza
Y = sultan ? ;

A = sazzad
B = moin
X = saad
Y = salman ? ;

A = sazzad
B = moin
X = saad
Y = sultan ? ;

A = sazzad
B = moin
X = sazzad
Y = salman ? ;

A = sazzad
B = moin
X = sazzad
Y = sultan ? ;

A = sazzad
B = moin
X = salman
Y = raza ? ;

A = sazzad
B = moin
X = salman
Y = saad ? ;

A = sazzad
B = moin
X = salman
Y = sazzad ? ;

A = sazzad
B = moin
X = sultan
Y = raza ? ;

A = sazzad
B = moin
X = sultan
Y = saad ? ;

A = sazzad
B = moin
X = sultan
Y = sazzad ? ;

A = salman
B = wali
X = raza
Y = salman ? ;

A = salman
B = wali
X = raza
Y = sultan ? ;

A = salman
B = wali
X = saad
Y = salman ? ;

A = salman
B = wali
X = saad
Y = sultan ? ;

A = salman
B = wali
X = sazzad
Y = salman ? ;

A = salman
B = wali
X = sazzad
Y = sultan ? ;

A = salman
B = wali
X = salman
Y = raza ? ;

A = salman
B = wali
X = salman
Y = saad ? ;

A = salman
B = wali
X = salman
Y = sazzad ? ;

A = salman
B = wali
X = sultan
Y = raza ? ;

A = salman
B = wali
X = sultan
Y = saad ? ;

A = salman
B = wali
X = sultan
Y = sazzad ? ;

A = sultan
B = wali
X = raza
Y = salman ? ;

A = sultan
B = wali
X = raza
Y = sultan ? ;

A = sultan
B = wali
X = saad
Y = salman ? ;

A = sultan
B = wali
X = saad
Y = sultan ? ;

A = sultan
B = wali
X = sazzad
Y = salman ? ;

A = sultan
B = wali
X = sazzad
Y = sultan ? ;

A = sultan
B = wali
X = salman
Y = raza ? ;

A = sultan
B = wali
X = salman
Y = saad ? ;

A = sultan
B = wali
X = salman
Y = sazzad ? ;

A = sultan
B = wali
X = sultan
Y = raza ? ;

A = sultan
B = wali
X = sultan
Y = saad ? ;

A = sultan
B = wali
X = sultan
Y = sazzad ? ;

no


*/