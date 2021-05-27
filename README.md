Тестовое задание для "Крауд"

Цель: сбор и выгрузка в csv (для дальнейшей обработки другими системами) моментального среза показаний погоды и текущего прогноза погоды в разных городах на момент запроса такого среза оператором.
Использовать можно любые фреймворки, библиотеки. Писать на любом удобном языке программирования. В общем все так, как нравится самому.
- 1) Сделать страницу с авторизацией (вход по логину и паролю - при желании добавить 2fa через ссылку на почту), созданием нового пользователя.
- 2) На странице сделать кнопку формирования и скачивания нового среза погодных данных.
  При нажатии на кнопку происходит следующее:
  - a) через Яндекс.Погода API (разобраться с API и завести доступ "тестовый") собираем данные по 5 наиболее населенным городам РФ.
  - b) собранные данные складываем в базу (помечаем их как данные для очередного запрошенного отчета).
  - c) данные сохраняем в csv, который автоматически скачивается в браузере клиента (оператора). Структуру данных csv придумать самостоятельно таким образом, чтобы непосвященный человек (оператор) понял, о чем там речь, открыв его в экселе.
- 3) Кроме кнопки нового среза (см п.2) на этой же странице вывести таблицу (или в другом удобном виде) историю срезов, собранных таким образом.
Структуру базы данных спроектировать самостоятельно с учетом особенностей задания.
Для каждого исторического среза необходимо:
  - a) указывать дату, время, логин пользователя (кто запросил срез)
  - b) иметь возможность (ссылка, кнопка и тп) скачать соответствующий csv с историческими данными
- 4) Дополнительно на той же странице (желательно вверху) отобразить текущие погодные данные по городам в табличном или другом удобном для просмотра виде
- 5) Сайт разместить в интернете (любым удобным способом).
 