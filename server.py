from sanic import Sanic
from sanic.response import *
from selenium import webdriver
import os
import asyncio

app=Sanic(__name__)

# webshot good
@app.post("/api")
async def ss_api(request):
    print("i")
    url=request.json.get("url")
    password=request.json.get("password")
    if not password == os.getenv("password"):
        print("error")
        return json({"error": "password is invaild"})
    option = webdriver.ChromeOptions()
    option.add_argument("--headless")
    option.add_argument("--lang=ja-JP,ja")
    option.add_experimental_option("prefs", {"intl.accept_languages": "ja,ja_JP"})
    driver = webdriver.Chrome(options=option, executable_path="/app/.chromedriver/bin/chromedriver")
    driver.implicitly_wait(3)
    driver.get(url)
    driver.set_window_size(1280, 730)
    await asyncio.sleep(2)
    with open("captcha.png", mode='wb') as local_file:
      local_file.write(driver.get_screenshot_as_png())
    driver.quit()
    return await file("captcha.png")
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
