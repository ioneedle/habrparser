# подключаем бс4 и рекуэстс. бс4 это модуль для парсига,
# а рекуэстс модуль для работы с интернетом
import bs4, requests

def getpage(cssclass, adres):   
    # requests.get дает штмл код любой веб страницы
    s=requests.get(adres).text
    # создаем экземпляр парсера и парсим им полученный код веб страницы
    parser=bs4.BeautifulSoup(s, "html.parser")
    # получаем массив элементов веб страницы с указанным классом через точку как в цсс
    massiv=parser.select(cssclass)
    # проходим по массиву найденных элементов и печатаем их текст и ссылку
    for x in massiv:
        # Печатаем текст найденного элемента
        print(x.getText())
        # Печатаем аттрибут href найденного элемента (то есть ссылку на статью)
        print(x.attrs['href'])

# Выбираем определенный хаб
getpage('.post__title_link','https://habr.com/ru/search/?target_type=posts&q=%5B%D0%BC%D0%B0%D1%88%D0%B8%D0%BD%D0%BD%D0%BE%D0%B5%20%D0%BE%D0%B1%D1%83%D1%87%D0%B5%D0%BD%D0%B8%D0%B5%5D&order_by=date')



