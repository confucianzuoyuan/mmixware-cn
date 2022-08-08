pdf:
	noweave -index -latex mmix-pipe.nw > mmix-pipe.tex
	python etl.py
	mv mmix-pipe.tex.new mmix-pipe.tex
	xelatex mmix-pipe.tex
	xelatex mmix-pipe.tex