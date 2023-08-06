LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(asctime)s %(levelname)s %(name)s %(module)s %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
    },
    # 'filters': {
    #     'special': {
    #         '()': 'project.logging.SpecialFilter',
    #         'foo': 'bar',
    #     },
    #     'require_debug_true': {
    #         '()': 'django.utils.log.RequireDebugTrue',
    #     },
    # },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            # 'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': 'moutain-red.log',
            'formatter': 'simple',
            'encoding': 'utf-8'
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
        },
        # 'django.server': {
        #     'handlers': ['console'],
        #     'level': 'ERROR',
        #     'propagate': False,
        # },
        'mountainred': {
            'handlers': ['console', 'file'],
            'level': 'INFO'
        }
    }
}
