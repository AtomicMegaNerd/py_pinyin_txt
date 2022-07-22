def get_version() -> str:
    """
    This method simply gets the version of the program from the canonical VERSION file
    and outputs that as a string.
    """
    with open("VERSION", "r", encoding="utf-8") as version_fd:
        version = version_fd.readlines()[0].strip()
        return version
