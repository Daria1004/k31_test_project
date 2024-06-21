# Проект по тестированию личного кабинета сети медицинских клиник

**Медицинские центры К+31** ️— частные многопрофильные семейные клиники в Москве.

**Страница** [личного кабинета](https://lk.k31.ru/)

![This is an image](tests/resources/images/lk_k+31_main.png)

<!-- Список проверок-->
## Список проверок, реализованных в автотестах:

### UI автотесты:

✔️ Открытие главной страницы личного кабинета без авторизации   
✔️ Проверка успешной авторизации  
✔️ Ошибка авторизации при неправильно введённом пароле   
✔️ Выход из личного кабинета  
✔️ Успешный поиск по комплексным программам и обследованиям  
✔️ Неуспешный поиск по комплексным программам и обследованиям    
✔️ Проверка отображения в профиле телефона, введённого при авторизации  

### API автотесты (везде была проверка ответа и его схемы):  

✔️ Успешная авторизация  
✔️ Неуспешная авторизации  
✔️ Добавление автомобиля в профиль  
✔️ Удаление автомобиля из профиля  
✔️ Запрос владения автомобилями у другого пользователя  


### MOBILE автотесты:  

✔️ Успешная авторизация  
✔️ Неуспешная авторизации  
✔️ Поиск по комплексным программам и обследованиям  


## Проект реализован с использованием:

<p  align="center">
<code><img width="5%" title="pycharm" src="tests/resources/images/intellij_pycharm.png"></code>
<code><img width="5%" title="python" src="tests/resources/images/python.png"></code>
<code><img width="5%" title="pytest" src="tests/resources/images/pytest.png"></code>
<code><img width="4%" title="requests" src="tests/resources/images/requests.png"></code>
<code><img width="5.5%" title="selene" src="tests/resources/images/selene.png"></code>
<code><img width="4.5%" title="selenium" src="tests/resources/images/selenium.png"></code>
<code><img width="5%" title="selenoid" src="tests/resources/images/selenoid.png"></code>
<code><img width="5%" title="docker" src="tests/resources/images/docker.png"></code>
<code><img width="5%" title="allure" src="tests/resources/images/allure_report.png"></code>
<code><img width="5%" title="alluretestops" src="tests/resources/images/allure_testops.png"></code>
<code><img width="5%" title="appium" src="tests/resources/images/appium.png"></code>
<code><img width="5%" title="browserstack" src="tests/resources/images/browserstack.png"></code>
<code><img width="5.7%" title="github" src="tests/resources/images/github.png"></code> 
<code><img width="5%" title="jenkins" src="tests/resources/images/jenkins.png"></code>
<code><img width="5%" title="jira" src="tests/resources/images/jira.png"></code>
<code><img width="5%" title="telegram" src="tests/resources/images/telegram.png"></code>   


## Особенности проекта
- Автотесты на WEB UI, API и Android App
  - Автотесты WEB UI запускаются через Selenoid
  - Автотесты Android App через BrowserStack или с помощью локального эмулятора
- Сборка проекта в Jenkins
- Интеграция с Allure TestOps
- Отчёты Allure Report
- Автоматизация отчётности о тестовых прогонах и тест-кейсах в Jira
- Отчеты с видео, скриншотами, логами
- Оповещения о тестовых прогонах в Telegram


## ▶️ Локальный запуск

Для локального запуска выполнить команду в терминале:

Все тесты:<br>
```bash
    CONTEXT=local_emulator pytest tests --browser_version=100.0
```

UI тесты:<br>

```bash
    pytest tests/web --browser_version=100.0
```

API тесты:<br>
```bash
    pytest tests/api
```
   
mobile тесты на эмуляторе:<br>
```bash
    CONTEXT=local_emulator pytest tests/mobile
```
   
mobile тесты на bstack:<br>
```
    CONTEXT=bstack pytest tests/mobile
```
   
**Параметры:**

- ️`--browser_version` — оставить пустым, чтобы был скачан актуальный вебдрайвер

**Переменные окружения**

- `CONTEXT` — Задаёт контекст выполнения теста: 
  - `local_emulator` — для локального запуска на эмуляторе Android.
  - ️`local_real` — для локального запуска на устройстве. 
  - ️`bstack` — для запуска в облаке BrowserStack. 

## ▶️ Удалённый запуск 

Выполняется на сервере Jenkins

### 1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/k31_test_project/">проект</a>


### 2. Выбрать пункт **Собрать с параметрами**/**Build with Parameters**
![This is an image](tests/resources/images/jenkins2.png)

### 3. Внести изменения в конфигурации сборки, при необходимости
- ️`BROWSER_VERSION` - выбор версии браузера для запуска тестов, по умолчанию 100.0, вручную можно внести другое значение (99.0, 120.0 или др.)
- `ENVIRONMENT` - значение окружения, можно выбрать из выпадающего списка
- `COMMENT` - комментарий, который будет отправлен в сообщении от бота в Телеграм

### 4. Нажать **Собрать**/ **Build**
![This is an image](tests/resources/images/jenkins4.png)

### 5. Результат запуска сборки можно посмотреть в отчёте Allure
![This is an image](tests/resources/images/jenkins5a.png)


## 📊 Запрос на формирование отчёта:

️команда для Windows

```bash
allure serve
```
️команда для MacOS

```bash
allure serve allure-results
```


### Allure отчёт

#### Общие результаты в Allure Report и Allure TestOps
![This is an image](tests/resources/images/allure_report_images.png)
![This is an image](tests/resources/images/allure_testops_images.png)

#### Пример тест-кейса в Allure Report с логированием и attachments
![This is an image](tests/resources/images/allure_report_images_1.png)

#### Пример тест-кейса в Allure TestOps с логированием и attachments
![This is an image](tests/resources/images/allure_report_images_2.png)

#### Интеграция с Jira
![This is an image](tests/resources/images/jira_1.png)

#### Заведение дефекта (интеграция с Jira)
![This is an image](tests/resources/images/bug.png)

## 🎬 Видео прохождения теста:
![video](tests/resources/images/video.gif)

## 🔔 Получение уведомлений о прохождении тестов в Telegram
![This is an image](tests/resources/images/tg_bot.png)
