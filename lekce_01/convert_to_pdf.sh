#!/bin/bash

jupyter nbconvert --to=latex --template=revtex_nocode.tplx praktikum_pdf.ipynb
pdflatex praktikum_pdf.tex
bibtex praktikum_pdf.aux
pdflatex praktikum_pdf.tex
pdflatex praktikum_pdf.tex

rm *.bbl *.aux *.blg *.log *.out #*.tex
