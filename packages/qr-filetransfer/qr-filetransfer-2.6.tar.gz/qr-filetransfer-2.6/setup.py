import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='qr-filetransfer',
    version='2.6',
    author='Siddharth Dushantha',
    author_email='siddharth.dushantha@gmail.com',
    description='Transfer files over WiFi between your computer and your smartphone from the terminal',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/sdushantha/qr-filetransfer',
    packages=setuptools.find_packages(),
    scripts=['qr-filetransfer/qr-filetransfer'],
    install_requires=['netifaces', 'qrcode']
)
