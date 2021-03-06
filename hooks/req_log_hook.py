import hooker
from wormnest.utils import check_filename_for_hook
import os, sys
import tempfile

@hooker.hook("pre_process")  # <-- This declares a hook when a GET request is made
def req_log_hook(request):
	log_line = "{method} - '{ua}' - '{url}'".format(
		method = request.method,
		ua = request.headers.get("User-Agent", "N/A"),
		url = request.full_path,
		)
	print (log_line)