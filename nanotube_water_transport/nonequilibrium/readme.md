Example of simulation of water flow across the CNT under external pressure difference

The pressure difference between the two ends of the CNT is created by an external force applied as a TCL force.
See here for a tutorial/introduction to the use of external forces in NAMD:
https://www.ks.uiuc.edu/Training/Tutorials/science/forces/forces-tutorial-html/node2.html

The value of the external force is specified in NAMD units of kcal/mol*Angstrom. 

The applied pressure difference can be calculated by multipliying the number of molecules to which the pressure is applied, by the force divided by the area in the directions perpendicular to the force.Since the dimensions of the simulaiton box are given in Angstrom, the unit of pressure is Kcal/(mol* Angs^3) which is 6.95 GPa (69.5 kbar)
