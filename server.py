from sanic import Sanic
from sanic.response import *
from selenium import webdriver

#prototype
app=Sanic("app")

@app.post("/api")
async def ss_api(request):
    print("i")
    url=request.json.get("url")
    driver = webdriver.Firefox()
    driver.implicitly_wait(3)
    #driver.set_preference("intl.accept_languages", "ja")
    driver.get(url)
    with open("captcha.png", mode='wb') as local_file:
      local_file.write(driver.get_screenshot_as_png())
    driver.quit()
    return await file("captcha.png")
    
app.run(debug=True)
