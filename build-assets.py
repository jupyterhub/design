import glob
import logging
import os.path
import pathlib
import subprocess

logger = logging.getLogger(__name__)


def svg2png(source_file):
    source_dir_name, source_file_name = os.path.split(source_file)
    source_dir_path = pathlib.Path(source_dir_name)

    target_dir_name = os.path.join("assets", *source_dir_path.parts[1:])
    target_file_name = source_file_name.replace(".svg", ".png")
    target_file_path = os.path.join(target_dir_name, target_file_name)

    subprocess.run(
        [
            "inkscape",
            f"--export-filename={target_file_path}",
            "--export-type=png",
            "--export-area-page",
            source_file,
        ]
    )


def svg2svg(source_file):
    source_dir_name, source_file_name = os.path.split(source_file)
    source_dir_path = pathlib.Path(source_dir_name)

    target_dir_name = os.path.join("assets", *source_dir_path.parts[1:])
    target_file_name = source_file_name.replace(".svg", ".png")
    target_file_path = os.path.join(target_dir_name, target_file_name)

    subprocess.run(
        [
            "inkscape",
            f"--export-filename={target_file_path}",
            "--export-type=svg",
            "--export-area-page",
            "--export-plain-svg",
            "--export-text-to-path",
            source_file,
        ]
    )


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        prog="build-assets", description="Build JupyterHub assets"
    )

    output_group = parser.add_argument_group("output")
    output_group.add_argument("--png", help="PNG", action="store_true")
    output_group.add_argument("--svg", help="SVG", action="store_true")
    output_group.add_argument("--all", help="All output formats", action="store_true")

    parser.add_argument(
        "-v", "--verbose", help="increase output verbosity", action="store_true"
    )
    parser.add_argument("source", nargs="*")

    args = parser.parse_args()

    if args.verbose:
        log_level = logging.DEBUG
    else:
        log_level = logging.INFO

    logging.basicConfig(level=log_level)

    if args.source:
        source_files = args.source
    else:
        source_files = glob.glob("src/**/*.svg")

    for _source_file in source_files:
        logger.info("Start processing %s ...", _source_file)

        if args.all or args.png:
            logger.info("Converting %s into PNG", _source_file)
            svg2png(_source_file)

        if args.all or args.svg:
            logger.info("Converting %s into SVG", _source_file)

        logger.info("End processing %s!", _source_file)
