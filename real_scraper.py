import requests
from bs4 import BeautifulSoup
import csv
import time


with open('1000_books_data.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    
    
    writer.writerow(['书名', '价格', '图片链接', '库存状态'])
    
    # ==========================================
    # 循环，自动翻阅 50 页
    # ==========================================
    for page in range(1, 51):
        url = f"https://books.toscrape.com/catalogue/page-{page}.html"
        print(f"抓取第 {page} 页...")
        
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        books = soup.find_all('article', class_='product_pod')
        
        # ==========================================
        # ==========================================
        for book in books:
            
            
            
            # 1. 提取标题 
            title_element = book.find('h3')
            a_element = title_element.find('a') if title_element else None
            title = a_element.get('title') if a_element else "未找到标题"
            # 2. 提取价格 
            price_element = book.find('p', class_='price_color')
            price = price_element.text.strip() if price_element else "未找到价格"
            # 3. 提取图片链接 
            img_element = book.find('img', class_='thumbnail')
            img_url = img_element.get('src').replace("../", "https://books.toscrape.com/") if img_element else "未找到图片"
            # 4. 提取在库状态
            stock_element = book.find('p', class_ = 'instock availability')
            stock = stock_element.text.strip() if stock_element else "未找到库存状态"

            
            
            writer.writerow([title, price, img_url, stock])
            
        
        time.sleep(1)

print("\n 已全部提取,检查CSV文件")