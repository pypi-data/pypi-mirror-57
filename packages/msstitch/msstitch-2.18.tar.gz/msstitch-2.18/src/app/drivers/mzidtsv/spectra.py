from app.actions.mzidtsv import spectra as actions
from app.drivers.mzidtsv import MzidTSVDriver
from app.drivers.options import mzidtsv_options


class TSVSpectraDriver(MzidTSVDriver):
    lookuptype = 'spectra'
    outsuffix = '_spectradata.tsv'
    command = 'specdata'
    commandhelp = ('Add more data to a PSM table: retention time, biological set name, injection time, missed cleavage amount to PSM table.')

    def set_options(self):
        super().set_options()
        self.options.update(self.define_options(['lookupfn', 'spectracol', 'addbioset', 'addmiscleav'],
                                                mzidtsv_options))

    def get_psms(self):
        """Creates iterator to write to new tsv. Contains input tsv
        lines plus quant data for these."""
        self.header = actions.create_header(self.oldheader, self.spectracol, self.addbioset, self.addmiscleav)
        self.psms = actions.generate_psms_spectradata(self.lookup, self.fn, 
                self.oldheader, self.addbioset, self.addmiscleav)


