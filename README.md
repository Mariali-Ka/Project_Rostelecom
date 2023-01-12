
Финальный тестовый проект SkillFactory курса INTQAP-1052

Автоматизированное тестирование UI сайта: https://b2c.passport.rt.ru/ с использованием PyTest и Selenium.

С тест-кейсами можно ознакомиться по ссылке: https://docs.google.com/spreadsheets/d/15lRAmZlIffvbiVnUIC8lttwZKqOAPRY7H9r6U4xecUI/edit?usp=sharing

В папке Project_Rostelecom в файле base_page.py находится конструктор webdriver и общие для всех тестируемых страниц методы.

В папке Project_Rostelecom в файлах authorization_login_pages.py, authorization_mail_pages.py, authorization_personal_account_pages.py, authorization_phone_pages.py, 

authorization_temporary_code_pages.py, recovery_password_pages.py, registration_pages.py, находятся все локаторы и методы для соответствующих тестируемых страниц.

В корне проекта в файле conftest.py находится фикстура с функцией открытия и закрытия браузера. Для запуска тестов необходимо поменять путь до webdriver на свой.

В корне проекта в файле test.py находятся тесты. Все тесты помечены номером который совпадает с номером тест-кейса в файле: 

https://docs.google.com/spreadsheets/d/15lRAmZlIffvbiVnUIC8lttwZKqOAPRY7H9r6U4xecUI/edit?usp=sharing 

Во всех файлах с тестами находятся закомментированные команды для запуска тестов из командной строки (# pytest -s -v )
