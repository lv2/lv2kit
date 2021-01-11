project('lv2kit', ['c'],
        version: '0.0.1',
        license: 'ISC',
        meson_version: '>= 0.49.2',
        default_options: [
          'b_ndebug=if-release',
          'buildtype=release',
          'c_std=c99',
          'default_library=both',
          'warning_level=2',
        ])

lv2kit_src_root = meson.current_source_dir()
major_version = meson.project_version().split('.')[0]
version_suffix = '-@0@'.format(major_version)
versioned_name = 'lv2kit' + version_suffix

# Load build tools
pkg = import('pkgconfig')
cc = meson.get_compiler('c')

# Dependencies

serd_dep = dependency('serd-1',
                      version: '>=1.0.0',
                      fallback: ['serd', 'serd_dep'])

lv2_dep = dependency('lv2',
                     version: '>=1.18.3',
                     fallback: ['lv2', 'lv2_dep'])

# Subprojects
sratom_dep = subproject('sratom').get_variable('sratom_dep')
lilv_dep = subproject('lilv').get_variable('lilv_dep')
suil_dep = subproject('suil').get_variable('suil_dep')

# Define lv2kit dependency and package

lv2kit_dep = declare_dependency(
  dependencies: [serd_dep, lv2_dep, sratom_dep, lilv_dep, suil_dep]
)

pkg.generate(
  name: 'LV2Kit',
  filebase: versioned_name,
  subdirs: [versioned_name],
  version: meson.project_version(),
  description: 'LV2 plugin SDK',
  requires: ['serd-0', 'sord-0', 'lv2', 'sratom-0', 'lilv-0', 'suil-0'])

# Print configuration summary
if meson.version().version_compare('>=0.53.0')
  summary('Tests', get_option('tests'), bool_yn: true)
  summary('Utilities', get_option('utils'), bool_yn: true)

  summary('Install prefix', get_option('prefix'))

  summary('Headers', get_option('prefix') / get_option('includedir'))
  summary('Libraries', get_option('prefix') / get_option('libdir'))
  summary('Executables', get_option('prefix') / get_option('bindir'))
  summary('Man pages', get_option('prefix') / get_option('mandir'))
endif
