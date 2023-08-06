
tasks = {
    'util' : {
        'features'  : 'cshlib',
        'source'    :  dict( include = 'shlib/**/*.c' ),
        'includes'  : '.',
        #'toolchain' : 'auto-c',
    },
    'test' : {
        'features'  : 'cxxprogram',
        'source'    :  dict( include = 'prog/**/*.cpp' ),
        'includes'  : '.',
        'use'       : 'util',
        #'toolchain' : 'auto-c++',
    },
}

