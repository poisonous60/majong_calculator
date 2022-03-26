import cal1_function as cal1
import copy

def cal_result(now):
    # now = [0] * 12
    pin = 0 #체크 시작하는 인덱스
    step = 0 #0 : 슌쯔 체크, 1 : 커쯔 체크, 2 : 또이 체크
    sum = []
    stack = []
    result = []
    body_head_num = [0] * 3 #[0] = 슌쯔 개수, [1] = 커쯔 개수, [2] = 또이 개수
    obj = {"now":copy.deepcopy(now), "pin":copy.deepcopy(pin), "sum":copy.deepcopy(sum) \
        , "step":copy.deepcopy(step), "body_head_num":copy.deepcopy(body_head_num)}

    stack.append(obj)

    while len(stack)!=0:
        now_obj = stack.pop()
        if now_obj["step"]==0:
            i = now_obj["pin"]
            while i < 11:
                if cal1.check_123(now_obj["now"], i):
                    new_obj = {"now":copy.deepcopy(now_obj["now"]), "pin":i+1, "sum":copy.deepcopy(now_obj["sum"]), \
                        "step":copy.deepcopy(now_obj["step"]), "body_head_num":copy.deepcopy(now_obj["body_head_num"])}
                    stack.append(new_obj)
                    label = ""
                    label += str(i)
                    label += str(i+1)
                    label += str(i+2)
                    now_obj["sum"].append(label)
                    now_obj["now"][i] += -1
                    now_obj["now"][i+1] += -1
                    now_obj["now"][i+2] += -1
                    now_obj["body_head_num"][0] += 1
                    i += -1
                i += 1
            now_obj["step"] += 1
            now_obj["pin"] = 0
        
        if now_obj["step"]==1:
            i = now_obj["pin"]
            while i < 11:
                if cal1.check_444(now_obj["now"], i):
                    new_obj = {"now":copy.deepcopy(now_obj["now"]), "pin":i+1, "sum":copy.deepcopy(now_obj["sum"]), \
                        "step":copy.deepcopy(now_obj["step"]), "body_head_num":copy.deepcopy(now_obj["body_head_num"])}
                    stack.append(new_obj)
                    label = ""
                    label += str(i)
                    label += str(i)
                    label += str(i)
                    now_obj["sum"].append(label)
                    now_obj["now"][i] += -3
                    now_obj["body_head_num"][1] += 1
                    i += -1
                i += 1
            now_obj["step"] += 1
            now_obj["pin"] = 0
        
        if now_obj["step"]==2:
            i = now_obj["pin"]
            while i < 11:
                if cal1.check_55(now_obj["now"], i):
                    new_obj = {"now":copy.deepcopy(now_obj["now"]), "pin":i+1, "sum":copy.deepcopy(now_obj["sum"]), \
                        "step":copy.deepcopy(now_obj["step"]), "body_head_num":copy.deepcopy(now_obj["body_head_num"])}
                    stack.append(new_obj)
                    label = ""
                    label += str(i)
                    label += str(i)
                    now_obj["sum"].append(label)
                    now_obj["now"][i] += -2
                    now_obj["body_head_num"][2] += 1
                    i += -1
                i += 1
            now_obj["step"] += 1
            now_obj["pin"] = 0
        
        result.append(now_obj)

    max_num = 0
    for re in result:
        temp_num = cal1.cal_max_num(re["body_head_num"])
        # temp_num = 0
        # temp_num += re["body_head_num"][0]
        # temp_num += re["body_head_num"][1]
        # if re["body_head_num"][2] > 0:
        #     temp_num += 0.5
        if temp_num > max_num:
            max_num = temp_num

    result2 = copy.deepcopy(result)
    for re in result2:
        temp_num = cal1.cal_max_num(re["body_head_num"])
        # temp_num = 0
        # temp_num += re["body_head_num"][0]
        # temp_num += re["body_head_num"][1]
        # if re["body_head_num"][2] > 0:
        #     temp_num += 0.5
        if temp_num < max_num or re["body_head_num"][2] > 1:
            result.remove(re)

    if result == []:
        result.append({"now":copy.deepcopy(now), "pin":copy.deepcopy(pin), "sum":copy.deepcopy(sum) \
        , "step":copy.deepcopy(step), "body_head_num":copy.deepcopy(body_head_num)})
    
    return result




def cal_result_headless(now):
    # now = [0] * 12
    pin = 0 #체크 시작하는 인덱스
    step = 0 #0 : 슌쯔 체크, 1 : 커쯔 체크, 2 : 또이 체크
    sum = []
    stack = []
    result = []
    body_head_num = [0] * 3 #[0] = 슌쯔 개수, [1] = 커쯔 개수, [2] = 또이 개수
    obj = {"now":copy.deepcopy(now), "pin":copy.deepcopy(pin), "sum":copy.deepcopy(sum) \
        , "step":copy.deepcopy(step), "body_head_num":copy.deepcopy(body_head_num)}

    stack.append(obj)

    while len(stack)!=0:
        now_obj = stack.pop()
        if now_obj["step"]==0:
            i = now_obj["pin"]
            while i < 11:
                if cal1.check_123(now_obj["now"], i):
                    new_obj = {"now":copy.deepcopy(now_obj["now"]), "pin":i+1, "sum":copy.deepcopy(now_obj["sum"]), \
                        "step":copy.deepcopy(now_obj["step"]), "body_head_num":copy.deepcopy(now_obj["body_head_num"])}
                    stack.append(new_obj)
                    label = ""
                    label += str(i)
                    label += str(i+1)
                    label += str(i+2)
                    now_obj["sum"].append(label)
                    now_obj["now"][i] += -1
                    now_obj["now"][i+1] += -1
                    now_obj["now"][i+2] += -1
                    now_obj["body_head_num"][0] += 1
                    i += -1
                i += 1
            now_obj["step"] += 1
            now_obj["pin"] = 0
        
        if now_obj["step"]==1:
            i = now_obj["pin"]
            while i < 11:
                if cal1.check_444(now_obj["now"], i):
                    new_obj = {"now":copy.deepcopy(now_obj["now"]), "pin":i+1, "sum":copy.deepcopy(now_obj["sum"]), \
                        "step":copy.deepcopy(now_obj["step"]), "body_head_num":copy.deepcopy(now_obj["body_head_num"])}
                    stack.append(new_obj)
                    label = ""
                    label += str(i)
                    label += str(i)
                    label += str(i)
                    now_obj["sum"].append(label)
                    now_obj["now"][i] += -3
                    now_obj["body_head_num"][1] += 1
                    i += -1
                i += 1
            now_obj["step"] += 1
            now_obj["pin"] = 0
        
        if now_obj["step"]==2:
            i = now_obj["pin"]
            while i < 11:
                if cal1.check_55(now_obj["now"], i):
                    new_obj = {"now":copy.deepcopy(now_obj["now"]), "pin":i+1, "sum":copy.deepcopy(now_obj["sum"]), \
                        "step":copy.deepcopy(now_obj["step"]), "body_head_num":copy.deepcopy(now_obj["body_head_num"])}
                    stack.append(new_obj)
                    label = ""
                    label += str(i)
                    label += str(i)
                    now_obj["sum"].append(label)
                    now_obj["now"][i] += -2
                    now_obj["body_head_num"][2] += 1
                    i += -1
                i += 1
            now_obj["step"] += 1
            now_obj["pin"] = 0
        
        result.append(now_obj)

    max_num = 0
    for re in result:
        temp_num = 0
        temp_num += re["body_head_num"][0]
        temp_num += re["body_head_num"][1]
        if temp_num > max_num:
            max_num = temp_num

    result2 = copy.deepcopy(result)
    for re in result2:
        temp_num = temp_num = cal1.cal_max_num(re["body_head_num"])
        # temp_num = 0
        # temp_num += re["body_head_num"][0]
        # temp_num += re["body_head_num"][1]
        if temp_num < max_num or (re["body_head_num"][0] == 0 and re["body_head_num"][1] == 0) or re["body_head_num"][2] > 0:
            result.remove(re)

    if result == []:
        result.append({"now":copy.deepcopy(now), "pin":copy.deepcopy(pin), "sum":copy.deepcopy(sum) \
        , "step":copy.deepcopy(step), "body_head_num":copy.deepcopy(body_head_num)})
        
    return result