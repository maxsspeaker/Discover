from setuptools import setup, find_namespace_packages


def readme():
    return open('README.md', 'r').read()


setup(
    name='discover-overlay',
    author='trigg,maxsspeaker',
    author_email='',
    version='0.7.8',
    description='Voice chat VR overlay',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/maxsspeaker/Discover_VR',
    packages=find_namespace_packages(),
    include_package_data=True,
    data_files=[
        ('share/applications', [
            'discover_overlay.desktop', 'discover_overlay_configure.desktop','foxlay_overlay.desktop'
        ]),
        ('share/icons/hicolor/256x256/apps',
         ['discover-overlay.png', 'discover-overlay-tray.png', 'discover-overlay-default.png']),
        ('share/icons/hicolor/scalable/apps',
         ['discover-overlay.svg', 'discover-overlay-tray.svg', 'discover-overlay-default.svg']),
        ('share/icons/hicolor/512x512/apps/',
         ['VR_overlay/icons/foxlay_disabled_headphone.png', 'VR_overlay/icons/foxlay_disabled_microphone.png'])
    ],
    install_requires=[
        'PyGObject>=3.22',
        'websocket-client',
        'pyxdg',
        'requests',
        'pillow',
        'python-xlib',
        'setuptools',
        'pulsectl-asyncio',
        'pyqt6',
        'watchdog'
    ],
    entry_points={
        'console_scripts': [
            'discover-overlay = discover_overlay.discover_overlay:entrypoint',
            'foxlay_overlay = VR_overlay.Foxlay_overlay:main',
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: X11 Applications :: GTK',
        'Environment :: X11 Applications :: QT',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Communications :: Chat',
        'Topic :: Communications :: Conferencing',
    ],
    package_data={
        'discover_overlay': ['locales/*/LC_MESSAGES/*.mo', 'glade/*'],
        'VR_overlay': ['icons/*']
    },
    keywords='discord overlay voice linux vr',
    license='GPLv3+',
)
