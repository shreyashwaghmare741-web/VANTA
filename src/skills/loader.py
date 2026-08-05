import importlib
import pkgutil
import skills


def load_skills():

    """
    Automatically import every module inside
    the skills package.
    """

    for _, module_name, _ in pkgutil.iter_modules(skills.__path__):

        # Skip helper modules
        if module_name in (
            "__init__",
            "registry",
            "loader",
            "skill_manager",
        ):
            continue

        importlib.import_module(f"skills.{module_name}")