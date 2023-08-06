# -*- coding: utf-8 -*-
'''Simplicity masking and scoring classes.
'''
# 3rd-party packages
from colorama import Fore
import numpy as np
# module packages
from . import cli
from .common import *
#
# global constants
#
TERM_CHAR = '$'
#
# class definitions
#


class RunlengthSimplicity(SimplicityObject):
    '''Define simplicity by the number of repeated letters.

    '''

    def __init__(self, default_cutoff=DEFAULT_SIMPLICITY_CUTOFF):
        super().__init__(default_cutoff=default_cutoff)
        self.label = 'runlength'
        self.desc = 'runlength (repeated characters)'

    def _runlength(self, s):
        return [all([s[i + j + 1] == s[i] for j in range(self.cutoff - 1)])
                for i in range(len(s) - self.cutoff + 1)]

    def mask(self, seq, print_results=False):
        '''Mask high-simplicity positions in a string.

        :param s: Input string.
        :return: Input string with masked positions changed to lower-case.
        '''
        for pos in [i for i, masked in
                    enumerate(self._runlength(to_str(seq).upper()))
                    if masked]:
            if isinstance(seq, str):  # strings need to have whole length set
                seq = seq[:pos] + seq[pos:pos + self.cutoff].lower() + \
                    seq[pos + self.cutoff:]
            else:
                seq[pos:pos +
                    self.cutoff] = to_str(seq[pos:pos +
                                              self.cutoff]).lower()
        return super().mask(seq)


class LetterFrequencySimplicity(SimplicityObject):
    '''Define simplicity by the number of repeated letters.

    '''

    def __init__(self,
                 default_cutoff=DEFAULT_SIMPLICITY_CUTOFF,
                 window_size=None):
        global config_obj
        super().__init__(default_cutoff=default_cutoff)
        if window_size is None:
            try:
                self.window_size = config_obj.config_dict['simplicity_window']
            except KeyError:
                self.window_size = DEFAULT_SIMPLICITY_WINDOW
        else:
            self.window_size = window_size
        self.label = 'letterfreq%d' % self.window_size
        self.desc = 'letter frequency in window of %d residues' % self.window_size


    def mask(self, seq, print_results=False):
        '''Mask high-simplicity positions in a string.

        :param s: Input string.
        :return: Input string with masked positions changed to lower-case.
        '''
        out_str = to_str(seq)
        end_idx = len(out_str) - 1
        byte_arr = np.array([char for char in to_bytes(out_str.upper())])
        mask_positions = set()
        #
        # test character by character for number of occurrances over window
        #
        for char in set(byte_arr):  # test character by character
            char_positions = list(np.where(byte_arr == char)[0])
            while len(char_positions) >= self.cutoff:
                testpos = char_positions.pop(0)
                next_positions = char_positions[:self.cutoff - 1]
                if next_positions[-1] - testpos < self.window_size:
                    mask_positions = mask_positions.union(
                        set([testpos] + next_positions))
        #
        # mask everything
        #
        for pos in mask_positions:
            out_str = out_str[:pos] + out_str[pos].lower() + out_str[pos + 1:]

        if isinstance(seq, str):  # strings need to have whole length set
            seq = out_str
        else:  # may be MutableSeq that needs lengths
            seq[:end_idx] = out_str[:end_idx]
        return super().mask(seq)


class GenerisSimplicity(SimplicityObject):
    '''Define simplicity by the number of repeated letters.

    '''

    def __init__(self,
                 default_cutoff=DEFAULT_SIMPLICITY_CUTOFF,
                 window_size=None):
        super().__init__(default_cutoff=default_cutoff)
        if window_size is None:
            try:
                self.window_size = config_obj.config_dict['simplicity_window']
            except KeyError:
                self.window_size = DEFAULT_SIMPLICITY_WINDOW
        else:
            self.window_size = window_size
        self.label = 'generis%d' % self.window_size
        self.desc = 'pattern by BW xform in window of %d residues' % self.window_size

    def mask_pairs(self, s):
        return [all([s[i + j + 1] == s[i] for j in range(1)])
                for i in range(len(s) - 1)]

    def _bwt(self, s):
        '''Burrows-Wheeler Transform.

        :param s: Input string.  Must not contain TERMCHAR.
        :return: Transformed string.
        '''
        s = s + TERM_CHAR
        return ''.join([x[-1] for x in sorted([s[i:] + s[:i]
                                               for i in range(len(s))])])

    def _ibwt(self, s):
        '''Inverse Burrows-Wheeler Transform on uppercase-only comparisons.

        :param s: Transformed string with mixed upper and lower case.
        :return: Untransformed string with original order.
        '''
        L = [''] * len(s)
        for i in range(len(s)):
            L = sorted([s[i] + L[i] for i in range(len(s))],
                       key=str.upper)
        return [x for x in L if x.endswith(TERM_CHAR)][0][:-1]

    def merge_mask_regions(self, mask, max_run):
        "merge regions separated by less than max_run"
        runs = self.run_lengths(mask)
        for i in range(len(runs)):
            if runs[i] <= max_run:
                mask[i] = True
        return mask

    def unset_small_regions(self, mask, min_run):
        "merge regions separated by less than max_run"
        runs = self.run_lengths([int(not i) for i in mask])
        for i in range(len(runs)):
            if mask[i] and (runs[i] < min_run-1):
                mask[i] = False
        return mask


    def mask(self, seq, print_results=False):
        '''Mask high-simplicity positions in a string.

        :param s: Input string, will be converted to all-uppercase.
        :return: Input string with masked positions changed to lower-case.
        '''
        out_str = to_str(seq)
        end_idx = len(out_str) - 1
        upper_str = out_str.upper()
        # run-length mask in direct space
        dir_mask = self.mask_pairs(upper_str)
        dir_mask = self.merge_mask_regions(dir_mask, 3)
        dir_mask = self.unset_small_regions(dir_mask, self.cutoff)
        for pos in [i for i, masked in
                    enumerate(dir_mask)
                    if masked]:
            out_str = out_str[:pos] + out_str[pos:pos + 2].lower()\
                      + out_str[pos + 2:]
        if print_results:
            logger.info('     rlm: %s', colorize_string(out_str))
        # run-length mask in Burrows-Wheeler space
        bwts = self._bwt(upper_str)
        bwt_mask = self.mask_pairs(bwts)
        bwt_mask = self.merge_mask_regions(bwt_mask, 2)
        bwt_mask = self.unset_small_regions(bwt_mask, self.cutoff)
        for pos in [i for i, masked in
                    enumerate(bwt_mask)
                    if masked]:
            bwts = bwts[:pos] + bwts[pos:pos + \
                self.cutoff].lower() + bwts[pos + self.cutoff:]
        if print_results:
            logger.info('     bwt: %s', colorize_string(bwts))
        ibwts = self._ibwt(bwts)
        if print_results:
            logger.info('    ibwt: %s', colorize_string(ibwts))
        # add in mask from inverse-transformed string
        for pos in [i for i, char in
                    enumerate(ibwts) if char.islower()]:
            out_str = out_str[:pos] + out_str[pos].lower() + out_str[pos + 1:]
        if print_results:
            logger.info(' generis: %s', colorize_string(out_str))
        if isinstance(seq, str):  # strings need to have whole length set
            seq = out_str
        else:                    # may be MutableSeq that needs lengths
            seq[:end_idx] = out_str[:end_idx]
        return  super().mask(seq)

#
# Instantiations of classes.
#
NULL_SIMPLICITY = SimplicityObject()
RUNLENGTH_SIMPLICITY = RunlengthSimplicity()
LETTERFREQ_SIMPLICITY = LetterFrequencySimplicity()
GENERIS_SIMPLICITY = GenerisSimplicity()

@cli.command()
@click.option('--smooth/--no-smooth', default=True, is_flag=True,
              help='Finish with real-space smoothing.')
@click.option('--cutoff', default=DEFAULT_SIMPLICITY_CUTOFF, show_default=True,
              help='Maximum simplicity to keep.')
@click.option('-k', default=DEFAULT_K, show_default=True,
              help='k-mer size for score calculation.')
def demo_simplicity(smooth, cutoff, k):
    '''Demo self-provided simplicity outputs.

    :param cutoff: Simplicity value cutoff, lower is less complex.
    :param window_size: Window size for masking computation..
    :return:
    '''
    user_ctx = get_user_context_obj()
    simplicity_obj = user_ctx['simplicity_object']
    simplicity_obj.set_cutoff(cutoff)
    logger.info('Simplicity function is %s with cutoff of %d.',
                simplicity_obj.desc, cutoff)
    simplicity_obj.set_k(k)
    simplicity_obj.use_smoother(smooth)
    logger.info('           Mask window demo for %d-mers:', k)
    mask_test = 'AAAAAAAAAAaaaaAAAAAAAAAAAaaaaaAAAAAAAAAAAAaaaaaaAAAAAAAAAAAAAaaaaaaaAAAAAAAAAAAAAA'
    logger.info('      in: %s\n S-score: %s\n', mask_test,
                ''.join(['%X' % i for i in
                         simplicity_obj.score(mask_test)]))
    try:
        window_size = user_ctx['simplicity_window']
    except KeyError:
        window_size = DEFAULT_SIMPLICITY_WINDOW
    smoother_tests = [('L end', 'aAAAAAAAAAAAAA'),
                      ('R end', 'AAAAAAAAAAAAAa'),
                      ('singleton', 'AAAAAaAAAAAAAAaaaaAAAAA'),
                      ('non-windowed singleton', 'AaAAAAaAAAAaAAAAAaAAAAAaAAAAAA')]
    logger.info('Demo smoother with window size of %d' %simplicity_obj.k)
    for label, pattern in smoother_tests:
        logger.info('%s:  %s', label, colorize_string(pattern))
        smoothed = simplicity_obj.smoother(pattern)
        logger.info('smoothed: %s', colorize_string(smoothed))
    for desc, case in simplicity_obj.testcases:
        if case is '':
            logger.info('              %s', desc)
        else:
            logger.info('\n%s:', desc)
            logger.info('      in: %s', case)
            masked_str = simplicity_obj.mask(case, print_results=True)
            logger.info('     out: %s', colorize_string(masked_str))


@cli.command()
@click.argument('window_size')
def set_simplicity_window(window_size):
    '''Define size of simplicity window.
    '''
    global config_obj
    if window_size == ():
        try:
            window_size = config_obj.config_dict['simplicity_window']
            default = ''
        except KeyError:
            window_size = DEFAULT_SIMPLICITY_WINDOW
            default = ' (default)'
        logger.info('Window size is %d residues%s',
                    window_size, default)
    try:
        window_size = int(window_size)
    except ValueError:
        logger.error('Window size must be an integer value.')
        sys.exit(1)
    if window_size < 3:
        logger.error('Window size must be >=3.')
        sys.exit(1)
    config_obj.config_dict['simplicity_window'] = window_size
    logger.info(
        'Window size for letter-frequency simiplicity calculation is now %d residues.',
        window_size)
    config_obj.write_config_dict()

@cli.command()
@click.argument('infile', type=str)
@click.argument('outfile', type=str)
def colorize_fasta(infile, outfile):
    "Color lower-case parts of sequence."
    infilepath = Path(infile)
    outfilepath = Path(outfile)
    with infilepath.open(mode='rU') as infh:
        line = infh.readline()
        with outfilepath.open(mode='wt') as outfh:
            for line in infh:
                if line.startswith('>'):
                    outfh.write(line)
                else:
                    outfh.write(colorize_string(line))