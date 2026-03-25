import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"

# 伪装成浏览器
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120.0.0.0 Safari/537.36",
}

print("开始发送请求，等待服务器响应...")
response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("网页获取成功！开始提取数据...\n")
    soup = BeautifulSoup(response.content, 'html.parser')

    # 提取标题
    title_element = soup.find('h1')
    page_title = title_element.text.strip() if title_element else "未找到标题"

    # 提取价格
    price_element = soup.find('p', class_='price_color')
    price = price_element.text.strip() if price_element else "未找到价格"

    # 提取图片
    img_container = soup.find('div', class_='item active')
    img_element = img_container.find('img') if img_container else None

    if img_element:
        raw_img_url = img_element.get('src')
        # 填平陷阱，拼接完整网址
        final_img_url = raw_img_url.replace("../../", "http://books.toscrape.com/")
    else:
        final_img_url = "未找到图片"
    
    # 提取在库状况
    stock_element = soup.find('p', class_='instock availability')
    stock_status = stock_element.text.strip() if stock_element else "未找到库存状态"

    # 打印结果
    print("========= 提取结果 =========")
    print(f"【标题】 {page_title}")
    print(f"【价格】 {price}")
    print(f"【图片】 {final_img_url}")
    print(f"【在库】 {stock_status}")
    print("============================")
else:
    print(f"请求失败，状态码: {response.status_code}")

