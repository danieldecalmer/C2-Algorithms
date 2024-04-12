import math

def fold_punch_card(R, C, Y, punch_card):
    folded_card = [""] * R
    left_side = ""
    temp = ""
    right_side_flipped = ""

    print("--------")

    if (C / Y != 2):
            
        

            
            if (Y < (C / 2)):
                for i in range(R):
                    #Splitting into two sides
                    left_side = punch_card[i][:Y]
                    temp = punch_card[i][Y:]

                    # Flipping the right side
                    right_side_flipped = temp[::-1]
                    # Use the right-side-flipped
                    num = int(C/Y)
                    print("iiiiiiiiii")
                    print(left_side)
                    print(right_side_flipped)
                    print("iiiiiiiiii")
                    folded_card[i] = right_side_flipped[num:] + folded_card[i]
                    print("rtsdflipb4: ",right_side_flipped)
                    right_side_flipped = right_side_flipped[num-1:]
                    print("rtsdflipafter: ",right_side_flipped)
                    print("folded_card: ",folded_card[i])

                    print("mmmmmmmmmm")
                    print(left_side)
                    print(right_side_flipped)
                    print("mmmmmmmmmm")
                    for j in range(int((C / 2))):
                        if left_side[j] == 'o' and right_side_flipped[j] == 'o':
                            folded_card[i] = folded_card[i] + 'o'
                            print("after comparison(o): ", folded_card[i])
                        else:
                            folded_card[i] = folded_card[i] + 'x'
                            print("after comparison(x): ", folded_card[i])

            else:
                for i in range(R):
                    #Splitting into two sides
                    left_side = punch_card[i][:Y]
                    temp = punch_card[i][Y:]

                    # Flipping the right side
                    right_side_flipped = temp[::-1]
                    # Use the left-side
                    num = int(math.sqrt(Y))
                    folded_card[i] = left_side[:num] + folded_card[i]
                    left_side = left_side[num:]
                    print("mmmmmmmmmm")
                    print(left_side)
                    print(right_side_flipped)
                    print("mmmmmmmmmm")
                    for j in range(int((C / 2))):
                        if left_side[j] == 'o' and right_side_flipped[j] == 'o':
                            folded_card[i] = folded_card[i] + 'o'
                            print("after comparison(o): ", folded_card[i])
                        else:
                            folded_card[i] = folded_card[i] + 'x'
                            print("after comparison(x): ", folded_card[i])

            print(folded_card[i])

    else:
        for i in range(R):
            #Splitting into two sides
            left_side = punch_card[i][:Y]
            temp = punch_card[i][Y:]

            # Flipping the right side
            right_side_flipped = temp[::-1]
            print("mmmmmmmmmm")
            print(left_side)
            print(right_side_flipped)
            print("mmmmmmmmmm")
            # Comparison starting from leftmost character
            for j in range(int(C / 2)):
                if left_side[j] == 'o' and right_side_flipped[j] == 'o':
                    folded_card[i] = folded_card[i] + 'o'
                    print("after comparison(o): ", folded_card[i])
                else:
                    folded_card[i] = folded_card[i] + 'x'
                    print("after comparison(x): ", folded_card[i])
            print(folded_card[i])
    print("--------")

    return folded_card

R, C, Y = map(int, input().split())
punch_card = [input() for _ in range(R)]

folded_card = fold_punch_card(R, C, Y, punch_card)
print("")
for i in range(R):
    print(folded_card[i])
