# This file is part of Desktop App Toolkit,
# a set of libraries for developing nice desktop applications.
#
# For license and copyright information please follow this link:
# https://github.com/desktop-app/legal/blob/master/LEGAL

{
  'cmake_precompiled_header': '<(pch_header)',
  'cmake_precompiled_header_script': '<(DEPTH)/helpers/PrecompiledHeader.cmake',
  'msvs_precompiled_source': '<(pch_source)',
  'msvs_precompiled_header': '<(pch_header)',
  'xcode_settings': {
    'GCC_PREFIX_HEADER': '<(pch_header)',
    'GCC_PRECOMPILE_PREFIX_HEADER': 'YES',
  },
  'sources': [
    '<(pch_source)',
    '<(pch_header)',
  ],
}
