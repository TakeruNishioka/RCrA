# mm => make mask

dirty_imagename = "dirty/" + "RCrA_13CO_all_cube_dirty.image"
beamsize_major = 7.889
beamsize_minor = 4.887
pa = -77.412

# find the RMS of a line free channel
chanstat = imstat(imagename=dirty_imagename, chans="1")
rms1 = chanstat["rms"][0]
chanstat = imstat(imagename=dirty_imagename, chans="38")
rms2 = chanstat["rms"][0]
rms = 0.5 * (rms1 + rms2)

print("rms = " + str(rms) + "Jy/beam")


def make_mask(times_sigma):
    immath(
        imagename=dirty_imagename,
        expr="iif(IM0>" + str(times_sigma * rms) + ",1,0)",
        outfile="mask/" + str(times_sigma) + "sigma.im",
    )

    imsmooth(
        imagename="mask/" + str(times_sigma) + "sigma.im",
        major=str(2 * beamsize_major) + "arcsec",
        minor=str(2 * beamsize_minor) + "arcsec",
        pa=str(pa) + "deg",
        outfile="mask/" + str(times_sigma) + "sigma.im.sm",
    )

    immath(
        imagename="mask/" + str(times_sigma) + "sigma.im.sm",
        expr="iif(IM0>0.2,1,0)",
        outfile="mask/" + str(times_sigma) + "sigma_mask.im",
    )


make_mask(10)
