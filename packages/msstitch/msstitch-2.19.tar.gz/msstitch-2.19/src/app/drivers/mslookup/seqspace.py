from app.drivers.mslookup import base
from app.actions.mslookup import searchspace as preparation
from app.drivers.options import mslookup_options, sequence_options
from Bio import SeqIO


class SeqspaceLookupDriver(base.LookupDriver):
    """Creates an SQLite lookup DB from a FASTA file. Sequences are
    trypsinized and stored. It's possible to store sequences reversed
    for N-terminal falloff indexing, and it can be specified to cut
    tryptic before proline.
    """
    lookuptype = 'searchspace'
    command = 'seqspace'
    commandhelp = """Create a lookup DB from a FASTA file. Sequences are
    trypsinized and stored. It's possible to store sequences reversed
    for N-terminal falloff indexing, and it can be specified to cut
    tryptic before proline."""

    def __init__(self):
        super().__init__()
        self.infiletype = 'FASTA'

    def set_options(self):
        super().set_options()
        self.options['--dbfile'].update({'required': False, 'default': None})
        self.options.update(self.define_options(['falloff', 'proline', 'minlength'], mslookup_options))
        self.options.update(self.define_options(['trypsinize', 'miss_cleavage'], sequence_options))

    def create_lookup(self):
        preparation.create_searchspace(self.lookup, self.fn, self.minlength, self.proline,
                                       self.falloff, self.trypsinize, self.miss_cleavage)


class WholeProteinSeqspaceLookupDriver(base.LookupDriver):
    lookuptype = 'searchspace'
    command = 'protspace'
    commandhelp = """Create a full-length protein lookup DB from a FASTA file.
    Protein sequences are stored as short peptides starting from every one of
    the proteins' amino acids."""

    def __init__(self):
        super().__init__()
        self.infiletype = 'FASTA'

    def set_options(self):
        super().set_options()
        self.options['--dbfile'].update({'required': False, 'default': None})
        self.options.update(self.define_options(['minlength'],
                                                mslookup_options))

    def create_lookup(self):
        preparation.create_searchspace_wholeproteins(self.lookup, self.fn,
                                                     self.minlength)



class DecoySeqDriver(base.LookupDriver):
    outsuffix = '_decoy.fa'
    lookuptype = 'searchspace'
    command = 'makedecoy'
    commandhelp = """Create a decoy database from a FASTA file.
    tryp_rev reverses tryptic peptides
    prot_rev reverses full protein
    Both make sure no decoys are accidentally identical to a target sequence,
    unless --ignore-target-hits is passed"""
    # FIXME doesnt really fit in mslookup category
    # maybe we should dump the categories in next version

    def __init__(self):
        super().__init__()
        self.infiletype = 'FASTA'

    def set_options(self):
        super().set_options()
        self.options['--dbfile'].update({'required': False, 'default': None})
        self.options.update(self.define_options([
            'fn', 'outfile', 'scramble', 'ignoretarget', 'trypsinize', 
            'miss_cleavage', 'minlength', 'max_shuffle'], sequence_options))

    def run(self):
        outfn = self.create_outfilepath(self.fn, self.outsuffix)
        if self.lookup is None and not self.ignoretarget:
            self.initialize_lookup('decoychecker.sqlite')
            preparation.create_searchspace(self.lookup, self.fn, self.minlength, reverse_seqs=False, miss_cleavage=self.miss_cleavage)
        decoyfa = preparation.create_decoy_fa(self.fn, self.scramble, self.lookup, self.trypsinize, self.miss_cleavage, self.minlength, self.max_shuffle)
        with open(outfn, 'w') as fp:
            SeqIO.write(decoyfa, fp, 'fasta')


class TrypsinizeDriver(base.LookupDriver):
    outsuffix = '_tryp.fa'
    command = 'trypsinize'
    commandhelp = """Trypsinize a FASTA file"""

    def __init__(self):
        super().__init__()
        self.infiletype = 'FASTA'

    def set_options(self):
        super().set_options()
        self.options['--dbfile'].update({'required': False, 'default': None})
        self.options.update(self.define_options([
            'fn', 'outfile', 'miss_cleavage', 'minlength', 'proline'], sequence_options))

    def run(self):
        outfn = self.create_outfilepath(self.fn, self.outsuffix)
        with open(self.fn) as fp, open(outfn, 'w') as wfp:
            seqs = SeqIO.parse(fp, 'fasta')
            decoyfa = preparation.create_trypsinized(seqs, self.proline, self.miss_cleavage, self.minlength)
            SeqIO.write(decoyfa, wfp, 'fasta')
