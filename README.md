# Kosilo scraper

Downloads and displays this weeks menu in the terminal

Currently implemented: 
- https://loncek-kuhaj.si/tedenski-jedilnik-tp.php
- https://www.fe.uni-lj.si/o_fakulteti/restavracija/tedenski_meni/

## Usage

Python requirements:

```
pip install beautifulsoup4 translators
```

Run with

### Lonček

```
python loncek_jedilnik.py
```

English version (takes longer to load since it uses Google translate)

```
python loncek_jedilnik.py --en
```

### Fe menza

```
python fe_jedilnik.py
```

English version (takes longer to load since it uses Google translate)

```
python fe_jedilnik.py --en
```