# energyusage

A Python package that measures the environmental impact of computation. Provides a function to
evaluate the energy usage and related carbon emissions of another function.
Emissions are calculated based on the user's location via the GeoJS API and that location's
energy mix data (sources: US E.I.A and eGRID for the year 2016).

## Installation

To install, simply `$ pip install energyusage`.

## Usage

To evaluate the emissions of a function, just call `energyusage.evaluate` with the function
name and the arguments it requires.

```python
import energyusage

# user function to be evaluated
def recursive_fib(n):
    if (n <= 2): return 1
    else: return recursive_fib(n-1) + recursive_fib(n-2)

energyusage.evaluate(recursive_fib, 40, pdf=True)
# returns 102,334,155
```
It will return the value of your function, while also printing out the energy usage report on the command line.
Optional keyword arguments:
* `pdf`(default = `False`): generates a PDF report, alongside the command-line utility
* `powerLoss` (default = `0.8`): accounts for PSU loss, can be set by user if known for higher accuracy of results
* `energyOutput` (default = `False`): prints amount of energy used by the process and time taken. The order is time, enery used, return of function
* `printToScreen` (default = `True`): controls whether there is a terminal printout of the package running

### Energy Report
The report that will be printed out will look like the one below. The second and third lines will show a real-time reading that disappears once the process has finished evaluating.
```
Location:                                                           Pennsylvania
--------------------------------------------------------------------------------
-------------------------------  Final Readings  -------------------------------
--------------------------------------------------------------------------------
Average baseline wattage:                                             2.35 watts
Average total wattage:                                               20.47 watts
Average process wattage:                                             18.12 watts
Process duration:                                                        0:00:01
--------------------------------------------------------------------------------
-------------------------------   Energy Data    -------------------------------
--------------------------------------------------------------------------------
                           Energy mix in Pennsylvania                           
Coal:                                                                     25.42%
Oil:                                                                       0.17%
Natural Gas:                                                              31.64%
Low Carbon:                                                               42.52%
--------------------------------------------------------------------------------
-------------------------------    Emissions     -------------------------------
--------------------------------------------------------------------------------
Effective emission:                                              4.44e-06 kg CO2
Equivalent miles driven:                                          1.82e-12 miles
Equivalent minutes of 32-inch LCD TV watched:                   2.74e-03 minutes
Percentage of CO2 used in a US household/day:                          1.46e-12%
--------------------------------------------------------------------------------
------------------------- Assumed Carbon Equivalencies -------------------------
--------------------------------------------------------------------------------
Coal:                                                      995.725971 kg CO2/MWh
Petroleum:                                                816.6885263 kg CO2/MWh
Natural gas:                                              743.8415916 kg CO2/MWh
Low carbon:                                                         0 kg CO2/MWh
--------------------------------------------------------------------------------
-------------------------     Emissions Comparison     -------------------------
--------------------------------------------------------------------------------
Mongolia:                                                        1.06e-05 kg CO2
Iceland:                                                         1.94e-06 kg CO2
Switzerland:                                                     4.68e-06 kg CO2
--------------------------------------------------------------------------------
--------------------------------------------------------------------------------
Process used:                                                       1.14e-05 kWh
```
The report is divided into several sections.
* **Final Readings**: Presents an average of:
	* *Average baseline wattage*: your computer's average power usage minus the process, ran for 10 seconds before starting your process
	* *Average total wattage*: your computer's average power usage while the process runs
	* *Average process usage*: the difference between the baseline and total, highlighting the usage solely from the specific process you evaluated
	* *Process duration*: how long your program ran for

* **Energy Data**: The energy mix of the location.

* **Emissions**: The effective CO<sub>2</sub> emissions of running the program one time and some real-world equivalents to those emissions.

* **Assumed Carbon Equivalencies**: The formulas used to convert from kWh to CO<sub>2</sub> based on the energy mix of the location (for international locations, see below for more information).

* **Emissions Comparison**: What the emissions would be for the same energy used in a representative group of US states and countries.

Not part of a section is the energy used by the process, which is optionally printed.

The PDF report contains the same sections, but does not include the process duration or the emissions comparison momentarily.

## Methodology
### Power Measurement
#### CPU
We calculate CPU power usage via the RAPL (Running Average Power Limit) interfaces found on Intel processors. These are non-architectural model-specific registers that provide power-related information
about the CPU. They are used primarily for limiting power consumption, but the Energy Status
register (MSR_PKG_ENERGY_STATUS) allows for power measurement.

The RAPL interface differentiates between several domains, based on the number of processors. For a single processor machine:
  * Package
  * Power planes:
      * Core
      * Uncore
  * DRAM

For a machine with multiple processors:
  * Package 0
  * Package 1
  * ...
  * Package n
  * DRAM

Presently, we use the Package domain (or a sum of all of the domains, for a multi-processor machine), which represents the complete processor package.

As outlined by [Vince Weaver](http://web.eece.maine.edu/~vweaver/projects/rapl/), there are multiple ways to access the RAPL interface data, namely:
 * Using perf_event interface
 * Reading the underlying MSR
 * Reading the files under `/sys/class/powercap/intel-rapl/`

We elected to use the final method because it is the only one that does not require sudo access.  We read the `energy_uj.txt` files inside the package folder(s) `intel-rapl:*`. These files represent the energy used in microjoules, and they update roughly every millisecond. The value in the file increases to the point of overflow and then resets. We take 2 readings with a delay in-between, and then calculate the wattage based on the difference (energy) and the delay (time). To avoid errors due to the reset of the file, we discard negative values.

For more information on the RAPL interface, consult the [Intel® 64 and IA-32 Architectures Software Developer's Manual](https://software.intel.com/sites/default/files/managed/39/c5/325462-sdm-vol-1-2abcd-3abcd.pdf).

#### GPU
To the package measurement we also add the power usage of the GPU for machines that have an Nvidia GPU that support the NVIDIA-smi program.

The NVIDIA-smi is a command-line utility that allows for the querying of information about the GPU. If the GPU is identified as valid, we use the built-in method to query the current wattage, and then convert the output into a float.

More  information on NVIDIA-smi can be found on the [Nvidia website](https://developer.nvidia.com/nvidia-system-management-interface).


### Calculating CO<sub>2</sub> Emissions
#### Location
In order to accurately calculate the CO₂ emissions associated with the computational power used, we determine the geographical location of the user via their IP address with the help of the [GeoJS](https://www.geojs.io/) API.  If the location cannot be determined, we use the United States as the default.

Location is especially important as the emissions differ based on the country's (and, in the case of the United States, the state's) energy mix.

#### Energy Mix Information
We obtained international energy mix data from the [U.S. Energy Information Administration data](https://www.eia.gov/beta/international/data/browser/#/?pa=0000000010000000000000000000000000000000000000000000000000u&c=ruvvvvvfvsujvv1vrvvvvfvvvvvvfvvvou20evvvfvrvvvvvvurs&ct=0&vs=INTL.44-2-AFG-QBTU.A&cy=2016&vo=0&v=H&start=2014&end=2016) for the year 2016. Specifically, we looked at the energy consumption of countries worldwide, broken down by energy source. For the data points labeled *(s)* (meaning that the value is too small for the number of decimal places shown), we approximated those amounts to 0. No data was available for, and thus we removed from consideration, the following: Former Czechoslovakia, Former Serbia and Montenegro, Former U.S.S.R., Former Yugoslavia, Hawaiian Trade Zone, East Germany and West Germany.

Our United States energy mix and emissions data was obtained from the [U.S. Environmental Protection Agency eGRID data](https://www.epa.gov/sites/production/files/2018-02/egrid2016_summarytables.xlsx) for the year 2016. We used the *State Resource Mix* section for displaying the energy mix, and the *State Output Emission Rates* section for calculating emissions in the United States. We did not use the *otherFossil* data as the values were predominantly 0 (and in cases in which the value was nonzero, it was below 1%).

As of July 2019, the most recent eGRID data was from the year 2016. We elected to use 2016 U.S. E.I.A. data for consistency between the data sources.

#### Conversion to CO<sub>2</sub>
Since the international data only contained an energy mix, and no emission data, we reverse-engineered the formulas used in the eGRID data. This gives us additionally consistency between the separate datasets.
* *Coal*: 2195.20 lbs CO<sub>2</sub>/MWh = 995.725971 kg CO<sub>2</sub>/MWh
* *Petroleum*: lbs CO<sub>2</sub>/MWh = 816.6885263 kg CO<sub>2</sub>/MWh
* *Natural gas*: 1639.89 lbs CO<sub>2</sub>/MWh = 743.8415916 kg CO<sub>2</sub>/MWh


## Related Work
* In their paper [*Energy and Policy Considerations for Deep Learning in NLP*](https://arxiv.org/abs/1906.02243), Strubell et. al not only analyze the computational power needed for training deep learning models in NLP, but further convert the data into carbon emissions and cost. Our tool aims to facilitate this analysis for developers in a single package. We do not consider cost, instead choosing to focus solely on the environmental impact. Further, we do not focus on a specific computational area. We also extend their analysis of carbon emissions by including international data on energy consumption and CO<sub>2</sub> emissions for localized analysis of the carbon footprint of the tested program.

## Limitations
* Due to the methods in which the energy measurement is being done (through the Intel RAPL
interface and NVIDIA-smi), our package is only available on Linux kernels that have the
RAPL interface and/or machines with an Nvidia GPU.

*  A country’s overall energy consumption mix is not necessarily representative of the mix of energy sources used to produce electricity (and even electricity production is not necessarily representative of electricity consumption due to imports/exports). However, the E.I.A. data is the most geographically comprehensive that we have found. We are working on obtaining even more accurate data.


## Acknowledgements
We would like to thank [Jon Wilson](https://www.haverford.edu/users/jwilson) for all his valuable insight with regards to the environmental aspect of our project.
