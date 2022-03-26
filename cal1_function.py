from itertools import count


def check_123(now_state, now_pin):
    if  now_state[now_pin] > 0 and now_state[now_pin+1] > 0 and now_state[now_pin+2] > 0:
        return True
    else:
        return False

def check_444(now_state, now_pin):
    if  now_state[now_pin] >= 3:
        return True
    else:
        return False

def check_55(now_state, now_pin):
    if  now_state[now_pin] >= 2:
        return True
    else:
        return False

def count_positive(arr):
    count_num = 0
    for idx in range(1, 10):
        if arr[idx] > 0:
            count_num += 1
    return count_num

def cal_max_num(body_head_num_arr):
    temp_num = 0
    temp_num += body_head_num_arr[0]
    temp_num += body_head_num_arr[1]
    if body_head_num_arr[2] == 1:
        temp_num += 1
    return temp_num

def cal_max_num_headless(body_head_num_arr):
    temp_num = 0
    temp_num += body_head_num_arr[0]
    temp_num += body_head_num_arr[1]
    
    return temp_num