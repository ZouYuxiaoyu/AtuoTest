# coding=utf-8
import time

from appium import webdriver

desired_caps = {
    'platformName': 'Android',
    'deviceName': '6c8caec0',
    'platformVersion': '8.1.0',
    # apk 包名
    'appPackage': 'com.unicom.zworeader.ui',
    # apk 的 launcherActivity
    'appActivity': 'com.unicom.zworeader.ui.QuickStartActivity'
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
# 休眠5秒等待页面加载完成
time.sleep(5)
# 自右向左滑动页面
i = 0
while i < 3:
    driver.swipe(800, 1400, 80, 1400, 500)
    i = i + 1
time.sleep(10)
print("成功进入书架")
time.sleep(10)

# 模拟手指点击（最多五个手指），可设置按住时间长度（毫秒）
# 点击书城
driver.tap([(270, 1751), (540, 1920)], 800)

print("成功进入书城")
time.sleep(5)

# 点击频道更多入口
driver.tap([(930, 219), (1080, 324)], 500)
time.sleep(5)

a = 0
# 点击未添加频道
while a < 8:
    if 0 < a & a < 3:
        driver.tap([(75, 793), (285, 895)], 500)
        a = a + 1
    elif 3 < a & a < 7:
        driver.tap([(75, 949), (285, 1051)], 500)
        a = a + 1
    else:
        driver.tap([(75, 1105), (285, 1207)], 500)
        a = a + 1
    time.sleep(1)
print("成功将频道添加到书城")
time.sleep(5)

# 关闭全部频道页面
driver.tap([(968, 111), (1080, 183)], 500)
time.sleep(5)
