#!/usr/bin/env python3

import sys
from pathlib import Path


def create_feature_structure(lib_path: str, feature_name: str):
    lib = Path(lib_path).resolve()

    if not lib.exists():
        print(f"❌ Error: '{lib}' does not exist.")
        return

    folders = [
        # Feature folders
        f"features/{feature_name}/presentation/bloc",
        f"features/{feature_name}/presentation/pages",
        f"features/{feature_name}/presentation/widgets",

        f"features/{feature_name}/domain/entities",
        f"features/{feature_name}/domain/repositories",
        f"features/{feature_name}/domain/usecases",

        f"features/{feature_name}/data/models",
        f"features/{feature_name}/data/repositories",
        f"features/{feature_name}/data/datasources",

        # Core folders
        "core/error",
        "core/usecases",
        "core/utils",
    ]

    # Create directories
    for folder in folders:
        path = lib / folder
        path.mkdir(parents=True, exist_ok=True)
        print(f"✅ Created: {path}")

    # Create main.dart if it doesn't exist
    main_dart = lib / "main.dart"
    if not main_dart.exists():
        main_dart.touch()
        print(f"✅ Created: {main_dart}")

    print(f"\n🎉 Feature '{feature_name}' created successfully!")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(
            "Usage:\n"
            "python create_structure.py <absolute_lib_path> <feature_name>\n\n"
            "Example:\n"
            "python create_structure.py "
            "/Users/john/myapp/lib counter"
        )
        sys.exit(1)

    lib_path = sys.argv[1]
    feature_name = sys.argv[2]

    create_feature_structure(lib_path, feature_name)