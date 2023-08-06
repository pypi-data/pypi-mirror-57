# -*- coding: utf-8 -*-
import os

from freckles_adapter_nsbl.defaults import NSBL_COMMUNITY_FRECKLET_REPO
from ting.attributes.rendering import JinjaTemplateMixin

SHELLTING_EXTERNAL_DIR = os.path.join(os.path.dirname(__file__), "external")
DEFAULT_SHELLTINGS_FOLDER = os.path.join(SHELLTING_EXTERNAL_DIR, "shelltings")
# SHELLTING_TEMPLATE_DIR = os.path.join(SHELLTING_EXTERNAL_DIR, "templates")
SHELLTING_COMMUNITY_REPO_URL = (
    "https://gitlab.com/frecklets/frecklets-nsbl-community.git"
)
SHELLTING_COMMUNITY_REPO = NSBL_COMMUNITY_FRECKLET_REPO
SHELLTING_CONTEXT_SCHEMA = {}

SHELLTING_LOAD_CONFIG = {
    "class_name": "Shellting",
    "attributes": [
        {
            "FrontmatterAndContentAttribute": {
                "metadata_name": "meta",
                "content_name": "shellting_content",
                "source_attr_name": "ting_content",
                "metadata_strategies": ["comments"],
            }
        },
        # {"FileStringContentAttribute": {"target_attr_name": "ting2_content"}},
        {
            "ArgsAttribute": {
                "source_attr_name": "meta",
                "target_attr_name": "args",
                "index_attr_name": "_meta_parent_repo",
                "filtered_attr_name": "args_filtered",
            }
        },
        {
            "ValueAttribute": {
                "target_attr_name": "properties",
                "source_attr_name": "meta",
                "default": {},
            }
        },
        {
            "ValueAttribute": {
                "target_attr_name": "resources",
                "source_attr_name": "meta",
                "default": {},
            }
        },
        {
            "CliArgsAttribute": {
                "target_attr_name": "cli_args",
                "var_names_attr_name": "args",
                "args_attr_name": "args",
                "default_arg": {"required": True, "empty": False},
            }
        },
        # {
        #     "JinjaTemplateAttribute": {
        #         "template": "arg_parse.j2",
        #         "target_attr_name": "arg_check_content",
        #         "required_attrs": ["args"],
        #         "template_dir": SHELLTING_TEMPLATE_DIR,
        #         "constants": {"is_function": True},
        #     }
        # },
        # {
        #     "JinjaTemplateAttribute": {
        #         "template": "code_block.j2",
        #         "target_attr_name": "script_content",
        #         "required_attrs": ["arg_check_content", "id", "shellting_content"],
        #         "template_dir": SHELLTING_TEMPLATE_DIR,
        #         "constants": {"is_function": True},
        #     }
        # },
        {"DocAttribute": {"target_attr_name": "doc", "source_attr_name": "meta"}},
    ],
    "ting_id_attr": "shellting_name",
    "mixins": [JinjaTemplateMixin],
    "loaders": {
        "script_files": {
            "class": "ting.tings.FileTings",
            "load_config": {"folder_load_file_match_regex": "\\.shellting$"},
            "attributes": [
                "FileStringContentAttribute",
                {
                    "MirrorAttribute": {
                        "source_attr_name": "filename_no_ext",
                        "target_attr_name": "shellting_name",
                    }
                },
            ],
        }
    },
}
