#!/usr/bin/env python

import os

from waflib import Logs
from waflib.extras import autowaf

# Mandatory waf variables
APPNAME = 'lv2kit'  # Package name for waf dist
VERSION = '0.0.0'   # Package version for waf dist
top = '.'           # Source directory
out = 'build'       # Build directory

line_just = 42
projects = list(map(lambda x: os.path.join('libs', x),
                    ['serd', 'sord', 'lv2', 'sratom', 'suil', 'lilv']))


def options(opt):
    opt.load('compiler_c')
    opt.load('compiler_cxx')
    opt.load('lv2')
    run_opts = opt.add_option_group('Run options')
    run_opts.add_option('--cmd', type='string', dest='cmd',
                        help='command to run from build directory')
    for p in projects:
        opt.recurse(p)


def configure(conf):
    conf.load('compiler_c', cache=True)
    conf.load('compiler_cxx', cache=True)
    conf.load('lv2', cache=True)
    conf.load('autowaf', cache=True)

    if not autowaf.set_c_lang(conf, 'c11', mandatory=False):
        autowaf.set_c_lang(conf, 'c99')

    conf.env.LV2KIT_BUILD = []
    for p in projects:
        try:
            name = os.path.basename(p)
            Logs.pprint('BOLD', '')
            conf.recurse(p)
            autowaf.set_local_lib(conf, name, name != 'lv2')
            conf.env.LV2KIT_BUILD += [p]
        except Exception as e:
            Logs.warn('Configuration failed, not building %s (%s)' % (p, e))

    Logs.info('')
    autowaf.display_summary(conf)
    Logs.info('\nBuilding: %s\n' % ' '.join(conf.env.LV2KIT_BUILD))

    not_building = []
    for i in projects:
        if i not in conf.env.LV2KIT_BUILD:
            not_building += [i]

    if not_building != []:
        Logs.warn('Not building:\n\t%s\n' % '\n\t'.join(not_building))


def build(bld):
    for i in bld.env.LV2KIT_BUILD:
        bld.add_group()
        bld.recurse(i)

    if bld.env.DOCS:
        bld(features       = 'subst',
            source         = 'doc/reference.doxygen.in',
            target         = 'doc/reference.doxygen',
            install_path   = '',
            LV2KIT_VERSION = VERSION,
            LV2KIT_SRCDIR  = os.path.abspath(bld.path.srcpath()))

        bld(features = 'doxygen',
            doxyfile = 'doc/reference.doxygen')


def test(tst):
    for i in tst.env.LV2KIT_BUILD:
        tst.recurse(i, mandatory=False)


def dist(ctx):
    ctx.archive()
