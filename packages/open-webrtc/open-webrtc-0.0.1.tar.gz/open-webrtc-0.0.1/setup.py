import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="open-webrtc", # Replace with your own username
    version="0.0.1",
    author="altanai",
    author_email="tara181989@gmail.com",
    description="Open webrtc package",
    long_description="A cross-platform WebRTC client framework based on GStreamer",
    long_description_content_type="text/markdown",
    url="https://github.com/altanai/openwebrtc",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
