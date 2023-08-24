# Copyright 2022-2023 David Robillard <d@drobilla.net>
# SPDX-License-Identifier: 0BSD OR ISC

project('lv2kit', ['c'],
        version: '0.0.1',
        license: 'ISC',
        meson_version: '>= 0.56.0',
        default_options: [
          'b_ndebug=if-release',
          'buildtype=release',
          'c_std=c99',
          'cpp_std=c++17',
        ])

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

################
# Dependencies #
################

zix_dep = dependency('zix-0', fallback: 'zix', version: '>= 0.4.0')
serd_dep = dependency('serd-0', fallback: 'serd', version: '>= 0.30.17')
sord_dep = dependency('sord-0', fallback: 'sord', version: '>= 0.16.15')
lv2_dep = dependency('lv2', fallback: 'lv2', version: '>= 1.18.2')

###############
# Subprojects #
###############

sratom_dep = subproject('sratom').get_variable('sratom_dep')
lilv_dep = subproject('lilv').get_variable('lilv_dep')
suil_subproject = subproject('suil', default_options: ['cpp_std=c++17'])
suil_dep = suil_subproject.get_variable('suil_dep')

###########
# Package #
###########

# Generage pkg-config file for external dependants
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
      'Install prefix':  get_option('prefix'),
      'Headers':  get_option('prefix') / get_option('includedir'),
      'Libraries':  get_option('prefix') / get_option('libdir'),
      'Executables': get_option('prefix') / get_option('bindir'),
      'Man pages': get_option('prefix') / get_option('mandir'),
    },
    section: 'Directories',
  )
endif
