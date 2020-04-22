from bs4 import BeautifulSoup
import requests
from PyPtt import PTT

import random
from getpass import getpass
import sys

# setting
post_url = 'https://www.ptt.cc/bbs/C_Chat/M.1587486579.A.E64.html'
ptt_id = 'mirror0227'
floor = 100  # 不重複發錢
amount = 49
samples = 33


# some check
assert samples >= floor


# get data
res = requests.get(post_url)
if res.status_code != 200:
    print('request failed, code {}'.format(res.status_code))
    sys.exit()
    
# get pushes
soup = BeautifulSoup(res.content, 'html.parser')

push_id_set = set()
pushes = soup.find_all("div", class_='push',)
for s in pushes:
    is_push = '推' in s.find('span', class_="push-tag").string
    if is_push:
        push_id_set.add(s.find(class_="push-userid").string)
print('find {} push\n'.format(len(push_id_set)))

push_id_list = list(push_id_set)[:floor]

# random choice
atari = list(random.sample(push_id_list, k=samples))
atari.sort()

# get ids
for a in atari:
    print(a)

print("恭喜以上 id 中獎，開始發錢\n")

# login
ptt_bot = PTT.API(
    screen_time_out=5,
)
password = getpass()
try:
    ptt_bot.login(ptt_id, password)
except PTT.exceptions.LoginError:
    ptt_bot.log('登入失敗')
    sys.exit()
except PTT.exceptions.WrongIDorPassword:
    ptt_bot.log('帳號密碼錯誤')
    sys.exit()
except PTT.exceptions.LoginTooOften:
    ptt_bot.log('請稍等一下再登入')
    sys.exit()
ptt_bot.log('登入成功')


# give money
for a in atari:
    ptt_bot.give_money(a, 49)


# end program
ptt_bot.logout()
