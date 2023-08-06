# PyCHAM: Python CHemistry with Aerosol Microphysics Box Model

Welcome to the PyCHAM.  Funding has been provided from the [EUROCHAMP-2020 research project](http://www.eurochamp.org).  Please contact Simon O'Meara (simon.omeara@manchester.ac.uk) with any issues, comments or suggestions.

PyCHAM is an open-access computer code (written in Python) for simulating aerosol chambers.  It is supplied under the GNU General Public License v3.0.

The programme is controlled via a graphical user interface (GUI).  There are two options for installing, via conda and via pip. 


## conda Install

1. Download the PyCHAM repository from github.com/simonom/PyCHAM or data.eurochamp.org/modelling-tools/

2. Download and install the package manager Anaconda using the following address and selecting the appropriate operating system version: https://www.anaconda.com/distribution/#download-section

3. To set-up PyCHAM, use the terminal/command prompt, cd to the directory where the PyCHAM package is stored, then use the following command to install: conda env create -f PyCHAM_OSenv.yml -n PyCHAM, where OS is replaced by your operating system name (win (for Windows), lin (for Linux), mac (for Mac))

4. Now the environment is set up you can activate it by: conda activate PyCHAM

5. Install complete

## pip Install

1. Inside the terminal/command prompt, create a virtual env using venv: python -m venv PyCHAM

2. cd to this environment then activate: source bin/activate

3. Install PyCHAM from the PyPi site: python -m pip install --upgrade PyCHAM

4. cd to where PyCHAM installed: cd lib/python3.6/site-packages

5. Although several PyCHAM dependencies are installed along with PyCHAM, the SUNDIALS package is currently not available on PyPi (true on 14/11/2019), however this package is required by the Assimulo package.  Therefore, please follow the instructions to install SUNDIALS and Assimulo on the PyPi Assimulo page.  Please also install the openbabel package. 

6. Install complete

## Once Installed

1. For model inputs, ensure you have: a .txt file chemical reaction scheme, a .xml file for converting species names to SMILE strings and a .txt file stating values of model variables (e.g. temperature) - see details about these three files below

2. Now you are ready to run the model: python PyCHAM

3. Follow the gui directions (see below for details on the chemical scheme, xml and model input files)

4. The 'run model' button starts the simulation - results will be saved in the output folder in your PyCHAM directory

5. The 'plot results' button produces (and saves in the output folder) two figures, the first called contours.png that shows the particle number distribution, SOA mass and particle number concentration against time, and the second called gas_pbb.png that shows the gas-phase concentrations of initial components with time  

## Unit Testing, Integration Testing and Example Run

Unit tests for PyCHAM modules can be found in the PyCHAM/Unit_Testing folder in the Github repository.  To use, cd to this folder and use python test_module.py with module replaced by the name of the module to be tested.

Integration testing can be completed using the '.travis.yml' file at the website: travis-ci.org.

The example run output is saved in output/Example_Run/Example_output in the Github repository.  To reproduce this (e.g. for testing), use the inputs/Example_Run.txt for the chemical scheme, inputs/Example_Run_xml.xml for the xml file and inputs/Example_Run_inputs.txt for the model inputs.  Note that the example output was produced using version 0.2.1 of PyCHAM.

## Chemical Scheme .txt file

An example chemical scheme .txt file is given in the inputs folder (of the Github repository), called 'Example_Run.txt', which has been obtained
from the [Master Chemical Mechanism website](http://mcm.leeds.ac.uk/MCM/) and modified.

// can be used for preceding comments, as in the example.

Equations should adhere to the syntax in the following standard expression for an equation: % rate coefficient equation : reactant1 + reactant2 = product1 + product2 ;
Each equation should be represented on a new line.


The rate coefficients must adhere to the following rules:
The expression for the rate coefficient can use Fortran type scientific notation or python type; acceptable math functions: EXP, dsqrt, dlog, LOG, dabs, LOG10, numpy.exp, numpy.sqrt, numpy.log, numpy.abs, numpy.log10; MCM (master chemical mechanism) rate constants are accepted, e.g. KMT01, as are MCM photolysis rates, e.g. J<1> ;rate coefficients may be functions of TEMP, RH, M, N2, O2 where TEMP is temperature (K), RH is relative humidity (0-1), M, N2 and O2 are the concentrations of third body, nitrogen and oxygen (# molecules/cc (air)) - these concentrations are calculated automatically as a function of temperature and pressure inside eqn_parser.py; rate coefficients may also be a function of MCM names such as RO2.


## Chemical Scheme .xml file

An example is given in the inputs folder (of the Github repository), called 'Examples_Run_xml.xml'.  It has a two line header, the first states that the mechanism is beginning (`<mechanism>`) and the second states that the species definition is beginning (`<species_defs>`).  The end of the species list must be marked (`</species_defs>`) and finally, the end of the mechanism must be marked (`</mechanism>`). 

Beneath this, every species included in the reactions of the chemical scheme must have its SMILES string given.


## Model Variables .txt File

An example is provided in the inputs folder (of the Github repository), called 'Example_Run_inputs.txt' , this must include the values for the following variables separated by a return (so one line per variable), note that if a variable is irrelevant for your simulation, it can be left empty (e.g. voli = ):

Res_file_name = Name of folder to save results to

Total_model_time = Simulation time (s)

Time_step = Maximum time interval for ode (s)

Recording_time_step = Time interval for recording results (s)

Number_size_bins = Number of size bins (excluding wall), please use zero if no particles to be modelled

lower_part_size = Radius of smallest size bin boundary (um)

upper_part_size = Radius of largest size bin boundary (um)

kgwt = mass transfer coefficient of vapour-wall partitioning (m3/g.s)

eff_abs_wall_massC = effective absorbing wall mass concentration (g/m3 (air))

Temperature = Temperature (K)

PInit = the chamber pressure (Pa)

RH = Relative Humidity (fraction, 0-1)

lat = representative latitude (degrees) for light intensity (if lights used)

lon = representative longitude (degrees) for light intensity (if lights used)

daytime_start = representative time of the day for light intensity (s since midnight)

act_flux_path = path where the text file for indoor actinic flux is stored, this 
				should have wavelengths in the first column in nm, followed by 
				actinic flux in the second column in photon/cm2/nm/s.  Columns should be
				separated by a tab.

ChamSA = Chamber surface area (m2)

nucv1 = Nucleation parameterisation value 1

nucv2 = Nucleation parameterisation value 2

nucv3 = Nucleation parameterisation value 3

nuc_comp = Index of component contributing to nucleation (only one index allowed, can be absolute or relative)

new_partr = Radius of newly nucleating particles (cm), must be a scalar, can be left empty

inflectDp = Particle diameter wall loss kernel inflection point (m)

Grad_pre_inflect = Gradient of particle wall loss before inflection (/s)

Grad_post_inflect = Gradient of particle wall loss after inflection (/s)

Kern_at_inflect = Wall loss kernel value at inflection (/s)

Rader_flag = 0 to use the particle wall loss parameter values given above or
			 1 to the Rader and McMurry (1983) method for particle wall loss, which
			 uses the chamber surface area given by ChamSA above

C0 = Initial concentrations of any trace gases input at the experiment's start (ppb)

Comp0 = Names of trace gases present at start (in the order corresponding to their 
		concentrations in C0).  Note, this is case sensitive, with the case matching that 
		in the xml file

voli = index of components with vapour pressures stated in volP (multiple indices allowed, can be absolute or relative)

volP = vapour pressures (Pa) of components with indices given in voli

pconc = total particle concentration at start of experiment (seed particles) 
		(# particles/cc (air)), must be a scalar

std = geometric mean standard deviation of seed particle number concentration 
		(dimensionless), must be a scalar

loc = shift of lognormal probability distribution function for seed particles 
	number-size distribution (um), must be a scalar

scale = scaling factor of lognormal probability distribution function for seed 
	particles (dimensionless), must be a scalar

core_diss = core dissociation constant (for seed component) (dimensionless), must be a scalar

light_time = times (s) for light status, corresponding to the elements of light_status
				(below), minimum requirement is start (0.0) and total time of the 
				experiment 

light_status = 1 for lights on and 0 for lights off, with times given in light_time 
				(above), minimum requirement is stating the status at the start and end
				time of the experiment
	
## Acknowledgements

This project has received funding from the European Union’s Horizon 2020 research and innovation programme under grant agreement No 730997.