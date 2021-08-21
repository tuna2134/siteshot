from sanic import Sanic
from sanic.response import *
from selenium import webdriver

app=Sanic(__name__)

# webshot good
@app.post("/api")
async def ss_api(request):
    print("i")
    url=request.json.get("url")
    if not url.startswith("http://") or not url.startswith("https://"):
        url="http://"+url
    option = webdriver.ChromeOptions()
    option.add_argument("--headless")
    option.add_argument("--lang=ja-JP,ja")
    option.add_experimental_option("prefs", {"intl.accept_languages": "ja,ja_JP"})
    driver = webdriver.Chrome(options=option, executable_path="/app/.chromedriver/bin/chromedriver")
    driver.implicitly_wait(3)
    driver.get(url)
    driver.set_window_size(1920, 930)
    driver.maximize_window()
    with open("captcha.png", mode='wb') as local_file:
      local_file.write(driver.get_screenshot_as_png())
    driver.quit()
    return await file("captcha.png")
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
