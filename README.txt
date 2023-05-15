1. TITLE
FOM DETERMINATION FOR MEASUREMENTS MADE IN THE SPECTROMETER QUANTULUS 1220

2. INCLUDED FILES
- A script "FOM.py"
- Two example spectra files: One spiked sample and one background

3. PYTHON PACKAGES NEEDED TO RUN
- pandas
- numpy
- matplotlib.pyplot
- os

4. INTRODUCTION
This script is capable of determining the optimal counting window in terms of LLD by trying all possible combinations of starting and ending channels and selecting whichever yields the greatest FOM. This requires the files resulting of a measument of a spiked sample and a background vial of similar quenching to the real sample. For now, this script only works for measurement spectra stored in the #SP12 spectrum. A fix for this may be uploaded in the future if needed. This script can also be modified to satisfy individual needs.

5. HOW TO RUN
The script can be run for the example spectra included or for your own spectra. This can be done by replacing the example files with your own and running the script.

Both spectra need to be located in their respective folders. Only one spiked sample spectrum must be in the "patron" folder, while the background file should be in the "bkg" folder. The original file names may be kept. After launching the script, the spectrum from the spiked sample is shown together with an "amplified background spectrum". This is simply the background spectrum multiplied by a factor so it can be easily compared in shape to the spiked sample spectrum. Based on this figure, a maximum channel for trying needs to be provided in the console, which allows for much shorter calculation times. In the example spectra provided, 400 is a reasonable ending channel for the calculations, which is usual for 63Ni measurements in our case, as there are no relevant counts in the spiked spectrum beyond that channel. After inputting this maximum, both first and last channel which maximize the FOM are displayed together with a plot. It's the same plot as earlier, but two vertical black lines representing the selected channels are included. In this figure, it can often be seen that this method avoids integrating the spectrum in high-background areas.

6. Credits
This project was done by José Luis García León.