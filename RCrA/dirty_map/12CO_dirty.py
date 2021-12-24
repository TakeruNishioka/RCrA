import datetime
import os

time_start = datetime.datetime.now()
print("CLEAN is Running")

# Define CLEAN parameters
vis = "RCrA_12CO_all.ms"
prename = "RCrA_12CO_all"
imsize = [1600, 1200]
cell = "1arcsec"
minpb = 0.2
restfreq = "230.538GHz"
outframe = "lsrk"
spw = "0~35"
width = "0.2km/s"
start = "-35km/s"
nchan = 401
robust = 0.5
phasecenter = "J2000 19h01m41 -36d57m00"

# Make initial dirty image
os.system("rm -rf dirty/" + prename + "_dirty.*")
tclean(
    vis=vis,
    imagename="dirty/" + prename + "_dirty",
    gridder="mosaic",
    pbmask=minpb,
    imsize=imsize,
    cell=cell,
    spw=spw,
    weighting="natural",
    # robust=robust,
    phasecenter=phasecenter,
    specmode="cube",
    restfreq=restfreq,
    width=width,
    start=start,
    nchan=nchan,
    outframe=outframe,
    veltype="radio",
    restoringbeam="common",
    mask="",
    niter=0,
    interactive=False,
)

time_finish = datetime.datetime.now()
print("END CLEAN")
print("start time : " + str(time_start))
print("finish time : " + str(time_finish))
