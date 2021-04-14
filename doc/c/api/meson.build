c_lv2kit_rst = custom_target(
  'LV2Kit C API ReST Documentation',
  command: [dox_to_sphinx, '-f', '@INPUT0@', meson.current_build_dir()],
  input: [c_index_xml] + c_rst_files,
  output: 'lv2kit.rst')
