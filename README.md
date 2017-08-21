MUSCLE Alignment WEB application

This Web application is a graphical interface for the MUSCLE protein alignment program developed by Robert C. Edgar in 2004. MUSCLE stands for MUltiple Sequence Comparison by Log-Expectation. It is a Bioinformatics Tool used to align sequences of proteins to determine how proteins may be similar and evolutionarily related. 

For more on the MUSCLE algorthm: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC390337/

Requirements:

Either Internet Explorer 7.0 and above. Mozilla Firefox 4.0 and above
Apple Safari 4.0 and above. Google Chrome 4.0 and above. Opera 10.0.

How to Use:

Alignment

Place a series of protein sequences in Fasta file format on the First TextBox. Click the Submit Button and the MUSCLE program will be called to perform the alignment which will appear in Clustalw format. It is advisable that the number of protein sequences do not go beyond 50. 

Save and Retreive Sequences

An interface with a database is also accessible from the Second TextArea. Select a sequence's Title from the database using the Search Input Box and click "Fetch Sequence". Your selected Sequence should appear on the Second TextArea in Fasta format. With the click of "Add to Query" button, it will then be added on tothe First TextBox. You may save sequences into the database with the "Save" Button.


Sample Sequences to Submit to MUSCLE:

>BAA00913.1 Rad51 protein [Saccharomyces cerevisiae]
MSQVQEQHISESQLQYGNGSLMSTVPADLSQSVVDGNGNGSSEDIEATNGSGDGGGLQEQAEAQGEMEDE
AYDEAALGSFVPIEKLQVNGITMADVKKLRESGLHTAEAVAYAPRKDLLEIKGISEAKADKLLNEAARLV
PMGFVTAADFHMRRSELICLTTGSKNLDTLLGGGVETGSITELFGEFRTGKSQLCHTLAVTCQIPLDIGG
GEGKCLYIDTEGTFRPVRLVSIAQRFGLDPDDALNNVAYARAYNADHQLRLLDAAAQMMSESRFSLIVVD
SVMALYRTDFSGRGELSARQMHLAKFMRALQRLADQFGVAVVVTNQVVAQVDGGMAFNPDPKKPIGGNIM
AHSSTTRLGFKKGKGCQRLCKVVDSPCLPEAECVFAIYEDGVGDPREEDE

>sp|P25453.1|DMC1_YEAST RecName: Full=Meiotic recombination protein DMC1
MSVTGTEIDSDTAKNILSVDELQNYGINASDLQKLKSGGIYTVNTVLSTTRRHLCKIKGLSEVKVEKIKE
AAGKIIQVGFIPATVQLDIRQRVYSLSTGSKQLDSILGGGIMTMSITEVFGEFRCGKTQMSHTLCVTTQL
PREMGGGEGKVAYIDTEGTFRPERIKQIAEGYELDPESCLANVSYARALNSEHQMELVEQLGEELSSGDY
RLIVVDSIMANFRVDYCGRGELSERQQKLNQHLFKLNRLAEEFNVAVFLTNQVQSDPGASALFASADGRK
PIGGHVLAHASATRILLRKGRGDERVAKLQDSPDMPEKECVYVIGEKGITDSSD

Sample Output of the Above Sequences:
MUSCLE (3.8) multiple sequence alignment
BAA00913.1                  MSQVQEQHISESQLQYGNGSLMSTVPADLSQSVVDGNGNGSSEDIEATNGSGDGGGLQEQ
sp|P25453.1|DMC1_YEAST      ------MSVTGTEI----------------------------------------------
                                    :: :::                                              
BAA00913.1                  AEAQGEMEDEAYDEAALGSFVPIEKLQVNGITMADVKKLRESGLHTAEAVAYAPRKDLLE
sp|P25453.1|DMC1_YEAST      ------------DSDTAKNILSVDELQNYGINASDLQKLKSGGIYTVNTVLSTTRRHLCK
                                        *. :  .::.:::**  **. :*::**...*::*.::*  :.*. * 

Built With

HTML5/CSS3/Javascript with JQuery
Python 3.3 with JINJA2
MySql and PHP


Authors

Jerald Macachor

Acknoledgements (Code and Assistance Contributed by the following)
Professor Joshua Orvis from Johns Hopkins University
CodexWorld https://www.codexworld.com/autocomplete-textbox-using-jquery-php-mysql/ 

License
GNU GNU Public License v3.0
