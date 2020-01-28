import pytest
import requests
from ke15.add_teacher import *





def test_add_teacher(login_xadmin_fix):
    s = login_xadmin_fix
    result = add_teacher(s,teacher_name="麻辣老师2")
    #判断
    actul_result = get_add_result(result)
    assert actul_result == "麻辣老师2"
