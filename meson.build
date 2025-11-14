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

docs_option_string = 'auto'
if get_option('docs').enabled()
  docs_option_string = 'enabled'
elif get_option('docs').disabled()
  docs_option_string = 'disabled'
endif

tests_option_string = 'auto'
if get_option('tests').enabled()
  tests_option_string = 'enabled'
elif get_option('tests').disabled()
  tests_option_string = 'disabled'
endif

tools_option_string = 'auto'
if get_option('tools').enabled()
  tools_option_string = 'enabled'
elif get_option('tools').disabled()
  tools_option_string = 'disabled'
endif

plugins_option_string = 'auto'
if get_option('plugins').enabled()
  plugins_option_string = 'enabled'
elif get_option('plugins').disabled()
  plugins_option_string = 'disabled'
endif

cpp_option_string = 'auto'
if not get_option('cxx')
  cpp_option_string = 'disabled'
endif

zix_dep = dependency(
  'zix-0',
  default_options: [
    'docs=' + docs_option_string,
    'lint=' + get_option('lint').to_string(),
    'tests=' + tests_option_string,
    'tests_cpp=' + cpp_option_string,
  ],
  fallback: ['zix', 'zix_dep'],
  include_type: 'system',
  version: '>= 0.8.0',
)
serd_dep = dependency(
  'serd-0',
  default_options: [
    'docs=' + docs_option_string,
    'lint=' + get_option('lint').to_string(),
    'tests=' + tests_option_string,
    'tools=' + tools_option_string,
  ],
  fallback: ['serd', 'serd_dep'],
  include_type: 'system',
  version: '>= 0.32.6',
)
sord_dep = dependency(
  'sord-0',
  default_options: [
    'docs=' + docs_option_string,
    'lint=' + get_option('lint').to_string(),
    'tests=' + tests_option_string,
    'tools=' + tools_option_string,
  ],
  fallback: ['sord', 'sord_dep'],
  include_type: 'system',
  version: '>= 0.16.20',
)
lv2_dep = dependency(
  'lv2',
  default_options: [
    'docs=' + docs_option_string,
    'lint=' + get_option('lint').to_string(),
    'lv2dir=' + get_option('lv2dir'),
    'tests=' + tests_option_string,
  ],
  fallback: ['lv2', 'lv2_dep'],
  include_type: 'system',
  version: '>= 1.18.11',
)
sratom_dep = dependency(
  'sratom-0',
  default_options: [
    'docs=' + docs_option_string,
    'lint=' + get_option('lint').to_string(),
    'tests=' + tests_option_string,
  ],
  fallback: ['sratom', 'sratom_dep'],
  include_type: 'system',
  version: '>= 0.6.20',
)
lilv_dep = dependency(
  'lilv-0',
  default_options: [
    'bindings_cpp=' + cpp_option_string,
    'docs=' + docs_option_string,
    'lint=' + get_option('lint').to_string(),
    'tests=' + tests_option_string,
    'tools=' + tools_option_string,
  ],
  fallback: ['lilv', 'lilv_dep'],
  include_type: 'system',
  version: '>= 0.26.0',
)
suil_dep = dependency(
  'suil-0',
  default_options: [
    'qt5=' + cpp_option_string,
    'qt6=' + cpp_option_string,
    'docs=' + docs_option_string,
    'lint=' + get_option('lint').to_string(),
    'tests=' + tests_option_string,
  ],
  fallback: ['suil', 'suil_dep'],
  include_type: 'system',
  version: '>= 0.10.24',
)

if not get_option('plugins').disabled()
  lv2_examples = subproject(
    'lv2-examples',
    default_options: [
      'docs=' + docs_option_string,
      'lint=' + get_option('lint').to_string(),
      'lv2dir=' + get_option('lv2dir'),
      'plugins=' + plugins_option_string,
      'tests=' + tests_option_string,
    ],
  )
endif

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
