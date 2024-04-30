import MDAnalysis as mda

#load simulaiton files
simulacio = mda.Universe('input/system.psf','MD_100ns/MD.dcd')

#select protein
proteina = simulacio.select_atoms("protein")

#Output file
fitxer= open('Rgir.dat', 'w') 
fileheader="# time(ps) Radi gir (A)\n"
fitxer.write("# time(ps) Radi gir (A)\n")

#Loop: calculate
for ts in simulacio.trajectory:
    temps_actual = round(ts.time)
    frame_actual = ts.frame
    rgir = proteina.radius_of_gyration()
    
    #print data
    print(f"Frame: {frame_actual:4d},Time {temps_actual:4.0f} ps, R= {rgir:.4f} A")
    #save data
    fitxer.write(f'{temps_actual} {rgir}\n') #save number of monomers

