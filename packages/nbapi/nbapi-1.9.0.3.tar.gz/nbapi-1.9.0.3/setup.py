import setuptools

long_description = "Simple Anime API package"
versionF="1.9.0.3"
setuptools.setup(
    name="nbapi",
    version=versionF,
    author="LazyNeko",
    author_email="nekobot.help@gmail.com",
    description="A small API for anime/nekos",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LazyNeko1/nbapi",
    #packages="nbapi",
    install_requires=['aiohttp','requests','asyncio'],
    data_files=[('nbapi', ['*.py'])],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)
