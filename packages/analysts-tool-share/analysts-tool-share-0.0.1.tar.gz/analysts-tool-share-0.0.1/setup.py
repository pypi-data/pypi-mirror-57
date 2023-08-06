from setuptools import setup

setup(
    name="analysts-tool-share",
    version="0.0.1",
    license="MIT License",
    author="James Balcomb",
    author_email="james.w.balcomb+ats@gmail.com",
    url="https://github.com/james-w-balcomb/analysts-tool-share-python",
    description="Tools for analyzing data, using Python.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown; charset=UTF-8; variant=GFM",
    python_requires=">=3.5",
    packages=["analysts_tool_share"],
    classifiers=["Development Status :: 4 - Beta",
                 "Intended Audience :: Developers",
                 "Intended Audience :: Science/Research",
                 "License :: OSI Approved :: MIT License",
                 "Natural Language :: English",
                 "Operating System :: OS Independent",
                 "Programming Language :: Python",
                 "Programming Language :: Python :: 3",
                 "Programming Language :: Python :: 3.5",
                 "Programming Language :: Python :: Implementation :: CPython",
                 "Topic :: Scientific/Engineering :: Information Analysis",
                 "Topic :: Utilities"],
    keywords="data analysis, data processing, data science, data software, data utilities, machine learning"
)
