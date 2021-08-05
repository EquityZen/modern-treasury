from distutils.core import setup
setup(
    name = 'modern_treasury',
    packages = ['modern_treasury'],
    version = '0.1',
    license='MIT',
    description = 'Modern Treasury Client Library',
    author = 'Issam Zeibak',
    author_email = 'issam.zeibak@equityzen.com',
    url = 'https://github.com/equityzen/modern-treasury',
    download_url = 'https://github.com/EquityZen/modern-treasury/archive/refs/tags/v_01.tar.gz',
    keywords = ['Modern Treasury', 'Finance'],
    install_requires=['pytest', 'requests'],
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9.1',
    ],
)
