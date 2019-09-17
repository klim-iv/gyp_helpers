# This file is part of Desktop App Toolkit,
# a set of libraries for developing nice desktop applications.
#
# For license and copyright information please follow this link:
# https://github.com/desktop-app/legal/blob/master/LEGAL

{
  'variables': {
    'moc_to_sources%': '0',
  },
  'rules': [{
    'rule_name': 'qt_moc',
    'extension': 'h',
    'outputs': [
      '<(SHARED_INTERMEDIATE_DIR)/<(_target_name)/moc/moc_<(RULE_INPUT_ROOT).cpp',
    ],
    'action': [
      '<(qt_loc)/bin/moc<(exe_ext)',

      # Silence "Note: No relevant classes found. No output generated."
      '--no-notes',

      '<!@(python -c "for s in \'<@(_defines)\'.split(\' \'): print(\'-D\' + s)")',
      # '<!@(python -c "for s in \'<@(_include_dirs)\'.split(\' \'): print(\'-I\' + s)")',
      '<(RULE_INPUT_PATH)',
      '-o', '<(SHARED_INTERMEDIATE_DIR)/<(_target_name)/moc/moc_<(RULE_INPUT_ROOT).cpp',
    ],
    'message': 'Moc-ing <(RULE_INPUT_ROOT).h..',
    'process_outputs_as_sources': '<(moc_to_sources)',
  }],
}
