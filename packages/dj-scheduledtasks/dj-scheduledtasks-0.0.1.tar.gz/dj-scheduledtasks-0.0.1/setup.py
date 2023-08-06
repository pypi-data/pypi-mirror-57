import setuptools

with open("./README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dj-scheduledtasks",
    version="0.0.1",
    author="AppointmentGuru",
    author_email="tech@appointmentguru.co",
    description="...",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/.../...",
    packages=['scheduledtasks'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
