import cal2_function as cal2
import copy

def result_to_valid(result, now):
    valid_headless = [0] * 11
    valid_head = [0] * 11
    valid_only_head = [0] * 11
    for re in result:
        now_copy = copy.deepcopy(now)
        for num in re["sum"]:
            for num2 in num:
                now_copy[int(num2)] += -1
        
        swi = False
        for i in range(1, 10):
            if now_copy[i] < 0:
                swi = True
        if swi:
            continue
        
        for i in range(1, 11):
            now_copy2 = copy.deepcopy(now_copy)
            now_copy2[i] += 1
            copy_result = cal2.cal_result_headless(now_copy2)
            if copy_result[0]["sum"] == []:
                pass
            else:
                valid_headless[i] = i
            copy_result = cal2.cal_result(now_copy2)
            if copy_result[0]["sum"] == []:
                pass
            else:
                valid_head[i] = i
            
    # print("headless:")
    # print(valid_headless)
    # print("plus head")
    # print(valid_head)

    for i in range(0, 11):
        valid_only_head[i] = valid_head[i] - valid_headless[i]

    # print("only head")
    # print(valid_only_head)
    body_head_num = cal2.cal_result(now)[0]["body_head_num"]
    new_obj = {"plus_head":valid_head, "headless":valid_headless, "only_head":valid_only_head, "body_head_num":body_head_num}
    return new_obj