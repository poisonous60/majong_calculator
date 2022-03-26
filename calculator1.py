from numpy import empty
import cal1_function as cal1
import cal2_function as cal2
import cal3_function as cal3
import copy

now = [0] * 12

input1 = input()
for num in input1:
    now[int(num)] += 1

result = cal2.cal_result(now)
for re in result:
    print(re["sum"])

valid_obj = cal3.result_to_valid(result, now)
valid_headless = valid_obj["headless"]
valid_head = valid_obj["plus_head"]
valid_only_head = valid_obj["only_head"]
print("headless:")
print(valid_headless)
print("plus head")
print(valid_head)
print("only head")
print(valid_only_head)
print("body_head_num")
print(valid_obj["body_head_num"])


change_stack = []
change_good_stack = []
change_still_stack = []
for draw in range(1, 10):
    for drop in range(1, 10):
        now_copy = copy.deepcopy(now)
        if now_copy[drop] == 0:
            pass
        else:
            now_copy[drop] += -1
            now_copy[draw] += 1
            change_valid_obj = cal3.result_to_valid(result, now_copy)
            change_valid_headless = copy.deepcopy(change_valid_obj["headless"])
            change_valid_head = copy.deepcopy(change_valid_obj["plus_head"])
            change_valid_only_head = copy.deepcopy(change_valid_obj["only_head"])
            for i in range(1, 11):
                change_valid_head[i] += -valid_head[i]
                change_valid_headless[i] += -valid_headless[i]
                change_valid_only_head[i] += -valid_only_head[i]
                change_body_head_num = 0
            
            #후리텐인 유효패 제거
            if change_valid_headless[drop] == drop:
                change_valid_headless[0] = "후리텐"
                change_valid_headless[drop] = -99
            if change_valid_head[drop] == drop:
                change_valid_head[0] = "후리텐"
                change_valid_head[drop] = -99
                
            label = "DRAW " + str(draw) +" / DROP " + str(drop)
            new_obj = {"NAME":label, "draw":draw, "drop":drop, "change_valid_head":copy.deepcopy(change_valid_head), \
                "change_valid_headless":copy.deepcopy(change_valid_headless), "change_valid_only_head":copy.deepcopy(change_valid_only_head) \
                    , "body_head_num":copy.deepcopy(change_valid_obj["body_head_num"])}
            change_stack.append(new_obj)

max_num = 0
max_num += result[0]["body_head_num"][0]
max_num += result[0]["body_head_num"][1]
if result[0]["body_head_num"][1] > 0:
    max_num += 1

for elem in copy.deepcopy(change_stack):
    temp_num = 0
    temp_num += elem["body_head_num"][0]
    temp_num += elem["body_head_num"][1]
    if elem["body_head_num"][1] > 0:
        temp_num += 1
    if temp_num < max_num:
        change_stack.remove(elem)

for elem in change_stack:
    if elem["change_valid_headless"][0] == 0:
        temp_num = 0
        for i in range(1, 10):
            if elem["change_valid_headless"][i] > 0:
                temp_num += 1
            elif elem["change_valid_headless"][i] < 0:
                temp_num += -1
        if temp_num > 0:
            change_good_stack.append(elem)
        else:
            temp_num = 0
            if elem["change_valid_head"][i] > 0:
                temp_num += 1
            elif elem["change_valid_head"][i] < 0:
                temp_num += -1
            if temp_num > 0:
                change_good_stack.append(elem)
                
for elem in change_good_stack:
    print("NAME:"+elem["NAME"]+", CVHless:"+str(elem["change_valid_headless"])+", CVH:"+str(elem["change_valid_head"])+", num:"+str(elem["body_head_num"]))