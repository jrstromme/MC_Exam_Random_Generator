# MC_Exam_Random_Generator


   ## To run:

   1. Create your exam questions in Master_Template.tex   Importantly, before each question that you want to have a random order, you need to make sure it has a comment structure of
   ```
   %% ! Q
   ```
   If you want a question to group with the one above it. Then simply omit the !. We also need one of these 'cut points' after the last question, so the tex suffix gets separated out.

   2. Test that your master template compiles correctly, both with and without the 'answers' option.

   3. When satisfied, run (put in desired number for 'nversions'
   ```
   python -m generate_exams nversions
   ```
   

   
   ## Folders:

   Master_Template: Here is where you write your exam

   generated_tex: The python code will generate exam versions into this folder

   generated_pdf: The python code compiles the Tex files, and copies pdfs to this folder, for easy access



   Entrypoint: generate_exams.py