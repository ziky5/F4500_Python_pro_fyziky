Tato lekce je opakovací. Studenti dostanou na výběr z několika datových souborů typu *.trc* s daty, která která obsahují závislost napětí na čase a data o osciloskopu, který je naměřil. Dostanou i soubor se skriptem, ve kterém je definována funkce, která dokáže *.trc* soubor přečíst.

Úkoly jsou následující:

- Načíst data
- Vykreslit data na začátku pulzu a na konci pulzu a ověřit, že na začátku pulzu je závislost sinusová, zatímco ke konci pulzu je závislost periodická, avšak ne sinusová
- Nakonec je všem doporučena funkce `periodogram <https://docs.scipy.org/doc/scipy-0.13.0/reference/generated/scipy.signal.periodogram.html>`_, aby provedly Fourierovu analýzu naměřených dat a viděli pík na budící frekvenci 13.56 MHz.

Důležitá pro analýzu dat je vzorkovací frekvence uložená v datech o osciloskopu jako HORIZ_INTERVAL': 2.0e-10.

**Varování** - Mnoho souborů s daty je hodně velkých a byly problémy s načítáním do paměti.

**Největší problém** bylo vybrat pouze nějaký interval dat.
