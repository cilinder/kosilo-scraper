import sys
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import translators as ts
import translators.server as tss
from datetime import timedelta, date

class DailyMenu:
    def __init__(self, english):
        self.english = english

    def __str__(self):
        daily_soup = self.soup['soup'] if not self.english else tss.google(self.soup['soup'], 'sl', 'en')
        menu = f"{self.day}\n------------\n{'Soup' if self.english else 'Juha'}: {daily_soup}\n"
        if self.english:
            for idx, item in enumerate(self.menu):
                self.menu[idx]['menu'] = tss.google(item['menu'], 'sl', 'en')
        l = max([len(item['menu']) for item in self.menu])
        for idx, item in enumerate(self.menu):
                menu += f"Menu {idx+1}: {item['menu']}     {' ' * (l - len(item['menu']))}{'Price' if self.english else 'Cena'}: {item['price']}\n"
        return menu

def main(english=False):
    req = Request(
        url='https://loncek-kuhaj.si/tedenski-jedilnik-tp.php',
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'html.parser')
    items=[]
    for day in soup.find_all(class_='pm-menu-item-desc'):
        items.append(day)
    items = items[1:]
    day = -1
    menus = [DailyMenu(english) for _ in range(5)]
    today = date.today()
    menus[0].day = ("Monday " if english else "Ponedeljek ") + str(today)
    menus[1].day = ("Tuesday " if english else "Torek ") + str(today + timedelta(days=1))
    menus[2].day = ("Wednesday " if english else "Sreda ") + str(today + timedelta(days=2))
    menus[3].day = ("Thursday " if english else "Četrtek ") + str(today + timedelta(days=3))
    menus[4].day = ("Friday " if english else "Petek ") + str(today + timedelta(days=4))
    for item in items:
        entries = list(item.find_all('p'))
        if entries[0].string == "Dnevna juha":
            day += 1
            menus[day].soup = {'soup': entries[1].string}
            menus[day].menu = []
        else:
            menus[day].menu.append({'menu': entries[2].string.strip(), 'price': entries[1].string})
    print()
    for menu in menus:
        print(menu)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--en":
        main(english=True)
    else:
        main(False)