# coding=utf-8
import time
import unittest

from appium import webdriver

desired_caps = {
    'platformName': 'Android',
    'deviceName': 'emulator-5554 ',
    'platformVersion': '5.0',
    # apk 包名
    'appPackage': 'com.linkedin.android',
    # apk 的 launcherActivity
    'appActivity': 'com.linkedin.android.authenticator.LaunchActivity'
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
time.sleep(2)
i = 0
while i < 3:
    driver.swipe(300, 1200, 600, 1200, 300)
    i = i+1
driver.find_element_by_id("com.linkedin.android:id/growth_prereg_v2_fragment_account_exists").click()


# 在登录页面输入账号密码，点击登录按钮
driver.find_element_by_id("com.linkedin.android:id/growth_login_fragment_sign_in").send_keys("zouyuxiaoyu@gmail.com")
driver.find_element_by_id("com.linkedin.android:id/growth_login_join_fragment_password").send_keys("Linked@257253")
driver.find_element_by_id("com.linkedin.android:id/growth_login_fragment_sign_in").click()

print("用户zouyuxiaoyu@gmail.com登录成功")


