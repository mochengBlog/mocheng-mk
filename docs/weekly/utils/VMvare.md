## 参考

windows11下安装

https://blog.csdn.net/qq_23845083/article/details/135078707







使用滴答api

1 获取token

```python
import requests
import json

url = "https://api.dida365.com/api/v2/user/signon"

payload = json.dumps({
   "username": "15932052170",
   "password": "Ycsxd2BY25XTAvg"
})
headers = {
   'authority': 'api.dida365.com',
   'referer': 'https://dida365.com/webapp/',
   'origin': 'https://dida365.com',
   'User-Agent': 'Apifox/1.0.0 (https://apifox.com)',
   'Content-Type': 'application/json'
}
response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)


```

2 





aHU5103r3gBLJhZhQz

37#O$5g_n)3Cewh&3t2a(A0cEZDfQh1J