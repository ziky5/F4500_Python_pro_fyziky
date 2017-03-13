Tato složka obsahuje materiál použitý na úvodní lekci. Na lekci byl prezentován pouze jeden notebook: ``praktikum.ipynb``, 
která obsahuje řešení slavného "Fišerova problému". 

Dále jsou zde k nalezení další dva notebooky: ``praktikum_html.ipynb`` a ``praktikum_pdf.ipynb``. ``praktikum_html.ipynb`` 
je obsahově identický s původním notebookem, rozdíl je ve formě - tento notebook je nachystán na export do statického html.
``praktikum_pdf.ipynb`` je opět obsahově stejný, jen je notebook nachystán na přímý export do pdf formátu.

Export do html::

    jupyter nbconvert --to html praktikum_html.ipynb

Export do pdf::

    ./convert_to_pdf.sh
