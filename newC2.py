def row_trim (C, Y, row):
    if (C/Y == 2):
        return [[], row]
    if (C/2 < Y):
        excess = row[:C-2*Y]
        sym_row = row[C-2*Y:]
        return [excess, sym_row]
    else: 
        excess = row[2*Y:]
        flipped_excess = excess[::-1]
        sym_row = row[:2*Y]
        return [flipped_excess, sym_row]

def book_solver (sym_row):
    solved_sym_row = ""
    fold = int(len(sym_row) / 2)

    left_side = sym_row[:fold]
    temp = sym_row[fold:]
    right_side_flipped = temp[::-1]

    for j in range(fold):
        if left_side[j] == 'o' and right_side_flipped[j] == 'o':
            solved_sym_row = solved_sym_row + 'o'
        else:
            solved_sym_row = solved_sym_row + 'x'
    return solved_sym_row

def card_solver (R, C, Y, punch_card):
    print("")
    print("Folded: ")
    for i in range(R):
        row = punch_card[i]
        row_trim_result = row_trim(C, Y, row)
        solved_sym_row = book_solver(row_trim_result[1])
        row = row_trim_result[0] + solved_sym_row
        print(row)
    print("")
        
R, C, Y = map(int, input().split())
punch_card = [input() for _ in range(R)]

card_solver(R, C, Y, punch_card)