#!/usr/bin/env python

"""
 *  File: get_video.py - Retrieves video parameters from videolectures.net URLs
 *
 *  Copyright (c) 2009 Uldis Bojars <captsolo@gmail.com>
 *
 *  This Program is free software; you can redistribute it and/or modify
 *  it under the terms of the GNU General Public License as published by
 *  the Free Software Foundation; either version 2, or (at your option)
 *  any later version.
 *
 *  This Program is distributed in the hope that it will be useful,
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 *  GNU General Public License for more details.
 *
 *  You should have received a copy of the GNU General Public License
 *  along with RTMPDump; see the file COPYING.  If not, write to
 *  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
 *  http://www.gnu.org/copyleft/gpl.html
 *
"""

from pprint import pprint
import re
import sys
import urllib2

def get_params(in_url):
    html = urllib2.urlopen(in_url).read()

    re_stream = re.search( r'streamer: "([^"]+)"', html ).groups()[0]
    re_path = re.search( r'file: "([^"]+)"', html ).groups()[0]
    re_param = re.search( r'swfobject.embedSWF\(([^\)]+)\)', html).groups()[0]

    return (re_stream, re_path, re_param)

def main(in_url):
    pprint( get_params(in_url) )

if __name__ == "__main__":
    main( sys.argv[1] )
