# mm => make mask

dirty_imagename = "dirty/" + "RCrA_13CO_all_dirty.image"
beamsize_major = 7.889
beamsize_minor = 4.887
pa = -77.412

chans = ["1", "398"]

# find the RMS of a line free channel
def derive_rms(chans):
    rms_pchan = []
    for i in chans:
        chanstat = imstat(imagename=dirty_imagename, chans=i)
        rms = chanstat["rms"][0]
        rms_pchan.append(rms)
    rms = sum(rms_pchan)

    print("rms = " + str(rms) + "Jy/beam")
    return rms


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


rms = derive_rms(chans)
make_mask(10)
