from selenium import webdriver
import os
import json
import requests
import arrow
import traceback
import time

class AutoDownloadFiles:
    __chrome_options = webdriver.ChromeOptions()
    __chrome_options.add_argument('--headless')
    __chrome_options.add_argument('--no-sandbox')
    __chrome_options.add_argument('--disable-gpu')
    __chrome_options.add_argument('--disable-dev-shm-usage')
    __browser = None

    __configPath = ''
    __downloadPath = ''

    sid = ''

    __headers = {
        'Content-Type': 'application/json; charset=UTF-8',
        'Cookie': 'sid={}'.format(sid)
    }

    def __init__(self, configPath, downloadPath):
        self.__configPath = configPath
        self.__downloadPath = downloadPath
        self.__browser = webdriver.Chrome('{}/chromedriver'.format(self.__configPath), options=self.__chrome_options)

    def __isLogin(self):
        testConditionStr = '7020214F8AECD712949615FA52BEAA33D62E9C2B099CC0F2FBCF787DF44E07C29265573E9AE18B1E9CAD423FE5E64928099F5640FD076244775C714E5317D68EFF513F57C8FB871C1530562BCD1AF7024FC5F0113DA5D3E0'
        url = 'http://59.202.38.111:8080/zjqlk/rest/zjqlk/increase/audititem/itemexport/zjqlkaudititemexportchoose/exportItem?conditionStr={}&isCommondto=true'
        text = requests.get(url.format(testConditionStr), headers=self.__headers).text
        # logger.info('获取的attachid是{}'.format(text))
        return '无法访问' not in text

    def __refrashSid(self):
        with open('config/sid', 'r') as f:
            self.sid = f.read()

        self.__headers = {
            'Content-Type': 'application/json; charset=UTF-8',
            'Cookie': 'sid={}'.format(self.sid)
        }


    def __run(self):
        self.__refrashSid()
        if not self.__isLogin():
            self.__login()
            self.__enterQlsx()
            self.__saveCookie()
            # self.__downloadFiles()
            time.sleep(2)
        self.__browser.quit()

    def __waitElement(self, xpath):
        while True:
            try:
                return self.__browser.find_element_by_xpath(xpath)
            except:
                time.sleep(0.5)

    def __getAttachGuid(self, conditionStr):
        url = 'http://59.202.38.111:8080/zjqlk/rest/zjqlk/increase/audititem/itemexport/zjqlkaudititemexportchoose/exportItem?conditionStr={}&isCommondto=true'
        s = json.loads(requests.get(url.format(conditionStr), headers=self.__headers).text)
        s = s['custom']['attachguid']
        # logger.info(s)

        return s

    def __download(self, conditionStr, fileName):

        downloadUrl = 'http://59.202.38.111:8080/zjqlk/rest/frame/base/attach/attachAction/getContent?isCommondto=true&attachGuid={}'

        if fileName == '温州全市':
            fileName = '{}温州'.format(arrow.now().format('MMDD'))

        with open(os.path.join(self.__downloadPath, '{}.xls'.format(fileName)), 'wb') as f:
            f.write(requests.get(headers=self.__headers,
                                 url=downloadUrl.format(self.__getAttachGuid(conditionStr))).content)

    def downloadFiles(self, signal):
        """
        下载全省各地市或者是全市的事项
        :param signal: [全省，全市]
        """
        self.__run()
        # self.__refrashSid()  # 刷新一下uid

        with open('config/地区情形编码', 'r') as f:
            seq = f.readlines()
            seq = list(filter(lambda x: signal in x.split()[0], seq[:1])) + [] if signal == '全市' else seq[1:]
            for area in seq:
                area = area.split()
                # logger.info('正在下载{}'.format(area))
                self.__download(area[1].strip(), area[0])


    def __enterQlsx(self):
        qlsxIframeXpath = '//*[@id="main"]'

        while True:
            try:
                qlsxIframe = self.__browser.find_element_by_xpath(qlsxIframeXpath)
                self.__browser.switch_to.frame(qlsxIframe)
                time.sleep(0.5)
                break
            except:
                pass

        qlsxXpath = '//*[@id="myapps"]/li[4]/div[3]'

        while True:
            try:
                self.__browser.find_element_by_xpath(qlsxXpath).click()
                time.sleep(0.5)

                nowHandle = self.__browser.current_window_handle
                allHandle = self.__browser.window_handles
                newHandle = [x for x in allHandle if x != nowHandle][0]
                self.__browser.switch_to.window(newHandle)
                time.sleep(5)
                break
            except:
                pass

    def __saveCookie(self):
        sid = self.__browser.get_cookie('sid')['value']
        with open('config/sid', 'w') as w:
            w.write(sid)


    def __login(self):

        url = 'http://gmuser.zjzwfw.gov.cn/idm/sso/login'
        self.__browser.get(url)

        userNameXpath = '//*[@id="loginname"]'
        areaSelectXpath = '//*[@id="text"]'
        citySelectXpath = '//*[@id="_easyui_tree_17"]/span[2]'
        iframeXpath = '//*[@id="dialog_page_iframe_0"]/iframe'
        wenzhouXpath = '//*[@id="_easyui_tree_20"]/span[5]'
        confirmXpath = '//*[@id="easyDialogYesBtn"]'
        passwordXpath = '//*[@id="password"]'


        try:
            inputUserName = self.__browser.find_element_by_xpath(userNameXpath)
            with open('{}/user'.format(self.__configPath), 'r') as fp:
                username, password = fp.read().split()
                inputUserName.send_keys(username)

            areaSelect = self.__browser.find_element_by_xpath(areaSelectXpath)
            areaSelect.click()


            #切换到选择区域框框
            while True:

                try:
                    selectIframe = self.__browser.find_element_by_xpath(iframeXpath)
                    break
                except:
                    time.sleep(0.5)

            # selectIframe = self.__browser.find_element_by_xpath(iframeXpath)
            self.__browser.switch_to.frame(selectIframe)

            #县（市区）
            citySelect = self.__waitElement(citySelectXpath).click()

            #点温州市
            wenzhouSelect = self.__waitElement(wenzhouXpath).click()

            #点确认
            self.__browser.find_element_by_xpath(confirmXpath).click()
            self.__browser.switch_to.parent_frame()
            self.__browser.find_element_by_xpath(passwordXpath).send_keys(password)

            self.__browser.find_element_by_xpath('//*[@id="btn-login"]').click()
        except Exception as e:
            traceback.print_exc()
            # logger.info('已经登录')
            return

a = AutoDownloadFiles('{}/config'.format(os.getcwd()), '{}/统计表'.format(os.getcwd()))
a.downloadFiles('全市')