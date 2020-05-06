# PTT 發錢小幫手

Python3 Script.\
給定文章 url，不重複抽樣發 P 幣給「推」的 ID\
沒有 UI 介面

Note: 我想應該只有繁中母語人士會用吧，就用中文來寫好了。

## Usage

### 先裝 requirement

```
pip install -r requirement.txt
```

### 設定

先改好 `ptt_money` 上面 `#setting` 的部分

- post_url = 用 bs4 爬這篇文章的「推」
- ptt_id = 發錢 ID
- floor = 發到第幾個「推」（不重複）
- amount = 發多少錢 **（稅後）**
- samples = 抽幾個人

### 發錢

```
python ptt_money.py
```

名單確認之後，會叫你打密碼登入發錢\
發完錢或遇到錯誤會自動登出
