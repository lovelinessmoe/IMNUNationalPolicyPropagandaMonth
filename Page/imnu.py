import time

from selenium.webdriver.common.by import By

class imnu:
    text_ans = ["各民族共有精神家园", "铸牢中华民族共同体意识", "高质量发展", "全面从严治党", "统一",
                "依法治理", "共同性", "反腐败", "中华民族共同体", "党史"]

    radio_ans = [1, 1, 1, 0, 0, 0, 1, 1, 1, 0]

    single_ans = [3, 4, 3, 4, 3, 4, 4, 3, 1, 4,
                  2, 1, 3, 1, 1, 3, 3, 1, 1, 1,
                  1, 3, 3, 3, 2, 2, 4, 3, 1, 1,
                  1, 1, 2, 1, 3, 1, 1, 1, 4, 4,
                  3, 4, 1, 4, 1, 4, 1, 4, 1, 1]

    mut_ans = [
        [2, 4], [1, 3, 4], [1, 2], [1, 2, 3, 5], [2, 3, 4], [1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 4],
        [1, 2, 3, 4], [1, 2, 3], [1, 3, 4], [1, 2, 4], [1, 3], [1, 2, 4], [1, 2, 3], [1, 2, 3], [2, 3], [2, 3, 4],
        [1, 2, 3, 4], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [3, 4], [1, 2, 3, 4], [1, 2], [1, 2, 3, 4], [1, 2, 3, 4],
        [1, 2, 3], [1, 3, 4]
    ]

    def __init__(self, driver, url):
        self.driver = driver
        self.driver.get(url)

    def test_imnu(self, name, school, num):
        self.driver.find_element(By.ID, "q1_0").send_keys(name)
        self.driver.find_element(By.ID, "q1_1").send_keys(school)
        self.driver.find_element(By.ID, "q1_2").send_keys(num)

        # 每次循环都加一是因为个人信息也算一道题
        for i in range(1, 101):
            # 填空题
            if 1 <= i <= 10:
                i += 1
                print(i)
                self.driver.find_element(By.ID, "q" + str(i)).send_keys(self.text_ans[i - 2])
            # 选择题
            elif 11 <= i <= 20:
                i += 1
                if bool(self.radio_ans[i - 12]):
                    radio_id = "q" + str(i) + "_1"
                else:
                    radio_id = "q" + str(i) + "_2"
                # 寻找id上的a标签
                # 选择对应id之上的a标签
                xpath = "//*[@id='" + radio_id + "']/../.."
                self.driver.find_element(By.XPATH, xpath).click()
            # 单选题
            elif 21 <= i <= 70:
                i += 1
                single_id = "q" + str(i) + "_" + str(self.single_ans[i - 22])
                xpath = "//*[@id='" + single_id + "']/../.."
                self.driver.find_element(By.XPATH, xpath).click()
            # 多选题
            elif 71 <= i <= 100:
                i += 1
                for j in self.mut_ans[i - 72]:
                    mut_id = "q" + str(i) + "_" + str(j)
                    xpath = "//*[@id='" + mut_id + "']/../.."
                    self.driver.find_element(By.XPATH, xpath).click()
        # 防止太快再次等待100s
        time.sleep(100)
        # 提交
        self.driver.find_element(By.ID, "ctlNext").click()
        time.sleep(3000)
