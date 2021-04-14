config = configuration_data()
config.set('LV2KIT_VERSION', meson.project_version())

conf_py = configure_file(configuration: config,
                         input: '../conf.py.in',
                         output: 'conf.py')

configure_file(copy: true, input: '../summary.rst', output: 'summary.rst')

c_rst_files = files(
  'index.rst',
  'overview.rst',
  'reference.rst',
)

foreach f : c_rst_files
  configure_file(copy: true, input: f, output: '@PLAINNAME@')
endforeach

configure_file(
  copy: true,
  input: files('../../subprojects/serd/doc/c/overview.rst'),
  output: 'serd_overview.rst')

configure_file(
  copy: true,
  input: files('../../subprojects/serd/subprojects/exess/doc/c/overview.rst'),
  output: 'exess_overview.rst')

configure_file(
  copy: true,
  input: files('../../subprojects/sratom/doc/c/overview.rst'),
  output: 'sratom_overview.rst')

configure_file(
  copy: true,
  input: files('../../subprojects/lilv/doc/c/overview.rst'),
  output: 'lilv_overview.rst')

configure_file(
  copy: true,
  input: files('../../subprojects/suil/doc/c/overview.rst'),
  output: 'suil_overview.rst')

configure_file(
  copy: true,
  input: files('../../subprojects/lilv/doc/c/world.rst'),
  output: 'world.rst')

configure_file(
  copy: true,
  input: files('../../subprojects/lilv/doc/c/plugins.rst'),
  output: 'plugins.rst')

configure_file(
  copy: true,
  input: files('../../subprojects/lilv/doc/c/uis.rst'),
  output: 'uis.rst')

subdir('xml')
subdir('api')

docs = custom_target(
  'singlehtml documentation for lv2kit',
  command: [sphinx_build, '-M', 'singlehtml',
            meson.current_build_dir(), meson.current_build_dir(),
            '-E', '-q', '-t', 'singlehtml'],
  input: [c_rst_files, c_lv2kit_rst, c_index_xml],
  output: 'singlehtml',
  build_by_default: true,
  install: true,
  install_dir: docdir / versioned_name)

docs = custom_target(
  'html documentation for lv2kit',
  command: [sphinx_build, '-M', 'html',
            meson.current_build_dir(), meson.current_build_dir(),
            '-E', '-q', '-t', 'html'],
  input: [c_rst_files, c_lv2kit_rst, c_index_xml],
  output: 'html',
  build_by_default: true,
  install: true,
  install_dir: docdir / versioned_name)
