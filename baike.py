import requests

# url = 'http://baike.baidu.com/link?url=IYE3gxq9SzNKjyb6B9v3PKISknwelLAPQ9JWQZJpbvy3m9GZ_-zXcuL8aSTnfpzEHB4-frTPt4lrqEgMquUIx3qR_E2rITwrdDoRiR3dTJnumWbmuMgGGEf2pVeOI6Ho'
# mm = 'IYE3gxq9SzNKjyb6B9v3PKISknwelLAPQ9JWQZJpbvy3m9GZ_-zXcuL8aSTnfpzEHB4-frTPt4lrqEgMquUIx3qR_E2rITwrdDoRiR3dTJnumWbmuMgGGEf2pVeOI6Ho'
url = 'http://baike.baidu.com/item/%E5%9B%A0%E6%9E%9C%E6%A0%91'

res = requests.get(url)
res.encoding = 'utf-8'

print(res.text)
