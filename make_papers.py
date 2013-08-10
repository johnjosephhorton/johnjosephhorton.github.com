# Author: John J. Horton 
# Date: Nov 1, 2012 
# Purpose: Parse my CV (in markdown form), extract papers and create the "papers.html" section for my webpage.  
# Notes: It would be good to re-factor to this to use subprocess & a 'with' block for file IO 

import os

PAPER_START_LINE = "<!--- Start Papers --->"
PAPER_END_LINE = "<!--- End Papers --->"

def refresh_index(index_md_file_name): 
    os.system("pandoc %s -o index.html" % index_md_file_name)
    
def refresh_CV(cv_md_file_name): 
    os.system("pandoc %s -o cv.html" % cv_md_file_name)
    os.system("pandoc %s -o cv.pdf"  % cv_md_file_name)


refresh_CV("cv.md") 
refresh_index("index.md") 

papers = open("papers.md", "w")
cv = open("cv.md", "r")
papers.write("""<link href="markdown.css" rel="stylesheet"></link>
<script type="text/javascript">

  var _gaq = _gaq || [];
  _gaq.push(['_setAccount', 'UA-9193153-6']);
  _gaq.push(['_trackPageview']);

  (function() {
    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;
    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);
  })();

</script>
\n\n""")
papers.writelines(["Research Papers\n", "===============\n\n"])

write_line = False 
for line in cv:
    if line.strip() == PAPER_START_LINE:
        write_line = True 
    if line.strip() == PAPER_END_LINE:
        write_line = False 
    if write_line:
        papers.write(line)
     
cv.close()
papers.close()

os.system("pandoc papers.md -o papers.html")
os.system("rm papers.md") # this is not the source for papers - CV is. 

#os.system("git add cv.*; git add index.* ; git add papers.html; git commit -m 'Update CV'; git push origin master")
#print("Run git status in the johnjosephhorton.github.com directory") 


