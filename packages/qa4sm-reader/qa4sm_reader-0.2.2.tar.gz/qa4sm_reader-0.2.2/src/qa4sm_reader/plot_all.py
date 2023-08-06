# -*- coding: utf-8 -*-
import os
from qa4sm_reader.plotter import QA4SMPlotter
from qa4sm_reader.img import QA4SMImg
from qa4sm_reader import globals
import matplotlib.pyplot as plt

def plot_all(filepath, metrics=None, extent=None, out_dir=None, out_type='png',
             boxplot_kwargs=dict(), mapplot_kwargs=dict()):
    """
    Creates boxplots for all metrics and map plots for all variables. Saves the output in a folder-structure.

    Parameters
    ----------
    filepath : str
        Path to the *.nc file to be processed.
    metrics : set or list, optional (default: None)
        metrics to be plotted, if None are passed, all are plotted (that have data)
    extent : list
        [x_min,x_max,y_min,y_max] to create a subset of the values
    out_dir : [ None | str ], optional
        Parrent directory where to generate the folder structure for all plots.
        If None, defaults to the current working directory.
        The default is None.
    out_types : list, optional (default: [png, svg])
        File types, e.g. 'png', 'pdf', 'svg', 'tiff'...
        A list, a plot is saved for each type.
    **boxplot_kwargs : dict, optional
        Additional keyword arguments that are passed to the boxplot function.
    **mapplot_kwargs : dict, optional
        Additional keyword arguments that are passed to the mapplot function.
    """

    if not out_dir:
        out_dir = os.path.join(os.getcwd(), os.path.basename(filepath))
    img = QA4SMImg(filepath, extent=extent, ignore_empty=True)
    plotter = QA4SMPlotter(image=img, out_dir=out_dir)

    # === Metadata ===
    if not metrics:
        metrics = img.ls_metrics(False)
    fnames_maps, fnames_boxes = [], []

    for metric in metrics:
    # === load values and metadata ===
        if metric not in globals.metric_groups[3]:
            fns_box = plotter.boxplot_basic(metric, out_type=out_type,
                                            **boxplot_kwargs)
        else:
            fns_box = plotter.boxplot_tc(metric, out_type=out_type,
                                         **boxplot_kwargs)
        fns_maps = plotter.mapplot(metric, out_type=out_type, **mapplot_kwargs)
        plt.close('all')
        for fn in fns_box: fnames_boxes.append(fn)
        for fn in fns_maps: fnames_maps.append(fn)

    return fnames_boxes, fnames_maps

if __name__ == '__main__':
    from zipfile import ZipFile, ZIP_DEFLATED
    from os import path
    afile = r"H:\code\qa4sm-reader\tests\test_data\tc\3-ERA5_LAND.swvl1_with_1-C3S.sm_with_2-ASCAT.sm.nc"
    out_dir = r"C:\Temp\qa4smreader_plots\new"
    fnb, fnm = plot_all(afile, out_dir=out_dir, out_type='png')
    fnb_svg, fnm_svg = plot_all(afile, out_dir=out_dir, out_type='svg')

    with ZipFile(os.path.join(out_dir, 'myzip.zip'), 'w', ZIP_DEFLATED) as myzip:
        for pngfile in fnb + fnm:
            arcname = path.basename(pngfile)
            myzip.write(pngfile, arcname=arcname)
        for svgfile in fnb_svg + fnm_svg:
            arcname = path.basename(svgfile)
            myzip.write(svgfile, arcname=arcname)
            os.remove(svgfile)
