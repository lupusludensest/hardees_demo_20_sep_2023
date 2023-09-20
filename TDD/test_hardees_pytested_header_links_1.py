from all_locators_tdd import *
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

def test_hardees_pytested_header_links_1():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)

    driver.get("https://www.hardees.com/locations")
    driver.delete_all_cookies()
    wait = WebDriverWait(driver, 15)

    # 1 Click button "Accept" cookies
    accpt_ll_cks_btn = wait.until(EC.element_to_be_clickable(ACCPT_LL_CKS_BTN))
    accpt_ll_cks_btn.click()

    # 2 Click on Gift Cards icon. Verify expected https://www.buyatab.com/custom/hardees is open
    gft_crds_icn = wait.until(EC.element_to_be_clickable(GFT_CRDS_ICN))
    gft_crds_icn.click()
    buyatab_com = driver.current_url
    expected_text = "https://www.buyatab.com/custom/hardees/"
    actual_text = str(buyatab_com)
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'
    driver.back()

    # 3 Click on Join Our Team icon. Verify expected https://www.hardees.com/careers/ is open
    jn_r_tm_icn = wait.until(EC.element_to_be_clickable(JN_R_TM_ICN))
    jn_r_tm_icn.click()
    crs_pg_url = driver.current_url
    expected_text = "https://www.hardees.com/careers"
    actual_text = str(crs_pg_url)
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'
    driver.back()

    # 4 Click on Franchising icon. Verify expected https://ckefranchise.com/ is open
    frchsn_icn = wait.until(EC.element_to_be_clickable(FRCHSN_ICN))
    frchsn_icn.click()
    frchsn_url = driver.current_url
    expected_text = "https://ckefranchise.com/"
    actual_text = str(frchsn_url)
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'
    driver.back()

    # Verify we returned to https://www.hardees.com/locations
    base_url = driver.current_url
    expected_text = "https://www.hardees.com/locations"
    actual_text = str(base_url)
    assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    sleep(2)
    driver.delete_all_cookies()
    driver.quit()