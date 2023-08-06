#- * - coding : utf - 8 - * -
"""
Helping functions and consts for pyAgrum
"""

#aGrum Licence(GPL)
#-- -- -- -- -- -- -- -- -- -
#* This program is free software; you can redistribute it and / or modify *
#* it under the terms of the GNU General Public License as published by *
#* the Free Software Foundation; either version 2 of the License, or *
#*(at your option) any later version.*
#* *
#* This program is distributed in the hope that it will be useful, *
#* but WITHOUT ANY WARRANTY; without even the implied warranty of *
#* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.See the *
#* GNU General Public License for more details.*
#* *
#* You should have received a copy of the GNU General Public License *
#* along with this program; if not, write to the *
#* Free Software Foundation, Inc., *
#* 59 Temple Place - Suite 330, Boston, MA 02111 - 1307, USA.

from .pyAgrum import BayesNet
from .pyAgrum import Potential
from .pyAgrum import InfluenceDiagram
from .pyAgrum import VariableElimination
from .pyAgrum import BNDatabaseGenerator
from .pyAgrum import PythonDatabaseGeneratorListener
from .pyAgrum import InvalidArgument

def about():
  """
  about() for pyAgrum

  """
  print("pyAgrum version {0}".format('0.16.4'))
  print("(c) Pierre-Henri Wuillemin, Christophe Gonzales, Lionel Torti")
  print("    UPMC 2015")
  print("""
    This is free software; see the source code for copying conditions.
    There is ABSOLUTELY NO WARRANTY; not even for MERCHANTABILITY or
    FITNESS FOR A PARTICULAR PURPOSE.  For details, see 'pyAgrum.warranty'.
    """)

def availableBNExts():
    """ Give the list of all formats known by pyAgrum to save a Bayesian network.
    
    :return: a string which lists all suffixes for supported BN file formats.
    """
    return "bif|dsl|net|bifxml|o3prm|uai"

def loadBN(filename,listeners=None,verbose=False,**opts):
    """load a file with optional listeners and arguments
    
    :param filename: the name of the input file
    :param listeners: list of functions to execute
    :param verbose: whether to print or not warning messages
    :param system: (for O3PRM) name of the system to flatten in a BN
    :param classpath: (for O3PRM) list of folders containing classes
    :return: a BN from a file using one of the availableBNExts() suffixes.

    Listeners could be added in order to monitor its loading.

    Examples
    --------
    >>> import pyAgrum as gum
    >>>
    >>> # creating listeners
    >>> def foo_listener(progress):
    >>>    if progress==200:
    >>>        print(' BN loaded ')
    >>>        return
    >>>    elif progress==100:
    >>>        car='%'
    >>>    elif progress%10==0:
    >>>        car='#'
    >>>    else:
    >>>        car='.'
    >>>    print(car,end='',flush=True)
    >>>
    >>> def bar_listener(progress):
    >>>    if progress==50:
    >>>        print('50%')
    >>>
    >>> # loadBN with list of listeners
    >>> gum.loadBN('./bn.bif',listeners=[foo_listener,bar_listener])
    >>> # .........#.........#.........#.........#..50%
    >>> # .......#.........#.........#.........#.........#.........% | bn loaded
    """
    bn=BayesNet()

    extension=filename.split('.')[-1].upper()
    if extension=="BIF":
        warns=bn.loadBIF(filename,listeners)
    elif extension=="BIFXML":
        warns=bn.loadBIFXML(filename,listeners)
    elif extension=="DSL":
        warns=bn.loadDSL(filename,listeners)
    elif extension=="NET":
        warns=bn.loadNET(filename,listeners)
    elif extension=="O3PRM":
        warns=bn.loadO3PRM(filename,opts.get('system',''),opts.get('classpath',''),listeners)
    elif extension=="UAI":
        warns=bn.loadUAI(filename,listeners)
    else:
        raise InvalidArgument("extension "+filename.split('.')[-1]+" unknown. Please use among "+availableBNExts())

    if verbose:
      print(warns)

    bn.setProperty("name",filename)
    return bn

def saveBN(bn,filename):
    """
    save a BN into a file using the format corresponding to one of the availableWriteBNExts() suffixes.

    :parma bn(gum.BayesNet): the BN to save
    :param filename(str): the name of the output file
    """
    extension=filename.split('.')[-1].upper()
    if extension=="BIF":
        bn.saveBIF(filename)
    elif extension=="BIFXML":
        bn.saveBIFXML(filename)
    elif extension=="DSL":
        bn.saveDSL(filename)
    elif extension=="NET":
        bn.saveNET(filename)
    elif extension=="UAI":
        bn.saveUAI(filename)
    elif extension=="O3PRM":
        bn.saveO3PRM(filename)
    else:
        raise InvalidArgument("[pyAgrum] extension "+filename.split('.')[-1]+" unknown. Please use among "+availableBNExts())



def loadID(filename):
  """
  read a gum.InfluenceDiagram from a bifxml file

  :param filename: the name of the input file
  :return: an InfluenceDiagram
  """

  extension=filename.split('.')[-1].upper()
  if extension!="BIFXML":
    raise InvalidArgument("extension "+extension+" unknown. Please use bifxml.")

  diag=InfluenceDiagram()
  res=diag.loadBIFXML(filename)

  if not res:
    raise Exception("Error(s) in "+filename)

  diag.setProperty("name",filename)
  return diag


def fastBN(arcs,domain_size=2):
  """
  rapid prototyping of BN.

  :param arcs: dot-like simple list of arcs ("a->b->c;a->c->d" for instance). The first apparition of a node name can be
   enhanced with a "[domain_size]" extension. For instance "a[5]->b->c;a[2]->c->d" will create a BN with a variable "a"
   whos domain size is a.nbrDim()==5 (the second "a[2]" is not taken into account since the variable has already been created).
  :param domain_size: the domain size of each created variable.
  :return: the created pyAgrum.BayesNet
  """
  return BayesNet.fastPrototype(arcs,domain_size)

def getPosterior(bn, evs, target):
  """
  Compute the posterior of a single target (variable) in a BN given evidence


  getPosterior uses a VariableElimination inference.
  If more than one target is needed with the same set of evidence or if the same
  target is needed with more than one set of evidence, this function is not
  relevant since it creates a new inference engine every time it is called.

  :param bn:
  :type bn: pyAgrum.BayesNet
  :param evs: events map {name/id:val, name/id : [ val1, val2 ], ...}
  :type evs: dictionary
  :param target: variable name or id
  :return: posterior Potential
  """
  inf = VariableElimination(bn)
  inf.setEvidence(evs)
  inf.addTarget(target)
  inf.makeInference()
#creating a new Potential from posterior(will disappear with ie)
  return Potential(inf.posterior(target))


def generateCSV(bn, name_out, n, visible=False, with_labels=False, random_order=True):
  """
  generate a CSV file of samples from a bn.

  :param bn: the BN from which the sample is generated
  :type bn: pyAgrum.BayesNet
  :param name_out: the name for the output filename
  :type name_out: string
  :param n: the number of samples
  :type n: int
  :param visible: if True, show a progress bar
  :type visible: boolean
  :param with_labels: if True, use the labels of the modalities of variables in the csv. If False, use their ids.
  :type with_labels: boolean
  :param random_order: if True, the columns in the csv are randomized sorted
  :type random_order: boolean  
  :return: the log2-likelihood of the generated base
  """

  genere = BNDatabaseGenerator(bn)
  if visible:
    from pyAgrum.lib._utils.progress_bar import ProgressBar
    prog = ProgressBar(name_out + ' : ', 0, 100, 77, mode='static', char='#')
    prog.display()
    listen = PythonDatabaseGeneratorListener(genere)

    def whenStep(x, y):
      prog.increment_amount()
      prog.display()

    def whenStop(msg):
      prog.update_amount(100)
      prog.display()
      print()

    listen.setWhenProgress(whenStep)
    listen.setWhenStop(whenStop)

  if random_order:
    genere.setRandomVarOrder()
  ll=genere.drawSamples(n)

  genere.toCSV(name_out,with_labels)

  if visible:
    print("Log2-Likelihood : {}".format(ll))

  return ll
