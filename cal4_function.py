import cal2_function as cal2
import copy


# result에 있는 now에 1부터 9까지 더하면 몸통(+머리)가 생기는지 보고
# 생긴다면 유효패 확인함
# cal2.cal_result_head 로 result를 찾은 다음, cal4.result_to_valid 로 유효패를 구함.
def result_to_valid(result):
    valid_head = [0] * 11
    for re in result:
        now_copy = copy.deepcopy(re["now"])
        
        for i in range(1, 11):
            now_copy2 = copy.deepcopy(now_copy)
            now_copy2[i] += 1
            copy_result = cal2.cal_result(now_copy2)
            if copy_result[0]["sum"] == []:
                pass
            else:
                #만약 이미 머리가 있는데
                #머리가 추가되서 샹텐수가 올라간 경우 유효패로 안쳐줌
                exist_head = False
                if re["body_head_num"][2] > 0:
                    exist_head = True
                if exist_head and copy_result[0]["body_head_num"][2] > 0:
                    pass
                else:
                    valid_head[i] = i
                
    return valid_head


def result_to_valid_headless(result):
    valid_headless = [0] * 11
    for re in result:
        now_copy = copy.deepcopy(re["now"])
        
        for i in range(1, 11):
            now_copy2 = copy.deepcopy(now_copy)
            now_copy2[i] += 1
            copy_result = cal2.cal_result_headless(now_copy2)
            if copy_result[0]["sum"] == []:
                pass
            else:
                valid_headless[i] = i
            
    return valid_headless