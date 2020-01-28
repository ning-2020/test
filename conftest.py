import pytest
import requests
from ke16.add_teacher import *
from ke16.execute_mysql import results

@pytest.fixture(scope="session")
def login_xadmin_fix():
    s = requests.session()
    login_xadmin(s)
    return s

def delete_teacher_sql():
    '''删除添加老师'''