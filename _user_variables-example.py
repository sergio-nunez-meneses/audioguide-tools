from audioguide_descriptors import _descriptors

_samples_path = "/path/to/samples"
_target_path = "/path/to/target"
_target_name = "file_name"
_output_path = "/path/to/output"

# Target
TARGET = tsf(f"{_target_path}/{_target_name}.wav", thresh=-40, offsetRise=1.1)

# Corpus
_instrument_name = "instrument_name"
CORPUS_GLOBAL_ATTRIBUTES = {
	"wholeFile": True,
	"recursive": True,
	"scaleDb":   "filenamedyn",
}
CORPUS = [
	csf(f"{_samples_path}/instrument_family/{_instrument_name}")
]

# Search
SEARCH = [
	spass("ratio_limit", d(_descriptors.amp.averaged.seg), maxratio=1),
	spass("closest", d(_descriptors.mfcc.averaged)),
]

# Superimposition
SUPERIMPOSE = si(maxSegment=4)

# Output
_descr_used = f"{_descriptors.amp.averaged.seg}+{_descriptors.mfcc.averaged}"
_output_file = f"{_output_path}/$TIME_{_target_name}_{_descr_used}_{_instrument_name}"

MAXMSP_OUTPUT_FILEPATH = None
OUTPUT_LABEL_FILEPATH = None
TARGET_SEGMENT_LABELS_FILEPATH = None

CSOUND_NORMALIZE = False
CSOUND_PLAY_RENDERED_FILE = False
CSOUND_RENDER_FILEPATH = f"{_output_file}.wav"
BACH_FILEPATH = f"{_output_file}.txt"
DICT_OUTPUT_FILEPATH = f"{_output_file}.json"
VERBOSITY = 2

# CSOUND_CSD_FILEPATH = None  # Error if not uncommented
# HTML_LOG_FILEPATH = None  # Error if uncommented
