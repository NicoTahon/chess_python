class Chess :
    def __init__ (self):
        self.board=[]
        self.board.append([" ","A","B","C","D","E","F","G","H"])
        for i in range (1, 9):
            self.ligne=[f"{i}"]
            for j in range (8):
                self.ligne.append("_")
            self.board.append(self.ligne)
        self.lettre={"A":1,"B":2, "C":3,"D":4,"E":5,"F":6,"G":7,"H":8}
        self.chiffre={"1":1,"2": 2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8}

    def placement (self):
        for i in range (1, 9):
            self.board[7][i]="♙"
        for i in range (1, 9):
            self.board[2][i]="♟"
        self.board[1][1]="♜"
        self.board[1][2]="♞"
        self.board[1][3]="♝"
        self.board[1][4]="♛"
        self.board[1][5]="♚"
        self.board[1][6]="♝"
        self.board[1][7]="♞"
        self.board[1][8]="♜"

        self.board[8][1]="♖"
        self.board[8][2]="♘"
        self.board[8][3]="♗"
        self.board[8][4]="♕"
        self.board[8][5]="♔"
        self.board[8][6]="♗"
        self.board[8][7]="♘"
        self.board[8][8]="♖"
        

    def affiche (self):
        print("\n")
        for ligne in self.board:
            ligne_str = ""
            for case in ligne:
                ligne_str=ligne_str + case + " "
            print (ligne_str)
        print("\n")


def main():
    plateau=Chess()
    plateau.placement()
    plateau.affiche()

main ()