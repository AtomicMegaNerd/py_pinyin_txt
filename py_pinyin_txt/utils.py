def getVersion() -> str:
    """
    This method simply gets the version of the program from the canonical VERSION file
    and outputs that as a string.
    """
    with open("VERSION", "r") as version_fd:
        version = version_fd.readlines()[0].strip()
        return version
