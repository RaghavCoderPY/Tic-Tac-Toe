from random import randint


moves = [
    "1", "2", "3",
    "4", "5", "6",
    "7", "8", "9",
]

def print_board(a: str = "1", b: str = "2", c: str = "3",
                d: str = "4", e: str = "5", f: str = "6", 
                g: str = "7", h: str = "8", i: str = "9",
                ):
    print(f"{a} | {b} | {c}")
    print("----------")
    print(f"{d} | {e} | {f}")
    print("----------")
    print(f"{g} | {h} | {i}")


def main():
    print_board()
    while True:
        try:
            user = int(input("Enter Number To Place: "))
        except ValueError:
            print("Only integers allowed")

        if user > 9:
            raise ValueError("Range: 1 - 9 allowed. Otherwise it cause error")

        robot = randint(1, 9)

        if (user == robot) and robot >= user:
            robot -= 1
        elif (user == robot) and robot <= user:
            robot += 1

        if (((moves[robot - 1]) == "O") and robot >= user) or (((moves[robot - 1]) == "X") and robot >= user):
            robot -= 1
        elif (((moves[robot - 1]) == "O") and robot <= user) or (((moves[robot - 1]) == "X") and robot <= user):
            robot += 1

        moves[user - 1] = "O"
        moves[robot - 1] = "X"


        print_board(
            moves[0], moves[1], moves[2],
            moves[3], moves[4], moves[5],
            moves[6], moves[7], moves[8],
                    )


if __name__ == "__main__":
    main()
