"""Annotations for sky maps."""
import os
import tempfile

from astropy.io import fits
from astropy import table
from celery import group
from ligo.skymap.tool import ligo_skymap_flatten
from ligo.skymap.tool import ligo_skymap_from_samples
from ligo.skymap.tool import ligo_skymap_plot
from ligo.skymap.tool import ligo_skymap_plot_volume
from matplotlib import pyplot as plt

from . import gracedb
from ..import app
from ..jinja import env
from ..util.cmdline import handling_system_exit
from ..util.tempfile import NamedTemporaryFile


@app.task(ignore_result=True, shared=False)
def annotate_fits(filecontents, versioned_filename, graceid, tags):
    """Perform annotations on a sky map.

    This function downloads a FITS file and then generates and uploads all
    derived images as well as an HTML dump of the FITS header.
    """
    filebase = versioned_filename.partition('.fits')[0]
    header_msg = (
        'FITS headers for <a href="/api/superevents/{graceid}/files/'
        '{versioned_filename}">{versioned_filename}</a>').format(
            graceid=graceid, versioned_filename=versioned_filename)
    allsky_msg = (
        'Mollweide projection of <a href="/api/superevents/{graceid}/files/'
        '{versioned_filename}">{versioned_filename}</a>').format(
            graceid=graceid, versioned_filename=versioned_filename)
    volume_msg = (
        'Volume rendering of <a href="/api/superevents/{graceid}/files/'
        '{versioned_filename}">{versioned_filename}</a>').format(
            graceid=graceid, versioned_filename=versioned_filename)

    group(
        fits_header.s(versioned_filename) |
        gracedb.upload.s(
            filebase + '.html', graceid, header_msg, tags),

        plot_allsky.s() |
        gracedb.upload.s(
            filebase + '.png', graceid, allsky_msg, tags),

        annotate_fits_volume.s(
            filebase + '.volume.png', graceid, volume_msg, tags)
    ).delay(filecontents)


def is_3d_fits_file(filecontents):
    """Determine if a FITS file has distance information."""
    with NamedTemporaryFile(content=filecontents) as fitsfile:
        return 'DISTNORM' in table.Table.read(fitsfile.name).colnames


@app.task(ignore_result=True, shared=False)
def annotate_fits_volume(filecontents, *args):
    """Perform annotations that are specific to 3D sky maps."""
    if is_3d_fits_file(filecontents):
        (
            plot_volume.s(filecontents)
            |
            gracedb.upload.s(*args)
        ).apply_async()


@app.task(shared=False)
def fits_header(filecontents, filename):
    """Dump FITS header to HTML."""
    template = env.get_template('fits_header.jinja2')
    with NamedTemporaryFile(content=filecontents) as fitsfile, \
            fits.open(fitsfile.name) as hdus:
        return template.render(filename=filename, hdus=hdus)


@app.task(shared=False)
def plot_allsky(filecontents, ra=None, dec=None):
    """Plot a Mollweide projection of a sky map using the command-line tool
    :doc:`ligo-skymap-plot <ligo/skymap/tool/ligo_skymap_plot>`.
    """
    # Note: plt.style.context added as workaround for
    # https://github.com/astropy/astropy/issues/8004.
    with NamedTemporaryFile(mode='rb', suffix='.png') as pngfile, \
            NamedTemporaryFile(content=filecontents) as fitsfile, \
            plt.style.context({'text.usetex': False}, after_reset=True), \
            handling_system_exit():
        if ra is not None and dec is not None:
            ligo_skymap_plot.main([fitsfile.name, '-o', pngfile.name,
                                   '--annotate', '--radec', str(ra), str(dec)])
        else:
            ligo_skymap_plot.main([fitsfile.name, '-o', pngfile.name,
                                   '--annotate', '--contour', '50', '90'])
        return pngfile.read()


@app.task(priority=1, queue='openmp', shared=False)
def plot_volume(filecontents):
    """Plot a 3D volume rendering of a sky map using the command-line tool
    :doc:`ligo-skymap-plot-volume <ligo/skymap/tool/ligo_skymap_plot_volume>`.
    """
    # Note: plt.style.context added as workaround for
    # https://github.com/astropy/astropy/issues/8004.
    with NamedTemporaryFile(mode='rb', suffix='.png') as pngfile, \
            NamedTemporaryFile(content=filecontents) as fitsfile, \
            plt.style.context({'text.usetex': False}, after_reset=True), \
            handling_system_exit():
        ligo_skymap_plot_volume.main([fitsfile.name, '-o',
                                      pngfile.name, '--annotate'])
        return pngfile.read()


@app.task(shared=False)
def flatten(filecontents, filename):
    """Convert a HEALPix FITS file from multi-resolution UNIQ indexing to the
    more common IMPLICIT indexing using the command-line tool
    :doc:`ligo-skymap-flatten <ligo/skymap/tool/ligo_skymap_flatten>`.
    """
    with NamedTemporaryFile(content=filecontents) as infile, \
            tempfile.TemporaryDirectory() as tmpdir, \
            handling_system_exit():
        outfilename = os.path.join(tmpdir, filename)
        ligo_skymap_flatten.main([infile.name, outfilename])
        return open(outfilename, 'rb').read()


@app.task(shared=False, queue='openmp')
def skymap_from_samples(samplefilecontents):
    """Generate multi-resolution fits file from samples."""
    with NamedTemporaryFile(content=samplefilecontents) as samplefile, \
            tempfile.TemporaryDirectory() as tmpdir, \
            handling_system_exit():
        ligo_skymap_from_samples.main(
            ['-j', '-o', tmpdir, samplefile.name])
        with open(os.path.join(tmpdir, 'skymap.fits'), 'rb') as f:
            return f.read()
