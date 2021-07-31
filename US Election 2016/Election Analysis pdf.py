# Python libraries
from fpdf import FPDF
from datetime import datetime, timedelta
import os
from PIL import Image

WIDTH = 210
HEIGHT = 297

''' First Page '''

pdf = FPDF()
pdf.add_page()
pdf.image(r'Images Election\2016 election.png',0,0,WIDTH)


''' Second Page '''
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.cell(50, 30, 'Election Poll 2016 Analysis',ln=1)


pdf.set_font('Arial','', 10)
col1="The 2016 United States presidential election was the 58th quadrennial presidential election, held on Tuesday, November 8, 2016.\n\n";
pdf.multi_cell(180, 5, col1, 0, 1);

col1=" It was the fifth and most recent presidential election in which the winning candidate lost the popular vote.\n\n";
pdf.multi_cell(180, 5, col1, 0, 1);

pdf.set_font('Arial', 'B', 10)
col1="In this project I will analyze the results of political polls and answer some questions.\n\n";
pdf.multi_cell(180, 5, col1, 0, 1);

pdf.set_font('Arial','', 10)
col1="1. Who was being polled and what was their party affiliation?\n\n";
pdf.multi_cell(180, 5, col1, 0, 1);

col1="2. Did the poll results favor Trump or Clinton?\n\n";
pdf.multi_cell(180, 5, col1, 0, 1);

col1="3. How do undecided voters effect the poll?\n\n";
pdf.multi_cell(180, 5, col1, 0, 1);

col1="4. Can we account for the undecided voters?\n\n";
pdf.multi_cell(180, 5, col1, 0, 1);

col1="5. How did voter sentiment change over time?\n\n";
pdf.multi_cell(180, 5, col1, 0, 1);

col1="6. Can we see an effect in the polls from the debates?\n\n";
pdf.multi_cell(180, 5, col1, 0, 1);



''' Second Page '''
pdf.add_page()


pdf.image(r'Images Election\Chart1.png', 35,0,0,130)
pdf.image(r'Images Election\Chart2.png', 15,90,0,130-5)   
pdf.image(r'Images Election\Chart3.png',35,170,0,130)


''' Third Page '''
pdf.add_page()

pdf.image(r'Images Election\Chart4.png',0,0,0,130)

pdf.image(r'Images Election\Chart5.png', 0,120,0,130)    
  

          
''' Sixth Page '''
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.cell(50, 30, 'Conclusion',ln=1)
          
pdf.set_font('Arial','', 10)
col1="By the analysis of the charts above we can see that on the first chart most of the polls has no affiliation. And there is a larger amount of Democratic affiliation than Republicans.\n\n";
pdf.multi_cell(180, 5, col1, 0, 1);

col1="On the second chart, we can see between the affiliations who is the population (Likely voters, Registered Voters and Adults). The large amount is no affiliation likely voters and Register voters. Also, there are more Republicans Registered voters than Democrats\n\n";
pdf.multi_cell(180, 5, col1, 0, 1);

col1="On the third chart we see the average sentiment of all polls. Where both main candidates are pretty close so the undecided volters can make a big difference on the eletion day.\n\n";
pdf.multi_cell(180, 5, col1, 0, 1);

col1="Because the chart number four shows the diference between Trump and Clinton, a positive difference indicates a leaning towards Trump in the polls. You can see that Hillary started on a better position but over time the sentiment mixed with spikes in favor of Trump.\n\n";
pdf.multi_cell(180, 5, col1, 0, 1);


col1="Finally, according to the last chart and the debates lines printed on it, we can see the sentiment changing up to october.\n\n";
pdf.multi_cell(180, 5, col1, 0, 1);

    
pdf.output('Election 2016.pdf', 'F')
