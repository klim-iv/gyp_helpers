# This file is part of Desktop App Toolkit,
# a set of libraries for developing nice desktop applications.
#
# For license and copyright information please follow this link:
# https://github.com/desktop-app/legal/blob/master/LEGAL

{
  'conditions': [
    [ 'build_win', {
      'libraries': [
        '-llibcrypto',
        '-llibssl',
        '-lWs2_32',
        '-lGdi32',
        '-lAdvapi32',
        '-lCrypt32',
        '-lUser32',
      ],
      'configurations': {
        'Debug': {
          'include_dirs': [
            '<(libs_loc)/openssl_1_1_1/include',
          ],
          'library_dirs': [
            '<(libs_loc)/openssl_1_1_1/out32.dbg',
          ],
        },
        'Release': {
          'include_dirs': [
            '<(libs_loc)/openssl_1_1_1/include',
          ],
          'library_dirs': [
            '<(libs_loc)/openssl_1_1_1/out32',
          ],
        },
      },
    }], [ 'build_mac', {
      'conditions': [[ 'not build_osx', {
        'xcode_settings': {
          'OTHER_LDFLAGS': [
            '<(libs_loc)/openssl_1_1_1/libssl.a',
            '<(libs_loc)/openssl_1_1_1/libcrypto.a',
          ],
        },
        'include_dirs': [
          '<(libs_loc)/openssl_1_1_1/include',
        ],
      }, {
        'xcode_settings': {
          'OTHER_LDFLAGS': [
            '<(libs_loc)/openssl/libssl.a',
            '<(libs_loc)/openssl/libcrypto.a',
          ],
        },
        'include_dirs': [
          '<(libs_loc)/openssl/include',
        ],
      }]],
    }], [ 'build_linux', {
      'include_dirs': [
        '/usr/local/desktop-app/openssl-1.1.1/include',
      ],
    }],
  ],
}
