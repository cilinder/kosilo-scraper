from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

class DailyMenu:
    def __str__(self):
        menu = f"{self.day}\n------------\nJuha: {self.soup['soup']}\n"
        l = max([len(item['menu']) for item in self.menu])
        for idx, item in enumerate(self.menu):
            menu += f"Menu {idx+1}: {item['menu']}     {' ' * (l - len(item['menu']))}Cena: {item['price']}\n"
        return menu

def main():
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
    menus = [DailyMenu() for _ in range(5)]
    menus[0].day = "Ponedeljek"
    menus[1].day = "Torek"
    menus[2].day = "Sreda"
    menus[3].day = "Četrtek"
    menus[4].day = "Petek"
    for item in items:
        entries = list(item.find_all('p'))
        if entries[0].string == "Dnevna juha":
            day += 1
            menus[day].soup = {'soup': entries[1].string}
            menus[day].menu = []
        else:
            menus[day].menu.append({'menu': entries[2].string.strip(), 'price': entries[1].string})
    for menu in menus:
        print(menu)


if __name__ == "__main__":
    main()