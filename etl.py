with open("mmix-pipe.tex", "rt") as fin:
    with open("mmix-pipe.tex.new", "wt") as fout:
        for line in fin:
            line1 = line.replace("\documentclass{article}", "\\documentclass[lang=cn,10pt]{elegantbook}")
            line2 = line1.replace("\\begin{document}", "\\begin{document}\\tableofcontents")
            fout.write(line2)