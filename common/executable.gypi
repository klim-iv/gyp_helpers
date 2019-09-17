# This file is part of Desktop App Toolkit,
# a set of libraries for developing nice desktop applications.
#
# For license and copyright information please follow this link:
# https://github.com/desktop-app/legal/blob/master/LEGAL

{
  'type': 'executable',
  'variables': {
    'win_subsystem': '2', # Windows application
  },
  'includes': [
    'common.gypi',
  ],
  'msvs_settings': {
    'VCLinkerTool': {
      'SubSystem': '<(win_subsystem)',
      'ImportLibrary': '<(PRODUCT_DIR)/<(_target_name).lib',
    },
  },
}
