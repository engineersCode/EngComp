from pathlib import Path
from IPython.core.display import HTML


# To use this function, put this styles.py file somewhere where you 
#    can import it into a notebook with the usual type of import statement. 
#    It has to be on the path that Python searches looking for 
#    modules to import.
#
# Then all you have to do is run the function for each style: 
#
#    from styles import tufte
#    tufte()
#
# Note: 
#  - This function will affect other notebooks that you open in the same 
#    browser tab. 
#  - If you run `Restart kernel and clear all output` the display will revert 
#    to the default Jupyter styling until `tufte()` runs again. 
#
# To add the path to this styles.py file, execute this in the notebook with the correct path:
#
#    import sys
#    sys.path.append('../../../styles/')

def tufte():
    """Put either a relative or absolute path 
    for the CSS file into the Path( ) command. 
    """
    stylesheet = Path('../../../styles/tufte_inspired.css').read_text()
    return HTML(stylesheet)

def custom():
    stylesheet = Path("../../../styles/custom.css").read_text()
    return HTML(stylesheet)
