(TeX-add-style-hook
 "Master_Template"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-class-options
                     '(("exam" "answers")))
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("hyperref" "colorlinks" "linkcolor=blue") ("geometry" "a4paper") ("exam-randomizechoices" "debug" "randomize" "nokeeplast") ("datetime" "yyyymmdd" "hhmmss")))
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "path")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "url")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "nolinkurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperbaseurl")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperimage")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "hyperref")
   (add-to-list 'LaTeX-verbatim-macros-with-braces-local "href")
   (add-to-list 'LaTeX-verbatim-macros-with-delims-local "path")
   (TeX-run-style-hooks
    "latex2e"
    "exam"
    "exam10"
    "parskip"
    "hyperref"
    "mathtools"
    "geometry"
    "exam-randomizechoices"
    "amsfonts"
    "amsmath"
    "bm"
    "amssymb"
    "array"
    "graphicx"
    "multirow"
    "subfigure"
    "subfloat"
    "ulem"
    "datetime")
   (TeX-add-symbols
    '("questionp" 1)
    '("sol" 1)
    "newline"))
 :latex)

