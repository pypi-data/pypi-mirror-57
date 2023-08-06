# -*- coding: utf-8 -*-
"""Runs unit tests of on multiple implementations and platforms.
Provides some essential features for multi-platform development:

* easy selection of the used implementation
* detailed information of the actual called implementation for the test cases

"""
from __future__ import absolute_import
from __future__ import print_function

import os
import sys
import distutils.cmd

import yapyutils.config.capabilities

import setuplib

from setuptestx import SetupTestXError

from pythonids import PYVxyz, PYV27

__author__ = 'Arno-Can Uestuensoez'
__author_email__ = 'acue_sf2@sourceforge.net'
__license__ = "Artistic-License-2.0 + Forced-Fairplay-Constraints"
__copyright__ = "Copyright (C) 2019 Arno-Can Uestuensoez @Ingenieurbuero Arno-Can Uestuensoez"
__uuid__ = "1936395c-9621-42df-b5ec-9c4df4f1ff49"

__version__ = "01.01.042"

__product_family__ = "setuplib"
__product__ = "testx"
__product_component__ = "testx"


class TestX(distutils.cmd.Command):
    """Calls *unittest* in the subdirectory *tests*."""

    description = "Calls 'unittest' in the subdirectory 'tests'"
    user_options = [
        ('abs',                   'a',  "change all paths where possible to absolute"),
        ('prog=',                 'p',  "call program for tests, default 'CallCase.py'"),
        ('implementation=',       'i',  "the Python implementation, default is 'python' - CPython,"
                                        " change to e.g. 'jython' - needs eventually additional options. "
                                        "Tested values are: python, jython, ipython, ipy(IronPython), pypy"),
        ('name=',                 None, "The name of the package. "
                                        "Default: attribute of derived class self.name"),
        ('start=',                's',  "start package, e.g. 'tests' or 'tests.setuplib'"),
        ('testlib=',              'm',  "test library, default 'unittest discover'"),
        ('noexec',                'n',  "print only, do not execute"),
        ('print-env',             None, "print subprocess environment after an exec call"),
        ('print-ver',             None, "print the version of executed Python implementation"),
        ('print-vinfo',           None, "print information about executed implementation"),
        ('verbose',               None, "pass verbose flag, e.g. 'jython -v' or 'python -v'"),
        ('quiet',                 'q',  "silence the default verbosity, e.g. 'jython -q' or 'python -q'"),

        ('exe',                  'c',  """call provided string, e.g. python -c "print 'hello'" """),

        ('coff',                  'C',  "JYTHON: set cache off, sets '-Dpython.cachedir.skip=true'"),
        ('jyjar=',                'j',  "JYTHON: switch to call of 'java -jar <jython.jar>', "
                                        "requires absolute path, "
                                        "default is 'jython', "
                                        "for 'jython' the default names are 'java -jar jython.jar', "
                                        "for a valid jar-file 'java -jar /my/path/jython.jar'"
                                        "- enabled by '-i jython',"),
        ('jyjvm=',                'J',  "JYTHON: Java JVM options for Jyhon, "
                                        "e.g. '-J-Xmx512m' - enabled by '-i jython',"),
        ('jyprop=',               'D',  "JYTHON: properties '<prop>=<value>', "
                                        "e.g '-Dpython.path=/my/path', enabled by '-i jython'"),
    ]


    #: The provided capabilities of the builder and it's components.
    #: The values are loaded dynamically during bootstrap where the
    #: enabled packages are loaded and initialized.
    #: Each component is responsible for it's own data which is dynamically
    #: updated in place.
    #: Only activated components are loaded, which is dynamically defined
    #: by the command line parameters.
    #: When missing the *default* item defines the active component.
    #: At least one subcommand component is required.
    capabilities = yapyutils.config.capabilities.Capability(
        {
            "master_data": {
                "author": __author__,
                "author_email": __author_email__,
                "license": __license__,
                "copyright": __copyright__,
                "uuid": __uuid__,
                "product_family": __product_family__,
                "product": __product__,
                "product_component": __product_component__,
                "component_version": __version__,
                "product_version": __version__,
            },

            "components": {                          # see also 'user_options'
                "default":             "testx",      # call when no parameters are provided
                "testx":               "testx",      # call unittest in subdirectory "tests"
            },

            "testx": {
                "status":    True,  # enables the component
                "package":   None,  # the implementation
                
                "exit":      False, # exit after list

                "entry":     True,  # List entry points.
                "local":     True,  # List local defined commands.
                "standard":  True,  # List standard commands.

                "long":      False, # List long format, similar to shell command 'ls -l'.
                "format":    (      # Define display format.
                
                ),

            }
        }
    )


    def initialize_options(self):
        self.debug = None
        self.noexec = None
        self.quiet = None
        self.verbose = None
        self.break_on_err = None

        self.abs = None
        self.call = None
        self.calljy = None
        self.coff = None
        self.exe = None
        self.implementation = None
        self.jyjar = None
        self.jyjvm = None
        self.jyprop = None
        self.name = None
        self.print_env = None
        self.print_ver = None
        self.print_vinfo = None
        self.prog = None
        self.start = None
        self.testlib = None
        self.postfix = None
        
    def finalize_options(self):        

        # scan for any context-help request
        _help_request = setuplib.check_for_context_help(self)
        if _help_request:
            print(_help_request)
            sys.exit(0)

        # quick-and-dirty hack to resolve the inconsistency of
        # global and local verbose values of distutils
        try:
            # The context option is actually not set by the framework,
            # instead the global option is reset and intialized to
            # the number of occurances and passes to the initialization
            # of the memeber 'self.verbose'.
            # Thus the poll fails, while the value is already set via the framework.
            # See code distutils.dist.Distribution.
            # Anyhow...keeping it as a reminder.
            _v_opts = self.distribution.get_option_dict('build_docx')['verbose'][1]
            if _v_opts:
                self.verbose += 1
        except:
            # fallback to the slightly erroneous behavior when the interface 
            # of distutils changes
            pass


        # global and local verbose values of distutils
        try:
            # See verbose for description of the global option quiet.
            # See code distutils.dist.Distribution.
            _q_opts = self.distribution.get_option_dict('build_docx')['quiet'][1]
            if _q_opts:
                self.quiet += 1
        except:
            # fallback to the slightly erroneous behavior when the interface 
            # of distutils changes
            if self.quiet == None:
                self.quiet = 0
            pass


        if self.verbose != None:
            if os.name == 'java':
                # Jython - however - re-initializes the 'None' to '1',
                # when missing verbose parameter

                if not (set(sys.argv) & set(('-v', '--verbose'))): 
                    self.verbose -= 1

        if self.quiet != None:
            # quiet dominates

            self.quiet = True
            self.verbose = 0

        # debug
        if self.debug == None:
            self.debug = 0

#         if self.verbose_ext == None:
#             self.verbose_ext = 0


        if self.abs:
            self.abs = True

        if self.print_env != None:
            # environment
            self.print_env = True

        if self.print_ver != None:
            # version
            self.print_ver = True

        if self.print_vinfo != None:
            # sounding info
            self.print_vinfo = True

        if self.postfix == None:
            self.postfix = '_cases'

#FIXME:
#        print("4TEST:sys.implementation = " + str(self.implementation))

        if not self.implementation:
            # default is to use current called executable
            self.implementation = sys.executable

            # this is None in case of Jython!!!
            if not sys.executable and os.name == 'java':
                self.implementation = 'jython'

        #
        # check implementation to be used for tests via subprocess call
        #
        if (
                #
                # hard-coded for standard names for now
                # egg-and-chicken for the process to be started
                # not doing it twice :-)
                #
                self.implementation.endswith('jython')
                or
                self.implementation.endswith('jython.exe')
                or
                self.implementation.endswith('.jar')
           ):
            self.calljy = True

        if self.calljy:
            # call Jython for subprocess - enables Jython and Java specific options
             
            if self.jyjar == None:
                if self.abs:
                    self.implementation = os.path.abspath('jython')
                else:
                    self.implementation = 'jython'
            
            elif self.jyjar:
                if self.abs:
                    self.implementation = os.path.abspath('java') + ' -jar ' + str(self.jyjar)
                else:
                    self.implementation = 'java -jar ' + str(self.jyjar)
        
            else:
                if self.abs:
                    self.implementation = os.path.abspath('java') + ' -jar jython.jar '
                else:
                    self.implementation = 'java -jar jython.jar'

        else:
            # prohibit Jyhton and Java specific options
            
            if(
                self.jyjar
                or
                self.jyjvm
                or
                self.jyprop
              ):
                # has options for Java
                
                raise SetupTestXError("Java options require '-i=jython'")


        if not self.testlib:
            self.testlib = 'unittest discover'

        if self.noexec != None:
            self.noexec = True

        #
        # name of current package - serves as default for package subdiretory etc.
        #
        if self.name == None:
            self.name = self.distribution.metadata.name

        if not self.start:
            if os.path.exists('tests' + os.sep + self.name):
                # try literally
                self.start = 'tests.' + self.name
                
            elif os.path.exists('tests' + os.sep + 'py' + self.name + self.postfix):
                # check for python specific
                self.start = 'tests.py' + self.name
    
            else:
                # provoke the sounding error message            
                self.start = 'tests.' + self.name

        
        if not self.prog:
            self.prog = 'CallCase.py'


    def run(self):
        """Run command."""

        command = []
        command.append(str(self.implementation))

        if self.calljy:
            if self.jyjvm:
                command.append("-J" + str(self.jyjvm))

            if self.jyprop:
                command.append("-D" + str(self.jyprop))
    
            if self.coff:
                command.append("-Dpython.cachedir.skip=true")

        for s in range(self.verbose):
            # want each separate
            command.append("-v")
            
        if self.print_env:
            if (PYVxyz&PYV27) == PYV27:
                command.append('''-c "import os;\nfor k in sorted(os.environ.keys()):\n\tprint '%-30s = %s' % (str(k), str(os.environ[k]))"''')
            else:
                command.append('''-c "import os;\nfor k in sorted(os.environ.keys()):\n\tprint('%-30s = %s' % (str(k), str(os.environ[k])))"''')

        elif self.print_ver:
            command.append('''--version''')

        elif self.print_vinfo:
            if (PYVxyz&PYV27) == PYV27:
                command.append('''-c "from pythonids.pythondist import PYDIST_DATA;print PYDIST_DATA.__str__()"''')
            else:
                command.append('''-c "from pythonids.pythondist import PYDIST_DATA;print(PYDIST_DATA.__str__())"''')

        elif self.call:
            command.append('-c "' + self.call + '"')
        elif self.exe:
            command.append('-c "' + self.exe + '"')

        else:
            command.append("-m " + str(self.testlib))
            command.append("-s " + str(self.start))
            command.append("-p " + str(self.prog))

        if self.noexec:
            print(' '.join(command))
            exit_code = 0
        else:
            exit_code = os.system(' '.join(command))
        
        sys.exit(exit_code)

