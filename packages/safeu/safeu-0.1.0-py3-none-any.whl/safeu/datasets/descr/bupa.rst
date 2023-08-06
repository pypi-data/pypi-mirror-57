BUPA liver disorders Database
=============================

Notes
-----
Data Set Characteristics:
	:Number of instances: 345
	:Number of attributes: 6 overall
	:Attribute information:
		- mcv		mean corpuscular volume
		- alkphos	alkaline phosphotase
		- sgpt		alamine aminotransferase
		- sgot 		aspartate aminotransferase
		- gammagt	gamma-glutamyl transpeptidase
		- drinks	number of half-pint equivalents of alcoholic beverages
					drunk per day
		- selector  field used to split data into two sets
	:Summary Statistics:

    ========= ==== ==== ======= =====
   	           Min  Max   Mean    SD
    ========= ==== ==== ======= =====
    mcv:       65   103  90.16   4.44
    alkphos:   23   138  69.87  18.32 
    sgpt:      4    155  30.41  19.48
    sgot:      5     82  24.64  10.05
    gammagt:   5    297  38.28  39.20
    drinks:    0     20   3.46   3.33
    ========= ==== ==== ======= ===== 

    :Missing values: none
    :Creators: BUPA Medical Research Ltd.
    :Donor: Richard S. Forsyth
             8 Grosvenor Avenue
             Mapperley Park
             Nottingham NG3 5DX
             0602-621676
    :Date: 5/15/1990


Relevant information:
    - The first 5 variables are all blood tests which are thought
      to be sensitive to liver disorders that might arise from
      excessive alcohol consumption.  Each line in the bupa.data file
      constitutes the record of a single male individual.
    - It appears that drinks>5 is some sort of a selector on this database.
      See the PC/BEAGLE User's Guide for more information.
	  
References
----------
   - None known other than what is shown in the PC/BEAGLE User's Guide
      (written by Richard S. Forsyth).