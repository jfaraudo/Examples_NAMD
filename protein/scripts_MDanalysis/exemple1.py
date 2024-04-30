import MDAnalysis as mda
simulacio = mda.Universe('input/system.psf','MD_100ns/MD.dcd')
for ts in simulacio.trajectory:
    temps_actual = ts.time
    frame_actual = ts.frame
    print(f"Frame: {frame_actual:4d},Time {temps_actual:4.0f} ps")

