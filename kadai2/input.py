from main import Porker

card_list_input = []
for _ in range(5):
    mark, num = map(int,input().split())
    if num == 1:
        num = 14
    card_list_input.append({"num": num , "mark": mark})
Porker().judgment_role(card_list_input)