# -*- coding: utf-8 -*-
 
 
"""mltrack.mltrack: provides entry point main()."""
 
 
__version__ = "0.0.2"
 
 
import sys
import os
from pathlib import Path
from collections import OrderedDict
import argparse
from datetime import datetime
import pickle
from jinja2 import Environment
from jinja2 import FileSystemLoader
import subprocess
import shlex
import re
from subprocess import Popen, PIPE, CalledProcessError



def _graph_to_makefile_str(mlt_dependency_graph):
    graph = mlt_dependency_graph["graph"]
    node_strings = []
    for node in graph:
        help_str = node.get('help', '')
        if help_str != '':
            help_str = "## "+help_str
        outputs_str = " ".join(node['outputs'])
        inputs_str = " ".join(node.get('inputs', []))
        io_str = outputs_str + ":" + " " + inputs_str
        actions = node.get('actions', [])
        if len(actions) > 0:
            actions_str = "\t"+"\n\t".join(node.get('actions', []))
        else:
            actions_str = ""
        item_str = "\n".join([help_str, io_str, actions_str])
        node_strings.append(item_str)
    
    makefile_str = "\n\n".join(node_strings)
    return makefile_str


def get_mlt_graph_data(repo_dir):
    mlt_dep_filepath = repo_dir / "mlt_dependencies.py"
    if not mlt_dep_filepath.exists():
        raise Exception("Cannot find {str(mlt_dep_filepath)} : define your project dependencies in mlt_dependencies.py and try again.")
        #### temp
    import sys
    sys.path.insert(0, str(repo_dir.resolve()))
    import mlt_dependencies
    sys.path.pop(0)
    graph_data = mlt_dependencies.mlt_dependency_graph
    return graph_data


def mlt_dep_to_dot_makefile(repo_dir):
    '''
    Reads mlt_dependencies.py and generates .mlt/.makefile
    '''
    graph_data = get_mlt_graph_data(repo_dir=repo_dir)
    makefile_str = _graph_to_makefile_str(mlt_dependency_graph=graph_data)
    dot_makefile = repo_dir / '.mlt' / '.makefile'
    dot_makefile.write_text(get_template('dot_makefile.j2').render(makefile_str=makefile_str))


# first, create mlt_dependencies.json --> generate .makefile from this
def mlt_init(project_name, repo_dir, ask_project_name=True):
    if ask_project_name:
        project_name = input("What's your project's name? ")
    dot_mlt_dir = repo_dir / ".mlt"
    dot_makefile = dot_mlt_dir / ".makefile"
    try:
        dot_mlt_dir.mkdir()
    except FileExistsError as e:
        print("Found existing ./.mlt directory: delete directory to run 'mlt init' again.")
        raise Exception(e)
    
    mlt_config = {
        'project_name': project_name,
        'repo_dir': repo_dir,
        'created_at': datetime.now()
    }
    mlt_config_filepath = dot_mlt_dir / 'mlt_config.pkl'
    pickle.dump(mlt_config, open(mlt_config_filepath, 'wb'))

    mlt_dep_filepath = repo_dir / 'mlt_dependencies.py'

    if mlt_dep_filepath.exists():
        mlt_dep_to_dot_makefile(repo_dir=repo_dir)
        print("Successfully initialized mlt project...")
    else:
        print("Successfully initialized mlt project. Define your project dependencies in mlt_dependencies.py to get started.")



def get_template(filename):
    package_path = Path(__file__).parent
    templates_folder = package_path / "templates"
    templates_folder = str(templates_folder)
    j2_env = Environment(loader=FileSystemLoader(templates_folder))
    template = j2_env.get_template(filename)
    return template

def get_project_config_info():
    cwd = Path.cwd()
    project_name = input("What's your project's name? ")
    if project_name == "":
        raise Exception("Need project name to proceed. Please start over with mlt create")
    _project_name = project_name.replace(" ", "_").lower()
    repo_name = input(f"Enter repository name [recommended repository name: {_project_name}, press enter to use {_project_name} ]: ")
    if repo_name == "":
        repo_name = _project_name
    
    author_name = input("Enter author name: ")
    license_type = input("Enter license type (optional, press enter for no license) [MIT (1), GPL (2), Apache (3)]: ")
    if license_type != "":
        try:
            license_type = int(license_type)
        except Exception as e:
            print("did not recognize license type, will not generate license file")
        
        if license_type not in (1, 2, 3):
            print("did not recognize license type, will not generate license file")
            license_type = None
    else:
        assert license_type == ""
        license_type = None  
    
    aws_profile = input("Enter AWS profile name (press enter to use 'default' ): ")
    if aws_profile == "":
        aws_profile = 'default'  #remember to add this to mlt_dependencies
    
    s3_bucketname = input("Enter bucket name: ")
    if s3_bucketname == "":
        s3_bucketname = 'default-bucket'

    assert repo_name != ""
    assert project_name != ""

    return project_name, repo_name, author_name, license_type, aws_profile, s3_bucketname


def create_project_directory(project_name, repo_name, author_name, license_type, aws_profile, s3_bucketname, parent_dir = Path('.')):

    cur_dir = Path(os.getcwd())
    repo_dir = cur_dir / repo_name
    print("repo_dir is :", str(repo_dir))
    repo_dir.mkdir()

    data_dir = repo_dir / "data"
    data_dir_external = data_dir / "external"
    data_dir_interim = data_dir / "interim"
    data_dir_processed = data_dir / "processed"
    data_dir_raw = data_dir / "raw"
    _ = [(dir_path.mkdir(), (dir_path / ".gitkeep").touch() ) for dir_path in 
    [data_dir, data_dir_external, data_dir_interim, data_dir_processed, data_dir_raw]]


    docs_dir = repo_dir / "docs"
    models_dir = repo_dir / "models"
    notebooks_dir = repo_dir / "notebooks"
    references_dir = repo_dir / "references"
    reports_dir = repo_dir / "reports"
    reports_figures_dir = reports_dir / "figures"
    _ = [(dir_path.mkdir(), (dir_path / ".gitkeep" ).touch() ) for dir_path in 
    [docs_dir, models_dir, notebooks_dir, references_dir, reports_dir, reports_figures_dir] ]
    

    src_dir = repo_dir / "src"
    src_data_dir = src_dir / "data"
    src_features_dir = src_dir / "features"
    src_models_dir = src_dir / "models"
    src_visualization_dir = src_dir / "visualization"
    src_tests_dir = src_dir / "tests"   #make sure to include tests
    _ = [ (dir_path.mkdir(), (dir_path / ".gitkeep" ).touch() )  for dir_path in 
    [src_dir, src_data_dir, src_features_dir, src_models_dir, src_visualization_dir, src_tests_dir] ]

    download_data_py = src_data_dir / "download_data.py"
    make_dataset_py = src_data_dir / "make_dataset.py"
    build_features_py = src_features_dir / "build_features.py"
    featurizer_py = src_features_dir / "featurizer.py"
    learn_features_py = src_features_dir / "learn_features.py"
    train_model_py = src_models_dir / "train_model.py"
    eval_model_py = src_models_dir / "eval_model.py"
    settings_py = repo_dir / "settings.py"
    to_write = [
        (download_data_py, 'download_data_py.j2'),
        (make_dataset_py, 'make_dataset_py.j2'),
        (build_features_py, 'build_features_py.j2'),
        (featurizer_py, 'featurizer_py.j2'),
        (learn_features_py, 'learn_features_py.j2'),
        (train_model_py, 'train_model_py.j2'),
        (eval_model_py, 'eval_model_py.j2'),
        (settings_py, 'settings_py.j2')
    ]
    for filepath, template_name in to_write:
        filepath.write_text(get_template(template_name).render())


    make_dataset = src_data_dir / "make_dataset.py"
    build_features = src_features_dir / "build_features.py"
    train_model = src_models_dir / "train_model.py"
    predict_model = src_models_dir / "predict_model.py"
    make_dataset.touch()
    build_features.touch()
    train_model.touch()
    predict_model.touch()
    
    # create .env, .gitignore, README.md
    dot_env = repo_dir / ".env"
    dot_gitignore = repo_dir / ".gitignore"
    readme_dot_md = repo_dir / "README.md"
    dot_env.touch()
    dot_gitignore.touch()
    readme_dot_md.touch()
    dot_env.write_text(get_template('dot_env.j2').render())
    dot_gitignore.write_text(get_template('dot_gitignore.j2').render())
    # might break if you don't utf-8 encode
    with open(readme_dot_md, 'wb') as readme_fh:
        output = get_template('readme.j2').render(project_name=project_name, repo_name=repo_name).encode('utf-8')
        readme_fh.write(output)
    #readme_dot_md.write_text(get_template('readme.j2').render(project_name=project_name, repo_name=repo_name).encode('utf-8'))

    # populate license file
    if license_type is not None:
        assert license_type in (1, 2, 3)
        license_template_files = {
            1: 'license_mit.j2',
            2: 'license_gpl.j2',
            3: 'license_apache.j2'
        }
        license_file = repo_dir / "LICENSE"  # remember to pre-populate the right kind of license     
        license_file.touch()
        template = get_template(license_template_files[license_type])
        year = str(datetime.now().year)
        license_file.write_text(template.render(year=year, author_name=author_name ))

    # create mlt_dependencies.py
    mlt_dependencies_file = repo_dir / 'mlt_dependencies.py'
    mlt_dependencies_file.write_text(get_template('mlt_dependencies.j2').render(s3_bucketname=s3_bucketname, aws_profile=aws_profile))

    #create .mlt directory
    mlt_init(project_name=project_name, repo_dir=repo_dir, ask_project_name=False)

def handle_project_creation():
    project_name, repo_name, author_name, license_type, aws_profile, s3_bucketname = get_project_config_info()
    create_project_directory(project_name, repo_name, author_name, license_type, aws_profile, s3_bucketname)

def get_mlt_config(repo_dir):
    dot_mlt_dir = repo_dir / ".mlt"
    mlt_config_filepath = dot_mlt_dir / 'mlt_config.pkl'

def get_vocab_from_mlt_dep(repo_dir):

    graph_data = get_mlt_graph_data(repo_dir)
    graph = graph_data["graph"]
    vocab = {}
    for node in graph:
        help_txt = node.get('help', '')
        if help_txt != '':
            outputs = node.get('outputs')
            for output in outputs:
                vocab[output] = help_txt
    return vocab

def refresh(repo_dir):
    mlt_dep_to_dot_makefile(repo_dir=repo_dir)

def is_mlt_init_required(repo_dir):
    
    mlt_init_needed = True

    dot_mlt = repo_dir / '.mlt'
    mlt_config_filepath = dot_mlt / 'mlt_config.pkl'

    if dot_mlt.exists() and mlt_config_filepath.exists():
        try:
            mlt_config = pickle.load(open(mlt_config_filepath, 'rb'))
            if mlt_config['repo_dir'].resolve() == repo_dir:
                mlt_init_needed = False
            else:
                mlt_init_needed = True
        except:
            mlt_init_needed = True
    else:
        mlt_init_needed = True
    return mlt_init_needed

def print_help_text(repo_dir):
    mlt_dep_filepath = repo_dir / "mlt_dependencies.py"

    mlt_init_needed = is_mlt_init_required(repo_dir=repo_dir)
    width = 30
    print("\n\n mlt - track and organize machine learning workflows from the terminal \n\n")
    print("FORMAT - ")
    print("\n mlt [command] \n")
    print("mlt commands: ")
    print("  create:".ljust(width)+"creates a new mlt repository")
    print("  init:".ljust(width)+"initializes existing repository for use with mlt")
    print("  help:".ljust(width)+"prints help text")

    if mlt_init_needed:
        print("\n No user defined commands available. \n")
        print("Cannot find mlt repo, or repository info in .mlt might be corrupted. Type 'mlt init' to initialize new mlt repository. Delete existing .mlt folder if one exists. \n")
        return
    
    if not mlt_dep_filepath.exists():
        print("\n No user defined commands available. \n")
        print("Define your project dependencies in mlt_dependencies.py")
        return
    
    vocab = get_vocab_from_mlt_dep(repo_dir=repo_dir)
    print("\n Commands defined in mlt_dependencies.py: \n")
    for key, val in vocab.items():
        key = "  "+key+":"
        print(key.ljust(width)+ val)

def run_command(command):
    process = subprocess.Popen(shlex.split(command), stdout=subprocess.PIPE, encoding='utf-8', shell=True)
    while True:
        output = process.stdout.readline()
        if output == b'' and process.poll() is not None:
            break
        if output:
            print(output)
    rc = process.poll()
    return rc

def parse_cmds():
    args = sys.argv[1:]
    #print(f"args: {args}")
    if args == []:
        print("\n type 'mlt help' for help text \n")
        return

    if len(args) > 1:
        raise Exception(f"did not understand args {args}")
    
    args = args[0]
    repo_dir = Path(os.getcwd())
    
    if args == "create":
        handle_project_creation()
        return
    if args == "init":
        project_name = ""
        mlt_init(project_name=project_name, repo_dir=repo_dir)
        return
    if args == "help" or args == "--help" or args == "-h":
        print_help_text(repo_dir=repo_dir)
        return
    
    mlt_init_needed = is_mlt_init_required(repo_dir=repo_dir)
    if mlt_init_needed:
        print("\n No user defined commands available. \n")
        print("Cannot find mlt repo, or repository info in .mlt might be corrupted. Type 'mlt init' to initialize new mlt repository. Delete existing .mlt folder if one exists.\n")
        return
    
    mlt_dep_filepath = repo_dir / "mlt_dependencies.py"
    if not mlt_dep_filepath.exists():
        print("\n No user defined commands available. \n")
        print("Define your project dependencies in mlt_dependencies.py")
        return

    vocab = get_vocab_from_mlt_dep(repo_dir=repo_dir)
    if args == "refresh":
        refresh(repo_dir=repo_dir)
        return
    if args in vocab:
        refresh(repo_dir=repo_dir)
        make_cmd = "make -f ./.mlt/.makefile "+args

        # from https://stackoverflow.com/a/28319191
        with Popen(shlex.split(make_cmd), stdout=PIPE, bufsize=1, universal_newlines=True) as p: 
            for line in p.stdout:
                line = re.sub('^make:', 'mlt:', line)
                print(line, end='') # process line here
                sys.stdout.flush()
                
        # TODO: investigate how to handle stderr in a friendlier way
        if p.returncode != 0:
            raise CalledProcessError(p.returncode, p.args)

        # print(f"running {make_cmd}")
        #subprocess.run(make_cmd, shell=True)

        # import shlex
        # print(shlex.split(make_cmd))
        # process = subprocess.Popen(shlex.split(make_cmd), stdout=subprocess.PIPE)
        # for line in process.stdout:
        #     line = line.decode('utf-8')
        #     line = re.sub('^make:', 'mlt:', line)
        #     sys.stdout.write(line)

        # process = subprocess.Popen([make_cmd], stdout=subprocess.PIPE)
        # for line in iter(process.stdout.readline, b''):  # replace '' with b'' for Python 3
        #     sys.stdout.write(line)
        return
    print("Did not recognize arguments to mlt. Type 'mlt help' to print help text")




def main():
    parse_cmds()
