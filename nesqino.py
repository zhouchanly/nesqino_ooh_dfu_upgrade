# coding=utf-8
import action as action
from appium import webdriver
import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.wait import WebDriverWait


def appium_desired( ):
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '9'
    desired_caps['deviceName'] = 'TG6HMFSOUCZ9NZ4P'
    desired_caps['appPackage'] = 'no.nordicsemi.android.mcp'
    desired_caps['appActivity'] = 'no.nordicsemi.android.mcp.DeviceListActivity'
    desired_caps['automationName'] = 'uiautomator2'
    desired_caps['newCommandTimeout'] = "2000"
    desired_caps["unicodeKeyboard"] = True  # 使用unicode编码方式发送字符串
    # desired_caps["resetKeyboard"] = True  # 隐藏键盘

    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.implicitly_wait(10)

    #获得屏幕坐标--不行
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    # print(x,y)
    x1 = int(x * 0.70)
    x2 = int(x * 0.3)
    y1 = int(y * 0.9)
    # print(x1,x2,y1)
    for i in range(17):
        time.sleep(1)  #swipe方法前要加一个sleep，不然那滑动不了
        driver.swipe(x1,y1,x2,y1,500)
    time.sleep(1)



    #点击done
    driver.find_element_by_id('no.nordicsemi.android.mcp:id/action_done').click()
    time.sleep(1)


    #点击scanner过滤器
    driver.find_element_by_id('no.nordicsemi.android.mcp:id/filter_header').click()
    # 点击搜索“nes”关键字
    driver.find_element_by_id('no.nordicsemi.android.mcp:id/filter').click()
    # 输入“nes”
    driver.find_element_by_id('no.nordicsemi.android.mcp:id/filter').send_keys("nes")
    #收回过滤器
    driver.find_element_by_id('no.nordicsemi.android.mcp:id/filter_header').click()

    #搜索nes 8F 2c的设备进行升级----这边要选择对设备，不然升级不了,怎么多条件定位？
    driver.find_element_by_id('no.nordicsemi.android.mcp:id/action_connect').click()

    # 点击secure DFU service
    try:
        driver.find_elements_by_id('no.nordicsemi.android.mcp:id/service_main')[3].click()
    except IndexError:
        driver.find_element_by_id('no.nordicsemi.android.mcp:id/action_close').click()
        driver.find_element_by_xpath("//*[contains(@text,'SCANNER')]").click()
        driver.find_element_by_id('no.nordicsemi.android.mcp:id/action_connect').click()
        driver.find_elements_by_id('no.nordicsemi.android.mcp:id/service_main')[3].click()

    # 使能
    driver.find_element_by_id('no.nordicsemi.android.mcp:id/action_start_indications').click() #点击两个箭头图标
    driver.find_element_by_id('no.nordicsemi.android.mcp:id/action_write').click()#点击一个箭头图标
    driver.find_element_by_id('android:id/button1').click() #点击弹框发送
    time.sleep(5)
    driver.find_element_by_id('no.nordicsemi.android.mcp:id/action_close').click()
    driver.find_element_by_xpath("//*[contains(@text,'SCANNER')]").click()
    #todo
    # driver.swipe(int(x*0.7), int(y*0.16), int(x*0.2), int(y*0.16), 500) #滑动到蓝牙扫描界面---这边有问题
    # driver.find_element_by_xpath('//android.widget.LinearLayout[@content-desc="Scanner"]').click()  #这步可以取消

    #下拉刷新
    time.sleep(2)
    driver.swipe(int(x * 0.5), int(y * 0.3), int(x * 0.5), int(y * 0.7), 1000)
    print("下拉")



    # 点击搜索“nes”关键字,输入nes，收回过滤器
    # driver.find_element_by_id('no.nordicsemi.android.mcp:id/filter').click()
    # driver.find_element_by_id('no.nordicsemi.android.mcp:id/filter').send_keys("nes")
    # driver.find_element_by_id('no.nordicsemi.android.mcp:id/filter_header').click()

    #点击第一个dfu
    driver.find_element_by_id('no.nordicsemi.android.mcp:id/action_connect').click()

    #点击右上角的升级
    driver.find_element_by_id('no.nordicsemi.android.mcp:id/action_dfu').click()
    driver.find_element_by_id('android:id/button1').click()

    #选择升级文件
    print("选择文件")
    driver.find_element_by_xpath("//android.widget.ImageButton[@content-desc='显示根目录']").click()
    driver.find_element_by_xpath("//*[contains(@text,'文件管理')]").click()
    driver.find_element_by_xpath("//*[contains(@text,'手机存储')]").click()
    driver.find_element_by_xpath("//*[contains(@text,'1')]").click()
    driver.find_element_by_xpath("//*[contains(@text,'Nesqino_OOH-MCU-Image-V0.2.2_dfu.zip')]").click()


    #等待升级成功
    #获取吐司
    toast_message = "Application has been sent successfully."
    message = '//*[@text=\'{}\']'.format(toast_message)
    # 显示等待检测元素
    toast_element = WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath(message))
    print(toast_element.text)
    # 结果进行比较
    assert toast_element.text == "再按一次返回键退出手机淘宝"

    time.sleep(10)





    driver.quit()


if __name__ == "__main__":
    print("111")
    appium_desired()

    # f  常")


