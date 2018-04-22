# Watcher of Friends Online

This program prints to the console your online friends in social network vk.com

# How to Install

Python 3 should be already installed. Then use pip (or pip3 if there is a conflict with old Python 2 setup) to install dependencies:

```bash
pip install -r requirements.txt # alternatively try pip3
```


To work you need to register your application at https://vk.com/dev and insert your application_id in variable name APP_ID.

 Example:
````bash
$ python3 vk_friends_online.py
Enter you login: login@yandex.ru
Enter password: ********
Иван Иванов
Петр Петров

````
Remember, it is recommended to use [virtualenv/venv](https://devman.org/encyclopedia/pip/pip_virtualenv/) for better isolation.

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
