import collections

class Trump:
    def __init__(self, mark, num):
        self.mark = mark
        self.num = num

class Check_flag:
    def is_flush(self, cards):
        return all( i["mark"] == cards[0]["mark"] for i in cards)

    def is_straight(self, cards):
        values = [i["num"] for i in cards]
        straight = (values == list(range(values[0], values[0]-5, -1) ) or values == [14, 5, 4, 3, 2])
        return straight    

class Porker:

    def ans_print(self, card_list, role):
        ans = ""
        for i in card_list:
            if 0 is i["mark"]:
                ans = ans + "S"
            elif 1 is i["mark"]:
                ans = ans + "C"
            elif 2 is i["mark"]:
                ans = ans + "D"
            elif 3 is i["mark"]:
                ans = ans + "H"

            if 14 is i["num"]:
                ans = ans + "A"
            elif 13 is i["num"]:
                ans = ans + "K"
            elif 12 is i["num"]:
                ans = ans + "Q"
            elif 11 is i["num"]:
                ans = ans + "J"
            else:
                ans = ans + str(i["num"])
            ans = ans + " "
        print(ans)
        print(role)
        exit()

    def judgment_role(self, card_list_input):
        card_list = sorted(card_list_input, key = lambda x : x["num"], reverse= True)

        straight = Check_flag().is_straight(card_list)
        flush = Check_flag().is_flush(card_list)

        if flush and \
            card_list[0]["num"] is 14 and \
            card_list[1]["num"] is 13 and \
            card_list[2]["num"] is 12 and \
            card_list[3]["num"] is 11 and \
            card_list[4]["num"] is 10 :
                self.ans_print(card_list_input, "ロイヤルストレートフラッシュ")
        if straight and flush:
            self.ans_print(card_list_input, "ストレートフラッシュ")

        c = collections.Counter( [i["num"] for i in card_list]  )
        
        if c.most_common()[0][1] is 4:
            self.ans_print(card_list_input, "フォーカード")
        elif c.most_common()[0][1] is 3 and \
            c.most_common()[1][1] is 2 : 
            self.ans_print(card_list_input, "フルハウス")

        if flush :
            self.ans_print(card_list_input, "フラッシュ")

        if straight :
            self.ans_print(card_list_input, "ストレート")

        if c.most_common()[0][1] is 3 :
            self.ans_print(card_list_input, "スリーカード")

        if c.most_common()[0][1] is 2 and \
            c.most_common()[1][1] is 2 : 
            self.ans_print(card_list_input, "ツーペア")

        if c.most_common()[0][1] is 2 :
            self.ans_print(card_list_input, "ワンペア")

        self.ans_print(card_list_input, "ハイカード")
