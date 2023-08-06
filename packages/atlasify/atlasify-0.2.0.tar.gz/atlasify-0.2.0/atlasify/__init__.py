"""
The atlasify package provides the method atlasify() which applies ATLAS style
to matplotlib plots.
"""

from matplotlib import rcParams
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
from matplotlib.transforms import ScaledTranslation, IdentityTransform

rcParams['font.family'] = 'sans-serif'
rcParams['font.sans-serif'] = ['Arial']

__version__ = '0.2.0'

FONT_SIZE = 16
LABEL_FONT_SIZE = 16
SUB_FONT_SIZE = 12
LINE_SPACING = 1.2
PT = 1 / 72  # 1 point in inches

def enlarge_yaxis(axes, factor=1):
    """
    Enlarges the y-axis by the given factor. A factor of 1 has no effect. The
    lower boundary of the y-axis is not affected.
    """
    ylim = axes.get_ylim()
    y_upper = ylim[0] + (ylim[1] - ylim[0]) * factor
    axes.set_ylim((ylim[0], y_upper))


def _indent(outside):
    """
    Return the base point indent of the ATLAS badge.
    """
    return (2 if outside else 10) * PT

def _offset(outside, subtext):
    """
    Return the vertical offset of the base point of the ATLAS badge.
    """
    offset = -(5 + FONT_SIZE)  # Inside

    if outside:
        offset = 5  # Outside
        if isinstance(subtext, str):
            offset += LINE_SPACING * SUB_FONT_SIZE * (subtext.count("\n") + 1)

    return offset * PT

def atlasify(atlas=True, subtext=None, enlarge=None, axes=None, outside=False):
    """
    Applies the atlas style to the plot. If the atlas argument evaluates to
    True, the ATLAS badge is added. If the atlas argument is a non-empty
    string, the string is appended after the badge.

    If the subtext argument is given, this argument is added on the line
    below. Multiple lines are printed separately.

    The enlarge factor defines how fare the y-axis should be extended
    to accommodate for the badge.

    If the axes argument is None, the currently active axes is used.

    If the outside argument is True, the label will be placed above the plot.
    """
    if enlarge is None:
        enlarge = 1 + 0.3 * (not outside)

    if axes is None:
        axes = plt.gca()

    enlarge_yaxis(axes, enlarge)

    axes.legend(frameon=False, loc=1)

    axes.tick_params("both", which="both", direction="in")
    axes.tick_params("both", which="major", length=6)
    axes.tick_params("both", which="minor", length=3)
    axes.tick_params("x", which="both", top=True)
    axes.tick_params("y", which="both", right=True)
    axes.xaxis.set_minor_locator(AutoMinorLocator())
    axes.yaxis.set_minor_locator(AutoMinorLocator())


    trans_indent = ScaledTranslation(_indent(outside), 0,
                                     axes.figure.dpi_scale_trans)
    trans_top = ScaledTranslation(0, _offset(outside, subtext),
                                  axes.figure.dpi_scale_trans)

    trans_sub = IdentityTransform()

    if atlas:
        badge = axes.text(0, 1, "ATLAS",
                          transform=axes.transAxes + trans_indent + trans_top,
                          fontdict={"size": FONT_SIZE,
                                    "style": "italic",
                                    "weight": "bold", })

        if isinstance(atlas, str):
            # Convert label with to dpi independent unit (pre-render)
            renderer = axes.figure.canvas.get_renderer()
            box = badge.get_window_extent(renderer)  # in display units
            box = axes.figure.dpi_scale_trans.inverted() \
                      .transform(box)  # in points
            badge_width = box[1][0] - box[0][0]

            trans_info = ScaledTranslation(0.4 * FONT_SIZE * PT + badge_width,
                                           0, axes.figure.dpi_scale_trans)
            axes.text(0, 1, atlas,
                      transform=axes.transAxes + trans_indent + trans_top +
                      trans_info, fontdict={"size": LABEL_FONT_SIZE, })

    if isinstance(subtext, str):
        trans_sub += ScaledTranslation(0, -LINE_SPACING * SUB_FONT_SIZE * PT,
                                       axes.figure.dpi_scale_trans)
        for line in subtext.split("\n"):
            axes.text(0, 1, line,
                      transform=axes.transAxes + trans_indent + trans_top +
                      trans_sub, fontdict={"size": SUB_FONT_SIZE, })
            trans_sub += ScaledTranslation(0, -LINE_SPACING * SUB_FONT_SIZE * PT,
                                           axes.figure.dpi_scale_trans)
