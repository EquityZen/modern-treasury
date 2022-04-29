from distutils.core import setup
setup(
    name = 'modern_treasury',
    packages = ['modern_treasury',
                'modern_treasury.objects',
                'modern_treasury.objects.request',
                'modern_treasury.objects.webhook_events',
                'modern_treasury.objects.response'],
    version = '0.0.38',
    license='MIT',
    description = 'Modern Treasury Client Library',
    author = 'Issam Zeibak',
    author_email = 'issam.zeibak@equityzen.com',
    url = 'https://github.com/equityzen/modern-treasury',
    download_url = 'https://github.com/EquityZen/modern_treasury/archive/refs/tags/v_0.0.38.tar.gz',
    keywords = ['Modern Treasury', 'Finance'],
    install_requires=['pytest', 'requests'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
    ],
)
