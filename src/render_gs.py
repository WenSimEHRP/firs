import codecs  # used for writing files - more unicode friendly than standard open() module

import sys
import shutil
import os

currentdir = os.curdir
from time import time

import firs
import utils
from polar_fox import git_info

registered_cargos = firs.registered_cargos
registered_industries = firs.registered_industries
registered_economies = firs.registered_economies

from chameleon import PageTemplateLoader  # chameleon used in most template cases

# get args passed by makefile
makefile_args = utils.get_makefile_args(sys)

gs_src = os.path.join(currentdir, "src", "gs")
gs_dst = os.path.join(firs.generated_files_path, "gs")


class GSHelper(object):
    # GS-specific methods for formatting etc in chameleon templates, this is only for things not handled in industry.py or utils.py

    def get_economy_fingerprint(self, registered_industries, economy):
        result = ""
        # as of August 2021, port and wharf were sufficiently unique, and at least one of them is in every economy
        # !! this could use a guard to enforce uniqueness
        for industry in registered_industries:
            if industry.id in ["port", "wharf"]:
                if industry.economy_variations[economy.id].enabled:
                    fingerprint_industry = industry
                    break
        result = (
            result
            + "Accepts: "
            + " ".join(sorted(fingerprint_industry.get_accept_cargo_types(economy)))
        )
        result = result + " Produces:"
        for cargo_label, prod_multiplier in sorted(
            fingerprint_industry.get_prod_cargo_types(economy)
        ):
            result = result + " " + cargo_label
        return result

    def get_grfid(self):
        # !! grfid needs moved out of header.pynml to global constants (may have done this for other grfs already?)
        utils.echo_message("GSHelper.get_grf_id incomplete, returning hard-coded value")
        return "0xF1250008"


def render_nuts(nuts_by_subdir):
    # setup the places we look for templates
    nut_templates = PageTemplateLoader(
        os.path.join(currentdir, "src", "gs", "gs_templates"), format="text"
    )
    for subdir_name, nuts in nuts_by_subdir.items():
        if subdir_name == "root":
            dst_dir = gs_dst
        else:
            dst_dir = os.path.join(gs_dst, subdir_name)
            if os.path.exists(dst_dir):
                shutil.rmtree(dst_dir)
            if not os.path.exists(dst_dir):
                os.mkdir(dst_dir)
        for nut_name in nuts:
            nut_template = nut_templates[nut_name + ".pynut"]
            dst_file = codecs.open(
                os.path.join(dst_dir, nut_name + ".nut"), "w", "utf8"
            )
            result = utils.unescape_chameleon_output(
                nut_template(
                    gs_helper=GSHelper(),
                    makefile_args=makefile_args,
                    git_info=git_info,
                    registered_industries=registered_industries,
                    registered_cargos=registered_cargos,
                    registered_economies=registered_economies,
                    utils=utils,
                )
            )
            dst_file.write(result)
            dst_file.close()


def main():
    start = time()
    print("[RENDER GS] render_gs.py")

    if os.path.exists(gs_dst):
        shutil.rmtree(gs_dst)
    if not os.path.exists(gs_dst):
        os.mkdir(gs_dst)
    hint_file = codecs.open(
        os.path.join(gs_dst, "_gs_files_here_are_generated.txt"), "w", "utf8"
    )
    hint_file.write(
        "Don't edit the gs files here.  They're generated by the build script. \n Edit the ones in src/gs instead."
    )
    hint_file.close()

    nuts_by_subdir = {
        # alphabetise nuts in each list for simplicity
        "root": [
            "firs",
            "info",
            "main",
            "persistent_storage",
            "temp_prototyping",
            "version",
        ],
        "grind": ["grind"],
        "atlas": ["atlas"],
        "vulcan": [
            "vulcan_industry_control",
            "vulcan_map_curator",
            "vulcan_town_control",
            "vulcan_town_story_book",
        ],
        # "minigames": ["winning_move", "zellepins"],
    }
    render_nuts(nuts_by_subdir)

    # copy lang dir also
    shutil.copytree(os.path.join(gs_src, "lang"), os.path.join(gs_dst, "lang"))

    print(format((time() - start), ".2f") + "s")


if __name__ == "__main__":
    main()
