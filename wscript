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
                    ['lv2', 'serd', 'sord', 'sratom', 'suil', 'lilv']))


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


def test(ctx):
    for i in ctx.env.LV2KIT_BUILD:
        ctx.recurse(i, mandatory=False)
