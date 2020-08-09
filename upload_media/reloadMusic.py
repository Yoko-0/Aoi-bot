from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


def reloadMusic():
    url_albums = "https://vk.com/audios-195205545?section=playlists"
    driver = webdriver.Chrome(ChromeDriverManager().install())

    driver.get(url_albums)

    login = "/html/body/div[9]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/form/input[7]"
    password = "/html/body/div[9]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/form/input[8]"
    login_button = "/html/body/div[9]/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[2]/form/div[2]/button[1]"

    driver.find_element_by_xpath(login).send_keys("+421951308761")
    driver.find_element_by_xpath(password).send_keys("Baris0n01))")
    driver.find_element_by_xpath(login_button).click()
    sleep(1)

    driver.get(url_albums)

    audios_album = {}
    xpath_albums = "//*[@id='content']/div/div[2]/div[2]/div[2]/div/div[2]/div/div/div"
    albums_class = "_audio_pl"

    albums = driver.find_element_by_xpath(xpath_albums).find_elements_by_class_name(albums_class)
    urls = []

    for album in albums:
        urls.append(str(album.get_attribute("data-id")))

    for url in urls:

        print(url)

        driver.get("https://vk.com/audios-195205545?section=playlists&z=audio_playlist" + url)

        class_audios = "_audio_pl_snippet__list"
        audio_class = "audio_row"
        sleep(1)
        audios_html = driver.find_element_by_class_name(class_audios).find_elements_by_class_name(audio_class)

        for audio in audios_html:
            try:
                audios_album[url].append(str(audio.get_attribute("data-full-id").split('_')[1]))

            except:
                audios_album[url] = [str(audio.get_attribute("data-full-id").split('_')[1])]
    driver.quit()
    return audios_album
