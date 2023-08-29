import matplotlib.ticker as mtick
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
import os
import matplotlib.font_manager as fm

def style_ticks_plot(ax, x_mayor_tick):
    '''
    x_mayor_tick: add mayor ticks every set value on x
    y_mayor_tick: add mayor ticks every set value on y  
    '''
    # set tick values on x: mayor and minor
    ax.xaxis.set_major_locator(mtick.MultipleLocator(x_mayor_tick))   # mayor tick on x
    x_minor_tick = x_mayor_tick*0.5
    ax.xaxis.set_minor_locator(mtick.MultipleLocator(x_minor_tick))   # minor tick on x

    # set tick values on y: mayor and minor
    #ax.yaxis.set_major_locator(mtick.MultipleLocator(y_mayor_tick)) # mayor tick on y
    #y_minor_tick = y_mayor_tick*0.5
    #ax.yaxis.set_minor_locator(mtick.MultipleLocator(y_minor_tick)) # minor tick on y

    # set amount of tick on y axe:
    ax.yaxis.set_major_locator(mtick.MaxNLocator(6))
    ax.yaxis.set_minor_locator(AutoMinorLocator(2))
    
    # format:
    #ax.yaxis.set_major_formatter(mtick.FormatStrFormatter("%.1e"))

def save_file(fig, output_file):
    '''
    this function save a figure with personal format and trim it
    put always fig
    put the filename
    '''
    fig.savefig(output_file, transparent=True, format="png", dpi=200)
    os.system('convert -trim {} {}'.format(output_file, output_file))


def set_plotstyle(plt, ax):
    '''
    This script set a personal style for plots on mathplotlib
    - font: serif
    - fontsize: 15 for title, xlabel, ylabel
    - aspect ration 1
    - fontsize for legend: 10
    - layout plot
    '''
    # Buscar una fuente serif
    serif_fonts = [font for font in fm.fontManager.ttflist if 'serif' in font.name.lower()]
    
    if serif_fonts:
        # Tomar la primera fuente serif encontrada
        serif_font = serif_fonts[0].name
        
        # Establecer la fuente para varios elementos del gráfico
        ax.set_title(ax.get_title(), fontname=serif_font, fontsize=15)
        ax.set_xlabel(ax.get_xlabel(), fontname=serif_font, fontsize=15)
        ax.set_ylabel(ax.get_ylabel(), fontname=serif_font, fontsize=15)
        ax.set_box_aspect(1)
        
        for label in (ax.get_xticklabels() + ax.get_yticklabels()):
            label.set_fontname(serif_font)

        # Configurar la fuente y otros parámetros de la leyenda
        legend = ax.legend(loc='best', fontsize=10, frameon=False)
        for text in legend.get_texts():
            text.set_fontname(serif_font)

        plt.tight_layout()


def molec_to_mg(mw):
    mw = mw   # molecular weitght in g by mol
    avogadro = 6.023*(10**23) # avogadro number in molecules by mol
    m_to_nm = 1*(10**9) # nm by m
    g_to_mg = 1000      # mg by g
    factor = (g_to_mg*mw*m_to_nm)/(avogadro)
    return factor
