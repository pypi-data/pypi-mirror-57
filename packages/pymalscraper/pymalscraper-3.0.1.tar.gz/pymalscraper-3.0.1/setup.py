from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()

    setup(name='pymalscraper',
          version='3.0.1',
          author='prinsepipo',
          author_email='prinsepipo.sanchez@gmail.com',
          description='Simple Anime Web Scraper.',
          long_description=long_description,
          long_description_content_type="text/markdown",
          url='https://github.com/prinsepipo/anime-scraper',
          license='MIT',
          packages=find_packages(),
          install_requires=[
              'requests',
              'BeautifulSoup4',
              'lxml'
          ],
          python_requires='>=3',
          zip_safe=False)
