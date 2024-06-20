# Проект по тестированию личного кабинета сети клиник К+31

**Медицинские центры К+31** — частные многопрофильные семейные клиники в Москве.

**Страница** [личного кабинета](https://lk.k31.ru/)

![This is an image](/tests/resources/images/lk_k+31_main.png)

<!-- Список проверок-->
## Список проверок, реализованных в автотестах:

### UI автотесты:

* ✅ Открытие главной страницы личного кабинета без авторизации 
* ✅ Проверка успешной авторизации 
* ✅ Ошибка авторизации при неправильно введённом пароле 
* ✅ Выход из личного кабинета 
* ✅ Успешный поиск по комплексным программам и обследованиям 
* ✅ Неуспешный поиск по комплексным программам и обследованиям  
* ✅ Проверка отображения в профиле телефона, введённого при авторизации  


### API автотесты (везде была проверка ответа и его схемы):  

* ✅ Успешная авторизация 
* ✅ Неуспешная авторизации
* ✅ Добавление автомобиля в профиль
* ✅ Удаление автомобиля из профиля
* ✅ Запрос владения автомобилями у другого пользователя


### mobile автотесты:  

* ✅ Успешная авторизация 
* ✅ Неуспешная авторизации
* ✅ Поиск по комплексным программам и обследованиям 


<!-- Tools -->

## Проект реализован с использованием:

<p  align="center">
<code><img width="5%" title="pycharm" src="/tests/resources/images/intellij_pycharm.png"></code>
<code><img width="5%" title="python" src="/tests/resources/images/python.png"></code>
<code><img width="5%" title="pytest" src="/tests/resources/images/pytest.png"></code>
<code><img width="4%" title="requests" src="/tests/resources/images/requests.png"></code>
<code><img width="5.5%" title="selene" src="/tests/resources/images/selene.png"></code>
<code><img width="4.5%" title="selenium" src="/tests/resources/images/selenium.png"></code>
<code><img width="5%" title="selenoid" src="/tests/resources/images/selenoid.png"></code>
<code><img width="5%" title="docker" src="/tests/resources/images/docker.png"></code>
<code><img width="5%" title="allure" src="/tests/resources/images/allure_report.png"></code>
<code><img width="5%" title="alluretestops" src="/tests/resources/images/allure_testops.png"></code>
<code><img width="5%" title="appium" src="/tests/resources/images/appium.png"></code>
<code><img width="5%" title="appium" src="/tests/resources/images/appium.png"></code>
<code><img width="5%" title="browserstack" src="/tests/resources/images/browserstack.png"></code>
<code><img width="5.7%" title="github" src="/tests/resources/images/github.png"></code> 
<code><img width="5%" title="jenkins" src="/tests/resources/images/jenkins.png"></code>
<code><img width="5%" title="jira" src="/tests/resources/images/jira.png"></code>
<code><img width="5%" title="telegram" src="/tests/resources/images/telegram.png"></code>   


## Особенности проекта
- Автотесты на WEB UI, API и Android App
  - Автотесты WEB UI запускаются через Selenoid
  - Автотесты Android App через BrowserStack или с помощью локального эмулятора
- Сборка проекта в Jenkins
- Отчеты Allure Report
- Интеграция с Allure TestOps
- Автоматизация отчетности о тестовых прогонах и тест-кейсах в Jira
- Отчеты с видео, скриншотами, логами
- Оповещения о тестовых прогонах в Telegram


## Локальный запуск UI и API тестов  

1. Скачать проект и открыть в IDE 
2. Создайте следующий файл:
   * `.env`  для запуска UI тестов локально и заполнить его актуальными тестовыми параметрами.
   * Пример заполнения файла указан в файле с расширением `.env.example`
3. Создайте и активируйте виртуальное окружение
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```
4. Установите зависимости с помощью pip
   ```bash
   pip install -r requirements.txt
   ```
5. Для локального запуска необходимо выполнить команду в терминале:
    * Все тесты:<br>
    ```bash
    pytest ./tests --context=web_local --browser_name=BROWSER_NAME --browser_version=
    ```
    * UI тесты:<br>
    ```bash
    pytest tests/web --context=web_local --browser_name=BROWSER_NAME --browser_version=
    ```
   
   * API тесты:<br>
    ```bash
    pytest tests/api
    ```
   
   * mobile тесты на эмуляторе:<br>
    ```bash
    pytest tests/mobile --context=local_emulator
    ```
   
   * mobile тесты на bstack:<br>
    ```bash
    pytest tests/mobile --context=bstack
    ```
   
   Параметры:
      * --context=web_local для локального запуска. Для запуска через Selenoid будет web_selenoid
      * --browser_name= на выбор доступны `chrome` и `firefox`
      * --browser_version= оставить пустым, чтобы был скачан актуальный вебдрайвер
      
6. Выполнить запрос на формирование отчета:
* команда для Windows
```bash
allure serve
```
* команда для MacOS
```bash
allure serve allure-results
```

<!-- Jenkins -->
##  Удаленный запуск автотестов выполняется на сервере Jenkins

<a target="_blank" href="https://jenkins.autotests.cloud/job/">Ссылка на проект в Jenkins</a>

### Параметры сборки
Данные параметры не обязательны для заполнения.

* `TESTS_FOLDER` - параметр определяет какие тесты будут запущены, по умолчанию ./tests/web - тесты WEB UI
* `COMMENT` - комментарий, который будет отправлен в сообщении от бота в Телеграм
* `BROWSER_NAME` - выбор браузера для запуска тестов, по умолчанию chrome
* `BROWSER_VERSION` - выбор версии браузера для запуска тестов, по умолчанию 100.0

![This is an image](assets/jenkins_parametrize.png)

### Запуск автотестов в Jenkins

1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/AD_qa_guru_diploma/">проект</a>

![This is an image](assets/jenkins_build_start.png)

2. Выбрать пункт **Build with Parameters**

3. Внести изменения в конфигурации сборки, при необходимости

4. Нажать **Build**

5. Результат запуска сборки можно посмотреть в классическом формате Allure Results

### Allure отчет

![image](assets/allure_results_jenkins_overview.png)
Отчет позволяет получить детальную информацию по все шагам тестов, включая скриншоты и log - файлы

![image](assets/allure_results_jenkins.png)

## Интеграция с Allure TestOps

<a target="_blank" href="https://allure.autotests.cloud/project/4217/dashboards">Ссылка на проект в
AllureTestOps</a> (запрос доступа `admin@qa.guru`)

#### Список всех кейсов, имеющихся в проекте

![This is an image](assets/alluretestops_test_cases.png)

#### Отображение результатов прогона тестов

![This is an image](assets/alluretestops_all_test_results.png)

## Интеграция с Jira

<a target="_blank" href="https://jira.autotests.cloud/browse/HOMEWORK-1218">Ссылка на проект в Jira</a>

![This is an image](assets/jira_all_tests.png)

## Видео прохождения теста:

Видеозапись каждого теста генерируется с помощью `Selenoid` после успешного запуска контейнера c тестами в `Docker`.

![video](assets/test_video.gif)

## Получение уведомлений о прохождении тестов в Telegram

После завершения сборки специальный Telegram-бот отправляет сообщение с отчетом.  

<img src="assets/tg_message.png" width="300" height="300">