import requests
import re
from requests_toolbelt import MultipartEncoder
from lxml import etree


def login_xadmin(s):
    '''xadmin登录'''
    url = "http://49.235.92.12:8020/xadmin/"
    # s = requests.session()
    r = s.get(url)
    # print(r.text)
    token = re.findall("name='csrfmiddlewaretoken' value='(.+?)'",r.text)
    print(token[0])
    body = {
        "csrfmiddlewaretoken" : token[0],
        "username" : "admin",
        "password" : "yoyo123456",
        "this_is_the_login_form" : "1",
        "next" : "/xadmin/"
    }
    r2 = s.post(url,data=body)
    # print(r2.text)
    if "主页面 | 后台页面" in r2.text:
        print("登录成功！")
    else:
        print("登录失败")



def add_teacher(s,teacher_name="老师003"):
    url2 = "http://49.235.92.12:8020/xadmin/hello/teacherman/add/"
    r2 = s.get(url2)
    token2 = re.findall("name='csrfmiddlewaretoken' value='(.+?)'", r2.text)
    print(token2[0])
    m = MultipartEncoder(
                fields=[
                    ("csrfmiddlewaretoken",token2[0]),
                    ("csrfmiddlewaretoken", token2[0]),
                    ("teacher_name",teacher_name),
                    ("tel","15800000000"),
                    ("mail","123@qq.com"),
                    ("sex","M"),
                    ("_save","")

                ]
    )
    r3 = s.post(url2,data=m,headers={'Content-Type': m.content_type})
    return r3.text

def get_add_result(result):
    '''获取添加文本的结果'''
    demo = etree.HTML(result)
    nodes = demo.xpath('//*[@id="changelist-form"]/div[1]/table/tbody/tr[1]/td[2]/a')
    print(nodes[0].text)
    return nodes[0].text
s = requests.session()
login_xadmin(s)

def add_image(title="zuoye"):
    url3 = "http://49.235.92.12:8020/xadmin/hello/fileimage/add/"
    r4 = s.get(url3)
    tokens = re.findall("name='csrfmiddlewaretoken' value='(.+?)'",r4.text)
    print(tokens[0])
    m = MultipartEncoder(
        fields=[
            ("csrfmiddlewaretoken", tokens[0]),
            ("csrfmiddlewaretoken", tokens[0]),
            ("title", title),
            ("image", ('zuoye_10.png', open('zuoye_10.png', 'rb'), 'image/png')),
            ("_save", "")

        ]
    )
    r4 = s.post(url3,data=m,headers={'Content-Type': m.content_type})
    print(r4.text)



# if __name__ == '__main__':
#     s = requests.session()
#     login_xadmin(s)
#     result = add_teacher(s,teacher_name="麻辣老师2")
#     #判断
#     actul_result = get_add_result(result)
#     assert actul_result == "麻辣老师2"

