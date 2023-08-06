HEADER_ACCESSION = 'Accession'
HEADER_PROTEIN = 'Protein ID'
HEADER_PROTEINS = 'Protein ID(s)'
HEADER_GENE = 'Gene'
HEADER_GENEID = 'Gene ID'
HEADER_GENENAME = 'Gene Name'
HEADER_ASSOCIATED = 'Associated gene ID'
HEADER_DESCRIPTION = 'Description'
HEADER_COVERAGE = 'Coverage'
HEADER_NO_PROTEIN = '# Proteins'
HEADER_CONTENTPROT = 'Proteins in group'
HEADER_NO_UNIPEP = '# Unique peptides'
HEADER_NO_PEPTIDE = '# Peptides'
HEADER_NO_PSM = '# PSMs'
HEADER_NO_PSMS_SUFFIX = ' - # quanted PSMs'
HEADER_AREA = 'MS1 precursor area'
HEADER_NO_QUANT_PSM = '# Quantified PSMs'
HEADER_CV_QUANT_PSM = '# CV of quantified PSMs'
HEADER_PROBABILITY = 'Protein error probability'
HEADER_QVAL = 'q-value'
HEADER_PEP = 'PEP'
HEADER_QVAL_MODELED = 'q-value (linear model)'
HEADER_QSCORE = 'Q-score best peptide'
PICKED_HEADER = [HEADER_PROTEIN, HEADER_QSCORE]
ACCESSIONS = {
        False: HEADER_PROTEIN, 
        'genes': HEADER_GENEID,
        'assoc': HEADER_GENENAME,
        }
