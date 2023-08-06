from distutils.core import setup

setup(
    name='hwmuliarska',
    packages=['hwmuliarska'],
    version="2.0.0",
    license='MIT',
    author="Yana Muliarska",
    author_email="muliarska@ucu.edu.ua",
    description="Five the most successful decades",
    long_description = """
    This package conducts the research based on file 'ratings.list'. 
    It identifies five the most successful decades and their average rating based on the ratings of films made during each decade. 
    It creates a pie chart rendering.
    """,
    long_description_content_type="text/markdown",

)
