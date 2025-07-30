# Copyright 2022-2025 David Robillard <d@drobilla.net>
# SPDX-License-Identifier: 0BSD OR ISC

project(
  'lv2kit',
  ['c'],
  default_options: [
    'b_ndebug=if-release',
    'buildtype=release',
    'c_std=c99',
    'c_winlibs=',
    'cpp_std=c++17',
    'cpp_winlibs=',
  ],
  license: 'ISC',
  meson_version: '>= 0.56.0',
  version: '0.0.1',
)

lv2kit_src_root = meson.current_source_dir()
versioned_name = 'lv2kit-' + meson.project_version().split('.')[0]

#######################
# Compilers and Flags #
#######################

# Required tools
pkg = import('pkgconfig')
cc = meson.get_compiler('c')

# Optional C++ support
if add_languages(['cpp'], native: false, required: get_option('cxx'))
  cpp = meson.get_compiler('cpp')
endif

##############################
# Dependencies / Subprojects #
##############################

zix_dep = dependency(
  'zix-0',
  fallback: ['zix', 'zix_dep'],
  include_type: 'system',
  version: '>= 0.6.2',
)
serd_dep = dependency(
  'serd-0',
  fallback: ['serd', 'serd_dep'],
  include_type: 'system',
  version: '>= 0.32.4',
)
sord_dep = dependency(
  'sord-0',
  fallback: ['sord', 'sord_dep'],
  include_type: 'system',
  version: '>= 0.16.19',
)
lv2_dep = dependency(
  'lv2',
  fallback: ['lv2', 'lv2_dep'],
  include_type: 'system',
  version: '>= 1.18.11',
)
sratom_dep = dependency(
  'sratom-0',
  fallback: ['sratom', 'sratom_dep'],
  include_type: 'system',
  version: '>= 0.6.19',
)
lilv_dep = dependency(
  'lilv-0',
  fallback: ['lilv', 'lilv_dep'],
  include_type: 'system',
  version: '>= 0.24.27',
)
suil_dep = dependency(
  'suil-0',
  fallback: ['suil', 'suil_dep'],
  include_type: 'system',
  version: '>= 0.10.23',
)

###########
# Package #
###########

# Generate pkg-config file for external dependants
pkg.generate(
  description: 'LV2 host libraries',
  filebase: versioned_name,
  name: 'LV2Kit',
  requires: ['zix-0', 'serd-0', 'sord-0', 'lv2', 'sratom-0', 'lilv-0', 'suil-0'],
  subdirs: [versioned_name],
  version: meson.project_version(),
)

# Declare dependency for internal meson dependants
lv2kit_dep = declare_dependency(
  dependencies: [
    zix_dep,
    serd_dep,
    sord_dep,
    lv2_dep,
    sratom_dep,
    lilv_dep,
    suil_dep,
  ],
)

# Print configuration summary
if not meson.is_subproject()
  summary(
    {
      'Tests': not get_option('tests').disabled(),
      'Tools': not get_option('tools').disabled(),
    },
    bool_yn: true,
    section: 'Components',
  )

  summary(
    {
      'Install prefix': get_option('prefix'),
      'Headers': get_option('prefix') / get_option('includedir'),
      'Libraries': get_option('prefix') / get_option('libdir'),
      'Executables': get_option('prefix') / get_option('bindir'),
      'Man pages': get_option('prefix') / get_option('mandir'),
    },
    section: 'Directories',
  )
endif
