x = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
player_input = 0
eternal = 0
Turncounter = 0
game_over = False


def function(Variabel):
    
    if Turncounter%2 == 0: 
        if player_input == 1:
            Variabel[0][0] = "x"
        elif player_input == 2:
            Variabel[0][1] = "x"
        elif player_input == 3:
            Variabel[0][2] = "x"
        elif player_input == 4:
            Variabel[1][0] = "x"
        elif player_input == 5:
            Variabel[1][1] = "x"
        elif player_input == 6:
            Variabel[1][2] = "x"
        elif player_input == 7:
            Variabel[2][0] = "x"
        elif player_input == 8:
            Variabel[2][1] = "x"
        elif player_input == 9:
            Variabel[2][2] = "x"

    else:
        if player_input == 1:
            Variabel[0][0] = "o"
        elif player_input == 2:
            Variabel[0][1] = "o"
        elif player_input == 3:
            Variabel[0][2] = "o"
        elif player_input == 4:
            Variabel[1][0] = "o"
        elif player_input == 5:
            Variabel[1][1] = "o"
        elif player_input == 6:
            Variabel[1][2] = "o"
        elif player_input == 7:
            Variabel[2][0] = "o"
        elif player_input == 8:
            Variabel[2][1] = "o"
        elif player_input == 9:
            Variabel[2][2] = "o"
    
    print( "",x[0][0], "|", x[0][1], "|", x[0][2])
    print("___________")
    print("", x[1][0], "|", x[1][1], "|", x[1][2] )
    print("___________")
    print("", x[2][0], "|", x[2][1], "|", x[2][2] )

    #for row in x:
    #    print(" | ".join(row))
if game_over == False:
    while eternal == 0:
        if player_input > 0:
            Turncounter += 1
        function(x)

        if Turncounter%2 == 0: 
            print("Player 1")
            player_input = int(input("Välj ruta med siffra "))
        else:
            print("Player 2")
            player_input = int(input("Välj ruta med siffra "))

    
   

    


    if (x[0][0] == "o") and (x[0][1] == "o") and (x[0][2] == "o"):
        print("Player_1 wins")
        game_over = True
    
        
    #if ((x[0][0] and x[0][1] and x[0][2]) or (x[1][0] and x[1][1] and x[1][2]) or (x[2][0] and x[2][1] and x[2][2]) or (x[0][0] and x[1][0] and x[2][0]) or (x[2][0] and x[2][1] and x[2][2]) or (x[0][1] and x[1][1] and x[2][1]) or (x[0][2] and x[1][2] and x[2][2]) or (x[0][0] and x[1][1] and x[2][2]) or (x[0][2] and x[1][1] and [2][0])) == "o":
     #   print("Player_1 wins")
      #  break
    #elif (x[0][0] and x[0][1] and x[0][2]) or (x[1][0] and x[1][1] and x[1][2]) or (x[2][0] and x[2][1] and x[2][2]) == "x":
     #   print("Player_2 wins")
      #  break