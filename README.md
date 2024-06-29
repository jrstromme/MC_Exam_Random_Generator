# MC_Exam_Random_Generator


   ## To run:

   1. Create your exam questions in Master_Template.tex   Importantly, before each question that you want to have a random order, you need to make sure it has a comment structure of: `%% ! Q`
   If you want a question to group with the one above it. Then simply omit the `!`.

   We also need one of these 'cut points' after the last question, so the tex suffix gets separated out. `%% ! QEnd`

   The python program searches for `%% ! Q` to split questions out.

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