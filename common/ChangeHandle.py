from time import sleep
class ChangeHandle():
    def __init__(self,driver):
        self.driver=driver
    def change_handle_new(self):

        # 点击录制脚本
        sleep(2)
        handles = self.driver.window_handles

        print(handles)
        self.driver.switch_to.window(handles[1])

    def change_handle_old(self):
        handles = self.driver.window_handles

        print(handles)
        self.driver.switch_to.window(handles[0])