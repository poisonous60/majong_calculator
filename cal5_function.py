from numpy import empty
import cal1_function as cal1
import cal2_function as cal2
import cal4_function as cal4
import copy


def GUI_SHOW(user_input):
    output = ""
    now = [0] * 12
    input1 = user_input
    for num in input1:
        now[int(num)] += 1

    result = cal2.cal_result(now)
    for re in result:
        output += str(re["sum"])
        output += "\n"

    output += str("--------------------")
    output += "\n"
    output += str("head")
    output += "\n"
    result_head = cal2.cal_result(now)
    for elem in result_head:
        output += str(elem)
        output += "\n"
    output += str("--------------------")
    output += "\n"

    output += str("headless")
    output += "\n"
    result_headless = cal2.cal_result_headless(now)
    for elem in result_headless:
        output += str(elem)
        output += "\n"
        
    output += str("--------------------")
    output += "\n"


    now_valid = cal4.result_to_valid(result)
    now_valid_headless = cal4.result_to_valid_headless(result_headless)
    output += str("head")
    output += "\n"
    output += str(now_valid)
    output += "\n"
    output += str("headless")
    output += "\n"
    output += str(now_valid_headless)
    output += "\n"

    output += str("--------------------")
    output += "\n"


    valid_stack = []
    valid_good_stack = []
    valid_still_stack = []
    valid_stack_headless = []
    valid_good_stack_headless = []
    valid_still_stack_headless = []

    for draw in range(1, 10):
        for drop in range(1, 10):
            now_copy = copy.deepcopy(now)
            now_copy[draw] += 1
            
            #draw한 패가 유효패면 스킵
            if now_valid[draw] > 0:
                continue
            
            #drop할 패가 없으면 스킵
            if now_copy[drop] == 0:
                continue
            now_copy[drop] += -1
            
            #draw, drop을 반영해서 result를 새로 계산
            draw_and_drop_result = cal2.cal_result(now_copy)
            
            #샨텐수를 줄이는 타패는 스킵
            if cal1.cal_max_num(draw_and_drop_result[0]["body_head_num"]) < cal1.cal_max_num(result_head[0]["body_head_num"]):
                continue
            
            change_valid_head = copy.deepcopy(cal4.result_to_valid(draw_and_drop_result))
            change_valid_head[10] = "DRAW:"+str(draw)+"|DROP:"+str(drop)
            valid_stack.append(change_valid_head)

    #유효패 수가 늘어난 쯔모/타패는 good_stack에, 유효패 수가 그대로인 쯔모/타패는 still_stack에 저장
    for elem in copy.deepcopy(valid_stack):
        if cal1.count_positive(elem) == cal1.count_positive(now_valid):
            valid_still_stack.append(elem)
        if cal1.count_positive(elem) > cal1.count_positive(now_valid):
            valid_good_stack.append(elem)

    output += str("valid_good_stack")
    output += "\n"
    for elem in valid_good_stack:
        output += str(elem)
        output += "\n"

    output += str("--------------------")
    output += "\n"

    for draw in range(1, 10):
        for drop in range(1, 10):
            now_copy = copy.deepcopy(now)
            now_copy[draw] += 1
            
            if now_valid_headless[draw] > 0:
                continue
            if now_copy[drop] == 0:
                continue
            now_copy[drop] += -1
            draw_and_drop_result_headless = cal2.cal_result_headless(now_copy)
            if cal1.cal_max_num_headless(draw_and_drop_result_headless[0]["body_head_num"]) < cal1.cal_max_num_headless(result_headless[0]["body_head_num"]):
                continue
            
            change_valid_headless = copy.deepcopy(cal4.result_to_valid_headless(draw_and_drop_result_headless))
            change_valid_headless[10] = "DRAW:"+str(draw)+"|DROP:"+str(drop)+", headless"
            valid_stack_headless.append(change_valid_headless)


    for elem in copy.deepcopy(valid_stack_headless):
        if cal1.count_positive(elem) == cal1.count_positive(now_valid_headless):
            valid_still_stack_headless.append(elem)
        if cal1.count_positive(elem) > cal1.count_positive(now_valid_headless):
            valid_good_stack_headless.append(elem)

    output += str("valid_good_stack_headless")
    output += "\n"
    for elem in valid_good_stack_headless:
        output += str(elem)
        output += "\n"

    output += str("--------------------")
    output += "\n"

    valid_stack_plus1 = []
    valid_good_stack_plus1 = []
    valid_still_stack_plus1 = []
    valid_stack_headless_plus1 = []
    valid_good_stack_headless_plus1 = []
    valid_still_stack_headless_plus1 = []

    for draw in range(1, 10):
        now_copy = copy.deepcopy(now)
        now_copy[draw] += 1
        draw_and_drop_result = cal2.cal_result(now_copy)
        if cal1.cal_max_num(draw_and_drop_result[0]["body_head_num"]) < cal1.cal_max_num(result_head[0]["body_head_num"]):
            continue
        change_valid_head = copy.deepcopy(cal4.result_to_valid(draw_and_drop_result))
        change_valid_head[10] = "DRAW:"+str(draw)+", plus1, BHnum:"+str(draw_and_drop_result[0]["body_head_num"])
        valid_stack_plus1.append(change_valid_head)

    #유효패 수가 2개 이상 늘어난 쯔모/타패는 good_stack에, 유효패 수가 1개 늘어난 쯔모/타패는 still_stack에 저장
    for elem in copy.deepcopy(valid_stack_plus1):
        if cal1.count_positive(elem) == cal1.count_positive(now_valid)+1:
            valid_still_stack_plus1.append(elem)
        if cal1.count_positive(elem) > cal1.count_positive(now_valid)+1:
            valid_good_stack_plus1.append(elem)

    output += str("valid_good_stack_plus1")
    output += "\n"
    for elem in valid_good_stack_plus1:
        output += str(elem)
        output += "\n"

    output += str("--------------------")
    output += "\n"

    for draw in range(1, 10):
        now_copy = copy.deepcopy(now)
        now_copy[draw] += 1
        
        draw_and_drop_result_headless = cal2.cal_result_headless(now_copy)
        if cal1.cal_max_num_headless(draw_and_drop_result_headless[0]["body_head_num"]) < cal1.cal_max_num_headless(result_headless[0]["body_head_num"]):
            continue
        
        change_valid_headless = copy.deepcopy(cal4.result_to_valid_headless(draw_and_drop_result_headless))
        change_valid_headless[10] = "DRAW:"+str(draw)+", headless"+", plus1, BHnum:"+str(draw_and_drop_result_headless[0]["body_head_num"])
        valid_stack_headless_plus1.append(change_valid_headless)


    for elem in copy.deepcopy(valid_stack_headless_plus1):
        if cal1.count_positive(elem) == cal1.count_positive(now_valid_headless)+1:
            valid_still_stack_headless_plus1.append(elem)
        if cal1.count_positive(elem) > cal1.count_positive(now_valid_headless)+1:
            valid_good_stack_headless_plus1.append(elem)

    output += str("valid_good_stack_headless_plus1")
    output += "\n"
    for elem in valid_good_stack_headless_plus1:
        output += str(elem)
        output += "\n"
    
    return output