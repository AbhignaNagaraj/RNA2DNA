RNA2DNA is a Python-based tool designed to convert the three-dimensional structures of single-stranded RNA (ssRNA) into single-stranded DNA (ssDNA) structures. The tool takes an RNA structure in PDB format as input and produces a DNA structure as output.

How to Use RNA2DNA
Steps:
Download the Tool
Download the RNA2DNA.py script to your working directory.

Prepare Your Input File
Place the 3D structure file of the ssRNA in PDB format in the same directory as RNA2DNA.py.

Run the Tool
Use the following command in your terminal or command prompt:

bash
Copy code
python RNA2DNA.py file.pdb
Replace file.pdb with the name of your ssRNA PDB file.

Outputs
The tool generates the following output files in the same directory:

pre-DNA1.pdb: Intermediate ssDNA structure file.
pre-DNA2.pdb: Intermediate ssDNA structure file.
DNA.pdb: Final converted ssDNA structure file.
The DNA.pdb file is your final output and contains the 3D structure of the converted ssDNA.

Prerequisites
Before using RNA2DNA, ensure the following are installed on your system:

Python
RNA2DNA is compatible with Python 3.x. Download Python 

BioPandas
Install the biopandas package, which is required for handling PDB files:
pip install biopandas


Example
Input:
An ssRNA structure file named example.pdb.

Command:
python RNA2DNA.py example.pdb
Output:
Three files will be generated:

pre-DNA1.pdb
pre-DNA2.pdb
DNA.pdb (final ssDNA structure)
 
