from selenium.webdriver.common.by import By

# Locators
ACCPT_LL_CKS_BTN = (By.XPATH, "//button[@id='onetrust-accept-btn-handler']")
GFT_CRDS_ICN = (By.XPATH, "//ul[@id='miniNav']//a[@class='nav-link'][normalize-space()='Gift Cards']")
JN_R_TM_ICN = (By.XPATH, "//a[@class='nav-link'][normalize-space()='Join Our Team']")
FRCHSN_ICN = (By.XPATH, "//ul[@id='miniNav']//a[@class='nav-link'][normalize-space()='Franchising']")
ADDR_KY_WRD = (By.XPATH, "(//div[@class='col-md-6 col-xl-7 locations'])[1]")