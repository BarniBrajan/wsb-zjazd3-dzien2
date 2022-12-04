
# TDD

## File 1.py
Podpiecie klasu unittest i wywolanie testow jednostkowych
testy jednostkowe uruchamiaja sie automatycznie
wywolujemy testy poprze polecenie: python3 1.py -v

## File test_sum.py
wywolujemy testy poprze polecenie:
<i>python3 -m unittest discover tests -v</i>
<i>python3 -m unittest discover tests -v -k div </i> wywola testy z nazwa zaweirajaca DIV

## File 2.py
testowanie funkcji

## Pytest - File 1.py

### srodowisko wirtualne
```
python3 -m venv .venv 
```
### aktywacja srodowiska wirtualnego
```
source .venv/bin/activate
```
### wywolanie testow w pytest
```
pytest -v
```
Pliki testowe musza zaczynac sie od "test_***" gdzie ** dalsza nazwa pliku