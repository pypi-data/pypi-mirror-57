# Create IGoR models and calculate the generation probability of V(D)J and
# CDR3 sequences. Copyright (C) 2019 Wout van Helvoirt

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


"""Contains a collection of commandline processing functions."""


def dynamic_cli_options(parser, options):
    """Semi-dynamically adds options to the given commandline parser.

    Parameters
    ----------
    parser : argparse.ArgumentParser
        ArgumentParser to use for appending options.
    options : dict
        A Python dict with key being the full name of the option. The value is a dict that corresponds to input arguments of
        the ArgumentParser.add_argument function. Make sure surround the 'type' argument value with quotes.

    Returns
    -------
    argparse.ArgumentParser
        Containing the expected commandline arguments. Note that the commandline arguments are not yet parsed.

    """
    # Semi-dynamically create the argparse arguments from given inputs.
    for name, kwargs in options.iteritems():
        kwargs_str = ""
        for (option, value) in kwargs.iteritems():
            if isinstance(value, str) and not option == 'type':
                kwargs_str += ', {}="{}"'.format(option, value)
            else:
                kwargs_str += ', {}={}'.format(option, value)
        eval('parser.add_argument("{0}"{1})'.format(name, kwargs_str))

    # Return the updated parser.
    return parser
