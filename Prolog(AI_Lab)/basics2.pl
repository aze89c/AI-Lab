
%check with fact 
 
/*

 Tom is a cat 
 Kunal loves to eat Pasta 
 Hair is black 
 Nawaz loves to play games 
 Pratyusha is lazy. 

*/

 
%PROGRAM 
cat(tom). 
loves_to_eat(kunal,pasta). 
of_color(hair,black). 
loves_to_play_games(nawaz). 
lazy(pratyusha).


/*
OUTPUT

GNU Prolog 1.5.0 (64 bits)
Compiled Jul  8 2021, 12:22:53 with gcc
Copyright (C) 1999-2021 Daniel Diaz

| ?- change_directory('C:/Users/azizb/OneDrive/Desktop/Prolog(AI_Lab)').

yes
| ?- [basics2].
compiling C:/Users/azizb/OneDrive/Desktop/Prolog(AI_Lab)/basics2.pl for byte code...
C:/Users/azizb/OneDrive/Desktop/Prolog(AI_Lab)/basics2.pl compiled, 19 lines read - 875 bytes written, 9 ms

yes
| ?- of_color(hair,blonde). 

no
| ?- of_color(hair,black). 

yes
| ?- loves_to_eat(kunal,pasta).

yes
| ?- loves_to_eat(kunal,pizza).

no
| ?- loves_to_play_games(nawaz). 

yes
| ?- loves_to_eat(kunal,nawaz).

no
| ?- lazy(pratyusha), cat(tom).

yes
| ?- lazy(tom), cat(pratyusha).

no

*/