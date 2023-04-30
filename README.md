# Natural_Systems_Simulation_Lab_ITMO

**Role:** Data Analyst | Business Analyst at ITMO University, Laboratory of Artificial Intelligence

**Department:** National Center for Cognitive Technologies -> Natural Systems Simulation Lab

## **Tasks:** 
### 1. Comparative analysis of reanalysis currents and existing actual currents at the locations of floating autonomous base stations (FABS) by ice-free periods
### Folder: rozes
#### Folders' description: 
The data in the datasets has been edited.
- **iceconc** - parsed data for FABS (variable - iceconc - ice-free periods)
- **iceconc/edited_dates** - deleted rows for iceonc > 0.5
- **model** - modelled data of ice (vectors (vomecrty, vozocrtx) of variables of direction and speed) 
- **model/prepared_model** - prepared modelled data of ice (vectors are preprocessed into variables of direction and speed) 
- **parsed_measurements** - parsed observations data from FABS
- **averaged_depths_(all)** - actual measurements averaged over the reanalysis horizons
- **rozes (model+parsed)** - models visualization (comparison of observations and modelled data)

**Technical requirements**

- The analysis should be carried out for the available observation dates from 2012.
- The analysis should include a comparison of data at locations FABS No. 1,11,12 (at depths of 3.4, 12.2, 25.4 m), FABS No. 5.10 (at depths of 3.4, 12.2, 25.4, 47.1 m).
- The analysis should be based on actual measurements averaged over the reanalysis horizons.

**Expected Results:**

- Uploading current data at FABS No. 1,5,10,11,12 (iceconc, vomecrty, vozocrtx).
- Analysis of currents with visualization in the format of velocity roses.

**Task:** 

Perform a comparison:
By deserted periods - reanalysis currents and actual currents at the locations of PAS No.1,5,10 (Kara Sea) 12,11 (Laptev Sea) for the available observation dates from 2012. 
On the horizons:
- depths for regular FABS - 3.4, 12.2, 25.4 mm
- depths for deep-sea FABS 5.10 - additionally at 47.1m
The actual measurements lead to the horizons of reanalysis by averaging.
It is ineeded to represent comparison to estimate the modeling error of iceberg propagation during drift by using **rose of speeds**.

### 2. Check the reasons for the systematic overestimation of the sea water temperature in the reanalysis
### Folder: vosaline_votemper
#### Folders' description: 
The data in the datasets has been edited.
- **check_vosaline** - parsed data for FABS 
- **check_vosaline/Avg FABS for different depths** - averaged data for chosen FABS for different depths
- **check_vosaline/Avg depths for 1 FABS** - averaged data for depths for one FABS
- **check_vosaline/Different depths for 1 FABS** - different depths for one FABS
- **check_vosaline/Distribution of FABS among depths** - different depths for different FABS
- **data** - parsed data for FABS (variables - vosaline, votemper)
- **data/grouped** - grouped data by datetime for averaged depths and ice-free periods
- **graphs/vosaline** - graphs for vosaline across depths 
- **graphs/votemper** - graphs for votemper across depths 

**Expected Result:**

Draw a graph where Y is the depth, and X is the salinity value (variable vosaline). Take the data from the storage and average over the winter.
