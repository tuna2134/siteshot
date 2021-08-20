# import
from flask import Flask, make_response, request
from selenium import webdriver

app = Flask("siteshot")
#reload
# webshot
@app.route("/webshot")
async def webshot():
  url=request.args.get("url")
  option = webdriver.ChromeOptions()
  option.add_argument("--headless")
  option.add_argument("--lang=ja-JP,ja")
  option.add_experimental_option("prefs", {"intl.accept_languages": "ja,ja_JP"})
  driver = webdriver.Chrome(options=option)
  driver.get(url)
  driver.set_window_size(1280, 720)
  time.sleep(2)
  response = make_response(driver.get_screenshot_as_png())
  response.headers.set("Content-Type", "image/png")
  driver.quit()
  return response

app.run(host="0.0.0.0", debug=True)
