#!/usr/bin/env python2

import os
import sys
import errno
import re
import shutil

def main(work_dir):
	otls_dir = os.path.join(work_dir,'otls')
	otldict = {}

	for otl in os.listdir(otls_dir):
		match = re.match(r"(.*?)_{1,2}(\d+)_(\d+)(?:_(\d+))?.(?:(?:otl)|(?:hda))",otl)
		if match is None:
			continue
		(name, v0, v1, v2) = match.groups()
		ver = (v0, v1, v2)

		if name not in otldict:
			otldict[name] = {}
		otldict[name][ver] = otl

	release_dir = os.path.join(work_dir, 'release', 'otls')
	try:
		os.makedirs(release_dir)
	except OSError as e:
		if e.errno == errno.EEXIST:
			pass
	#purge
	print "purging old release:"
	for fname in os.listdir(release_dir):
		print "...removing %s" % fname
		os.remove(os.path.join(release_dir, fname))

	#copy new
	print "generating new release:"
	for assname,assvers in otldict.iteritems():
		assfile = assvers[max(assvers.keys())]
		print "...copying %s as %s" % (assfile, assname)
		shutil.copy2(os.path.join(otls_dir, assfile), os.path.join(release_dir, assname + '.hda'))


if __name__ == '__main__':
	main(os.path.dirname(os.path.normpath(sys.argv[0])))
