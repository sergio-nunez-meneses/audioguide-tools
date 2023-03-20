def write_ops_file(ops_file):
	from datetime import datetime as dt

	now = dt.now().strftime("%Y-%m-%d_%H-%M-%S")
	descriptors = get_descriptor_names(ops_file.opsfileAsString)
	full_path = f"{ops_file.ops_file_path}/{now}_{descriptors}_{ops_file.ops_file_name}"
	f = open(full_path, "w")
	f.write(ops_file.opsfileAsString)
	f.close()


def get_descriptor_names(file_content):
	from re import findall as f_all
	r = r"d\('([^']*)'"
	c = '-'
	return "-".join([d[:d.index(c)] + d.split(c)[1].capitalize() if c in d else d for d in f_all(r, file_content)])
