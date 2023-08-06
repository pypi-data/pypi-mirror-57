# -*- coding: utf-8 -*-
#******************************************************************************
# ZYNTHIAN PROJECT: Zynthian LV2 Preset Converter
# 
# obxdfxb2lv2 class: Convert OBXD native fxb presets to LV2
# 
# Copyright (C) 2015-2019 Markus Heidt <markus@heidt-tech.com>
#
#******************************************************************************
# 
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of
# the License, or any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# For a full copy of the GNU General Public License see the LICENSE.txt file.
# 
#******************************************************************************


import os
import sys
import logging
import mmap
import re

from . import native2lv2

class obxd2lv2(native2lv2.native2lv2):
	port_map = {
		"0": "lv2_port_1",
		"1": "unused_1",
		"2": "volume",
		"3": "voicecount",
		"4": "tune",
		"5": "octave",
		"6": "bendrange",
		"7": "bendosc2only",
		"8": "legatomode",
		"9": "vibratorate",
		"10": "vfltfactor",
		"11": "vampfactor",
		"12": "asplayedallocation",
		"13": "portamento",
		"14": "unison",
		"15": "voicedetune",
		"16": "oscillator2detune",
		"17": "lfofrequency",
		"18": "lfosinewave",
		"19": "lfosquarewave"
,		"20": "lfosampleholdwave",
		"21": "lfoamount1",
		"22": "lfoamount2",
		"23": "lfoosc1",
		"24": "lfoosc2",
		"25": "lfofilter",
		"26": "lfopw1",
		"27": "lfopw2",
		"28": "osc2hardsync",
		"29": "xmod",
		"30": "osc1pitch",
		"31": "osc2pitch",
		"32": "pitchquant",
		"33": "osc1saw",
		"34": "osc1pulse",
		"35": "osc2saw",
		"36": "osc2pulse",
		"37": "pulsewidth",
		"38": "brightness",
		"39": "envelopetopitch",
		"40": "osc1mix",
		"41": "osc2mix",
		"42": "noisemix",
		"43": "filterkeyfollow",
		"44": "cutoff",
		"45": "resonance",
		"46": "multimode",
		"47": "filter_warm",
		"48": "bandpassblend",
		"49": "fourpole",
		"50": "filterenvamount",
		"51": "attack",
		"52": "decay",
		"53": "sustain",
		"54": "release",
		"55": "filterattack",
		"56": "filterdecay",
		"57": "filtersustain",
		"58": "filterrelease",
		"59": "envelopedetune",
		"60": "filterdetune",
		"61": "portamentodetune",
		"62": "pan1",
		"63": "pan2",
		"64": "pan3",
		"65": "pan4",
		"66": "pan5",
		"67": "pan6",
		"68": "pan7",
		"69": "pan8",
		"70": "unused_2",
		"71": "economymode",
		"72": "lfosync",
		"73": "pwenv",
		"74": "pwenvboth",
		"75": "envpitchboth",
		"76": "fenvinvert",
		"77": "pwofs",
		"78": "leveldif",
		"79": "selfoscpush",
		"80": "unused_3",
	}

	def __init__(self, args, bank_per_file=False):
		self.plugin_name = 'Obxd'
		self.plugin_uri = 'https://obxd.wordpress.com'
		self.preset_ext = '.fxb'

		super().__init__(args, True)


	def parse_preset(self, preset):
		# Parse FXB file
		data = ''
		with open(preset['fpath'], 'rb', 0) as f, mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as s:
			startOfData = s.find(b'<programs>')
			if startOfData != -1:
				while not data:
					try:
						data = s.readline()[startOfData:-1].decode("UTF-8")
					except Exception  as e:
						logging.error(e)
			s.close()

		#logging.debug(data)
		#logging.debug("*******************************************")
		programs = re.findall('<program programName="(.*?)" (.*?)/>', data)

		preset_data = []
		for program in programs:
			#logging.info(program)
			# Get ports data
			ports = {}
			for port in re.findall('(\d*)="(.*?)"', program[1]):
				port_id = str(port[0])
				if port_id in self.port_map:
					ports[self.port_map[port_id]] = port[1]

			preset_data.append({
				'name': self.sanitize_text(program[0]),
				'bank': preset['bank'],
				'ports': ports
			})

		#logging.debug(preset_data)
		return preset_data


#******************************************************************************
