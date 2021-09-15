print("起動しました")
from sanic import Sanic
from sanic.response import *
from selenium import webdriver
import os
import asyncio
from jinja2 import Environment, FileSystemLoader

env=Environment(loader=FileSystemLoader('./templates/', encoding='utf8'), enable_async=True)

app=Sanic(__name__)

app.static('/static', './static')

async def template(tpl, **kwargs):
    template = env.get_template(tpl)
    content = await template.render_async(kwargs)
    return html(content)

@app.route("/")
async def main(request):
    return redirect("/index.html")

@app.route("/<file>")
async def main(request, file):
    if file.endswith(".html"):
        if file in os.listdir("templates"):
            return await template(file)
        else:
            return await template("index.html")
    else:
        return redirect("/index.html")

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

@app.get("/manaba")
async def automanaba(request):
    user="20612"
    option.add_argument("--headless")
    option.add_argument("--lang=ja-JP,ja")
    option.add_experimental_option("prefs", {"intl.accept_languages": "ja,ja_JP"})
    driver = webdriver.Chrome(options=option, executable_path="/app/.chromedriver/bin/chromedriver")
    driver.implicitly_wait(3)
    user=driver.find_element_by_id("mainuserid")
    user.clear()
    user.send_keys(user)
    print("ok")
    password=driver.find_element_by_name("password")
    password.send_keys(user)
    submit=driver.find_element_by_name("login")
    submit.submit()
    return text("ok")
    
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
