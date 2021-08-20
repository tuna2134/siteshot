from sanic import Sanic
from sanic.response import *
from selenium import webdriver

app = Sanic("siteshot")

@app.post("/webshot")
async def webshot(request):
  url=request.data.get("url")
  option = webdriver.ChromeOptions()
  option.add_argument("--headless")
  option.add_argument("--lang=ja-JP,ja")
  option.add_experimental_option("prefs", {"intl.accept_languages": "ja,ja_JP"})
  driver = webdriver.Chrome(options=option)
  driver.get(url)
  driver.set_window_size(1280, 720)
  time.sleep(2)
  driver.save_screenshot("captcha.png")
  return await file("captcha.png")

app.run(host="0.0.0.0", port=8080)
