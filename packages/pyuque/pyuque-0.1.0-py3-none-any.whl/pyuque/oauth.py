'''
Handle OAuth of yuque.
'''
import requests

OAUTH_BASE = 'https://www.yuque.com'

'''
GET https://www.yuque.com/oauth2/authorize
参数
参数名
类型
描述
client_id 
string 
语雀应用分配的 client_id
scope 
string 
要求用户授权的 权限范围，多个权限用逗号分隔，例如: doc,repo,group:read
redirect_uri 
string 
重定向地址，授权完成后会跳转到这个路径，并带上临时授权 code
state 
string 
OAuth 规范中的 state，会透传到回调的 redirect_uri 参数
response_type 
string 
固定值: code
'''

def authorize():
    pass


def get_access_token():
    pass
