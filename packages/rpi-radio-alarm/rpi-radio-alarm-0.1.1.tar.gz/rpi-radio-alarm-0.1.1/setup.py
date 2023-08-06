from distutils.core import setup

setup(
    name='rpi-radio-alarm',
    packages=['rpi-radio-alarm'],
    version='0.1.1',
    license='BSD-3',
    description='Library simplify communication to the rpi-radio-alarm',
    author='bb4L',
    author_email='39266013+bb4L@users.noreply.github.com',
    url='https://github.com/bb4L/rpi-radio-alarm-pip',
    download_url='https://github.com/bb4L/rpi-radio-alarm-pip/archive/v_01_2.tar.gz',
    keywords=['Raspberry Pi', 'radio', 'alarm'],
    install_requires=[
        'aiohttp==3.5.4',
        'async-timout=3.0.1',
        'attrs==19.3.0',
        'chardet==3.0.4',
        'discord==1.0.1',
        'discord.py==1.2.4',
        'idna==2.8',
        'multidict==4.5.2',
        'python-dotenv==0.10.3',
        'websockets==6.0',
        'yarl==1.3.0'

    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
)
