# MC_Exam_Random_Generator

   This package allows for question order randomization on top of two existing latex packages: The `exam` document class and the `exam-randomizechoices` package. The latter only randomizes answer ordering within a multiple choice question, whereas I wanted to also randomize question order. The python code here adds in this extra level of randomization, and will call latex system commands to do so.

   Python was used as it was the easiest and quickest way to code this randomization. It would be cleaner to have a latex package but I do not know how to write TeX macros. Python is easy to use for this application as it can simply take an existing tex doc, and randomize some of the internal text, creating new tex files. The caveat is that it is a bit "hacky".

   ## To run:

   1. Create your exam questions in Master_Template.tex
     *  The python program searches for `%% ! Q` to split questions out.
     * Importantly, before each question that you want to have a random order, you need to make sure it has a comment structure of: `%% ! Q`
     * If you want a question to group with the one above it. Then simply omit the `!`.
     * We also need one of these 'cut points' after the last question, so the tex suffix gets separated out. `%% ! QEnd`
   

   2. Test that your master template compiles correctly, both with and without the 'answers' option.

   3. When satisfied, run (put in desired number for `nversions`
   ```
   python -m generate_exams nversions
   ```

   
   ## A note on creating questions.

   Each question should be written within `\questionp{}`. This is a custom command which wraps each question in a minipage so it appears altogether on the same page. If you have a very long question and don't care/would want it to wrap pages, simply use the standard `\question` with no brackets.

   
   ## Folders:

   Master_Template: Here is where you write your exam

   generated_tex: The python code will generate exam versions into this folder

   generated_pdf: The python code compiles the Tex files, and copies pdfs to this folder, for easy access



   Entrypoint: generate_exams.py